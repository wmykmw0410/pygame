"""
練習5: 罠と接触したらゲームオーバー
example/ex05.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(罠に触れたら page を 2 にする → ゲームオーバー画面でデータをリセットして、リプレイボタンを表示する)
リポジトリのルートで実行する(python 09_actiongame/practice/practice05.py)

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  実行する前に、結果を予想してみよう
  1. 罠に触れる → 画面はどうなる?
  2. ゲームオーバー画面のリプレイボタンを押す → どうなる? 罠の配置は前と同じ?
  3. RESULT_FONT_SIZE の 150 を 50 や 250 に変える → 文字の大きさは?
  4. REPLAY_BTN_POS の (320, 480) を (100, 100) に変える → ボタンの位置と、反応する場所は?
  5. gameover() の中の gamereset() の行を消す → リプレイボタンを押すと、どうなる?
"""
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
pg.display.set_caption("練習5: アクションゲーム")
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
    # ★ myrect が traps のいずれかと衝突したら、pi.wav の音を鳴らして、page を 2 にする

# ★ データのリセット: 関数 gamereset を作る
#   プレイヤーを (50, 100) に戻し、すべての罠の位置を、もう一度ランダムに決め直す

# ★ ゲームオーバー: 関数 gameover を作る
#   gamereset() を呼ぶ → 画面を NAVY で塗りつぶす → "GAMEOVER" を RED で (100, 200) に描画する
#   → replay_img を REPLAY_BTN_POS に描画して btn1 に受け取る → btn1 を押したらページ1へ(button_to_jump)

# ループ
while True:
    if page == 1:
        gamestage()
    # ★ page が 2 なら gameover() を呼ぶ
    # 画面を表示する
    pg.display.update()
    clock.tick(FPS)

    # 終了
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
