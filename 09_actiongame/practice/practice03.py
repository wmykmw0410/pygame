"""
練習3: 複数のRectとの衝突判定
example/ex03.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(壁の Rect をリストにする → collidelist で、どれかの壁と衝突したかを調べる → 壁を描画する)
リポジトリのルートで実行する(python 09_actiongame/practice/practice03.py)

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  実行する前に、結果を予想してみよう
  1. 4つの壁にそれぞれぶつかるまで進む → 画面の外に出られる?
  2. WALL_THICKNESS の 20 を 40 に変える → 動ける範囲は?
  3. WALL_THICKNESS を 100 にする → 動ける? (プレイヤーの最初の位置 x=50 は、壁の中になる)
  4. 下の壁(4つ目の Rect)をリストから消す → 下に進み続けると?
  5. if の前に print(myrect.collidelist(walls)) を足す → 壁にぶつかっているときと、いないときで、何が表示される?
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
pg.display.set_caption("練習3: アクションゲーム")
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
# ★ 上・左・右・下の4つの壁の Rect をリスト walls にする(WIDTH, HEIGHT, WALL_THICKNESS を使う)

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
    # ★ myrect が walls のいずれかと衝突したら(collidelist が -1 でなければ)、移動を戻す

    if rightFlag:
        screen.blit(myimgR, myrect)
    else:
        screen.blit(myimgL, myrect)

    ## 壁の処理
    # ★ walls のすべての壁を、DARKGREEN で描画する

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
