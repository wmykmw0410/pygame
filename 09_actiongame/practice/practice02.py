"""
練習2: 他のRectとの衝突判定
example/ex02.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(colliderect で、プレイヤーが緑の四角と衝突したかを調べる → 衝突したら移動を戻す)
リポジトリのルートで実行する(python 09_actiongame/practice/practice02.py)

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  実行する前に、結果を予想してみよう
  1. 右キーを押し続けて、緑の四角にぶつける → どこで止まる?
  2. 移動を戻す2行(myrect.x -= vx と myrect.y -= vy)をどちらも消す → どうなる?
  3. myrect.x -= vx の行だけ消して、右キーで緑の四角にぶつかる → どうなる?
  4. myrect.y -= vy の行だけ消して、右キーで緑の四角にぶつかる → どうなる?
  5. boxrect = pg.Rect(300, 200, 100, 100) の数字を変える → 緑の四角の位置と大きさは?
"""
from pathlib import Path
import pygame as pg
import sys

pg.init()
BASE_DIR = Path(__file__).resolve().parent.parent
IMG_DIR = BASE_DIR / "images"
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("練習2: アクションゲーム")
clock = pg.time.Clock()

## プレイヤーデータ
PLAYER_SIZE  = (40, 50)
PLAYER_SPEED = 4
myimgR = pg.image.load(IMG_DIR / "playerR.png")
myimgR = pg.transform.scale(myimgR, PLAYER_SIZE)
myimgL = pg.transform.flip(myimgR, True, False)
myrect = myimgR.get_rect(topleft=(50, 200))

## 障害物データ
boxrect = pg.Rect(300, 200, 100, 100)

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
    # ★ myrect が boxrect と衝突したら、移動を戻す(x と y の両方)

    if rightFlag:
        screen.blit(myimgR, myrect)
    else:
        screen.blit(myimgL, myrect)

    ## 障害物の処理
    pg.draw.rect(screen, pg.Color("DARKGREEN"), boxrect)

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
