"""罠をたくさんばら撒く"""
from pathlib import Path
import pygame as pg
import sys
import random

pg.init()
BASE_DIR = Path(__file__).resolve().parent.parent
IMG_DIR = BASE_DIR / "images"
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
    wy = random.randint(20, 550)  # Y座標はランダム配置
    traps.append(pg.Rect(wx, wy, 30, 30))

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

# ループ
while True:
    gamestage()
    # 画面を表示する
    pg.display.update()
    clock.tick(60)

    # 終了
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
