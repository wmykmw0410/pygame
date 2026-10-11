"""ゴールと衝突したらゲームクリア"""
from pathlib import Path
import pygame as pg
import sys
import random

pg.init()
BASE_DIR = Path(__file__).resolve().parent.parent
IMG_DIR = BASE_DIR / "images"
SND_DIR = BASE_DIR / "sounds"
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("アクションゲーム")
clock = pg.time.Clock()

## プレイヤーデータ
PLAYER_SIZE  = (40, 50)
PLAYER_SPEED = 4
myimgR = pg.image.load(IMG_DIR / "playerR.png")
myimgR = pg.transform.scale(myimgR, PLAYER_SIZE)
myimgL = pg.transform.flip(myimgR, True, False)
myrect = myimgR.get_rect(topleft=(50, 200))

## 壁データ
WALL_THICKNESS = 20
walls = [pg.Rect(0, 0, WIDTH, WALL_THICKNESS),
         pg.Rect(0, 0, WALL_THICKNESS, HEIGHT),
         pg.Rect(WIDTH - WALL_THICKNESS, 0, WALL_THICKNESS, HEIGHT),
         pg.Rect(0, HEIGHT - WALL_THICKNESS, WIDTH, WALL_THICKNESS)]

## 罠データ
TRAP_COUNT   = 20
TRAP_SPACING = 30
TRAP_SIZE    = (30, 30)
TRAP_START_X = 150
TRAP_Y_MIN   = 20
TRAP_Y_MAX   = 550
trapimg = pg.image.load(IMG_DIR / "uni.png")
trapimg = pg.transform.scale(trapimg, TRAP_SIZE)
traps = []
for i in range(TRAP_COUNT):
    wx = TRAP_START_X + i * TRAP_SPACING
    wy = random.randint(TRAP_Y_MIN, TRAP_Y_MAX)
    traps.append(pg.Rect(wx, wy, *TRAP_SIZE))

## ボタンデータ
REPLAY_BTN_POS   = (320, 480)
RESULT_FONT_SIZE = 150
replay_img = pg.image.load(IMG_DIR / "replaybtn.png")
goalrect = pg.Rect(750, 250, 30, 100)

## メインループで使う変数
rightFlag = True
pushFlag = False
page = 1

## btnを押したら、newpageにジャンプする
def button_to_jump(btn, newpage):
    global page, pushFlag
    # ユーザーからの入力を調べる
    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()
    if mdown[0]:
        if btn.collidepoint(mx, my) and not pushFlag:
            pg.mixer.Sound(SND_DIR / "pi.wav").play()
            page = newpage
            pushFlag = True
    else:
        pushFlag = False

# ゲームステージ
def gamestage():
    global rightFlag, page

    # 画面を初期化する
    screen.fill(pg.Color("DEEPSKYBLUE"))
    vx = 0
    vy = 0

    # ユーザーからの入力
    key = pg.key.get_pressed()

    # 描画や判定
    if key[pg.K_RIGHT]:
        vx = PLAYER_SPEED
        rightFlag = True
    if key[pg.K_LEFT]:
        vx = -PLAYER_SPEED
        rightFlag = False
    if key[pg.K_UP]:
        vy = -PLAYER_SPEED
    if key[pg.K_DOWN]:
        vy = PLAYER_SPEED

    ## プレイヤーの処理
    myrect.x += vx
    myrect.y += vy
    if myrect.collidelist(walls) != -1:
        myrect.x -= vx
        myrect.y -= vy

    if rightFlag:
        screen.blit(myimgR, myrect)
    else:
        screen.blit(myimgL, myrect)

    ## 壁の処理
    for wall in walls:
        pg.draw.rect(screen, pg.Color("DARKGREEN"), wall)

    ## 罠の処理
    for trap in traps:
        screen.blit(trapimg, trap)
    if myrect.collidelist(traps) != -1:  # 罠に触れたらゲームオーバー
        pg.mixer.Sound(SND_DIR / "pi.wav").play()
        page = 2

    ## ゴールの処理
    pg.draw.rect(screen, pg.Color("GOLD"), goalrect)
    if myrect.colliderect(goalrect):  # ゴールに触れたらゲームクリア
        pg.mixer.Sound(SND_DIR / "up.wav").play()
        page = 3

## データのリセット
def gamereset():
    myrect.x = 50
    myrect.y = 100
    for d in range(TRAP_COUNT):
        traps[d].x = TRAP_START_X + d * TRAP_SPACING
        traps[d].y = random.randint(TRAP_Y_MIN, TRAP_Y_MAX)

## ゲームオーバー
def gameover():
    gamereset()
    screen.fill(pg.Color("NAVY"))
    font = pg.font.Font(None, RESULT_FONT_SIZE)
    text = font.render("GAMEOVER", True, pg.Color("RED"))
    screen.blit(text, (100, 200))
    btn1 = screen.blit(replay_img, REPLAY_BTN_POS)
    # 描画や判定
    button_to_jump(btn1, 1)

## ゲームクリア
def gameclear():
    gamereset()
    screen.fill(pg.Color("GOLD"))
    font = pg.font.Font(None, RESULT_FONT_SIZE)
    text = font.render("GAMECLEAR", True, pg.Color("RED"))
    screen.blit(text, (60, 200))
    btn1 = screen.blit(replay_img, REPLAY_BTN_POS)
    # 描画や判定
    button_to_jump(btn1, 1)

# ループ
while True:
    if page == 1:
        gamestage()
    elif page == 2:
        gameover()
    elif page == 3:
        gameclear()
    # 画面を表示する
    pg.display.update()
    clock.tick(FPS)

    # 終了
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
