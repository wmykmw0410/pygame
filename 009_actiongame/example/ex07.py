"""追いかけてくるオバケ"""
from pathlib import Path
import pygame as pg
import sys
import random

pg.init()
BASE_DIR = Path(__file__).resolve().parent.parent
IMG_DIR = BASE_DIR / "images"
SND_DIR = BASE_DIR / "sounds"
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("アクションゲーム")
clock = pg.time.Clock()

## プレイヤーデータ
myimgR = pg.image.load(IMG_DIR / "playerR.png")
myimgR = pg.transform.scale(myimgR, (40, 50))
myimgL = pg.transform.flip(myimgR, True, False)
myrect = myimgR.get_rect(topleft=(50, 200))

## 壁データ
walls = [pg.Rect(0, 0, 800, 20),
         pg.Rect(0, 0, 20, 600),
         pg.Rect(780, 0, 20, 600),
         pg.Rect(0, 580, 800, 20)]

## 罠データ
trapimg = pg.image.load(IMG_DIR / "uni.png")
trapimg = pg.transform.scale(trapimg, (30, 30))
traps = []
for i in range(20):
    wx = 150 + i * 30
    wy = random.randint(20, 550)
    traps.append(pg.Rect(wx, wy, 30, 30))

## ボタンデータ
replay_img = pg.image.load(IMG_DIR / "replaybtn.png")
goalrect = pg.Rect(750, 250, 30, 100)

## オバケデータ
enemyimgR = pg.image.load(IMG_DIR / "obake.png")
enemyimgR = pg.transform.scale(enemyimgR, (50, 50))
enemyimgL = pg.transform.flip(enemyimgR, True, False)
enemyrect = enemyimgR.get_rect(topleft=(650, 200))

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
        vx = 4
        rightFlag = True
    if key[pg.K_LEFT]:
        vx = -4
        rightFlag = False
    if key[pg.K_UP]:
        vy = -4
    if key[pg.K_DOWN]:
        vy = 4

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

    ## オバケの処理
    ovx = 1 if enemyrect.x < myrect.x else -1  # プレイヤーの方向に1ずつ近づく
    ovy = 1 if enemyrect.y < myrect.y else -1
    enemyrect.x += ovx
    enemyrect.y += ovy
    if ovx > 0:
        screen.blit(enemyimgR, enemyrect)
    else:
        screen.blit(enemyimgL, enemyrect)
    if myrect.colliderect(enemyrect):  # オバケに触れたらゲームオーバー
        pg.mixer.Sound(SND_DIR / "down.wav").play()
        page = 2

## データのリセット
def gamereset():
    myrect.x = 50
    myrect.y = 100
    for d in range(20):
        traps[d].x = 150 + d * 30
        traps[d].y = random.randint(20, 550)
    enemyrect.x = 650
    enemyrect.y = 200

## ゲームオーバー
def gameover():
    gamereset()
    screen.fill(pg.Color("NAVY"))
    font = pg.font.Font(None, 150)
    text = font.render("GAMEOVER", True, pg.Color("RED"))
    screen.blit(text, (100, 200))
    btn1 = screen.blit(replay_img, (320, 480))
    # 描画や判定
    button_to_jump(btn1, 1)

## ゲームクリア
def gameclear():
    gamereset()
    screen.fill(pg.Color("GOLD"))
    font = pg.font.Font(None, 150)
    text = font.render("GAMECLEAR", True, pg.Color("RED"))
    screen.blit(text, (60, 200))
    btn1 = screen.blit(replay_img, (320, 480))
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
    clock.tick(60)

    # 終了
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
