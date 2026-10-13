"""
練習4: 罠をたくさんばら撒く
example/ex04.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(random.randint で Y座標をランダムに決めて、罠の Rect をリストに追加する → for 文でまとめて描画する)
リポジトリのルートで実行する(python 09_actiongame/practice/practice04.py)

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  実行する前に、結果を予想してみよう
  1. プログラムを何回か実行し直す → 罠の位置は、毎回同じ? 違う?
  2. TRAP_COUNT の 20 を 5 や 40 に変える → 罠の数は? 40 にすると、どうなる?
  3. TRAP_SPACING の 30 を 60 に変える → 罠の間隔は? 画面に収まる?
  4. TRAP_Y_MIN と TRAP_Y_MAX を 100 と 150 に変える → 罠はどこに並ぶ?
  5. 罠の上を通る → 何か起きる? (この時点では、当たり判定をしていない)
"""
from pathlib import Path
import pygame as pg
import sys
import random

pg.init()
BASE_DIR = Path(__file__).resolve().parent.parent
IMG_DIR = BASE_DIR / "images"
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("練習4: アクションゲーム")
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
# ★ uni.png を読み込み、TRAP_SIZE に縮小して trapimg に代入する
# ★ 空のリスト traps を用意する
# ★ TRAP_COUNT 回くり返して、x は TRAP_START_X + i * TRAP_SPACING、y は TRAP_Y_MIN〜TRAP_Y_MAX のランダムな値で、
#   大きさ TRAP_SIZE の Rect を traps に追加する

## メインループで使う変数
rightFlag = True

# ゲームステージ
def gamestage():
    global rightFlag

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
    # ★ traps のすべての罠に、trapimg を描画する

# ループ
while True:
    gamestage()
    # 画面を表示する
    pg.display.update()
    clock.tick(FPS)

    # 終了
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
