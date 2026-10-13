"""
練習1: キャラクタを上下左右に動かす
example/ex01.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(プレイヤーの画像とRectを用意する → キーで vx, vy を決める → Rectを動かして、向きに合わせた画像を描画する)
リポジトリのルートで実行する(python 09_actiongame/practice/practice01.py)
(練習2〜7でも、前の練習で作った部分は最初から書いてあり、新しく習う部分だけが空欄になっている)

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  実行する前に、結果を予想してみよう
  1. PLAYER_SPEED の 4 を 1 や 10 に変える → 動く速さは?
  2. 右キーと上キーを同時に押す → どの向きに動く?
  3. 左キーを押してから離す → キャラクタの向きは? (rightFlag は何を覚えている?)
  4. 緑の四角(boxrect)の上を通る → 何か起きる?
  5. PLAYER_SIZE の (40, 50) を (80, 100) に変える → 何が変わる?
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
pg.display.set_caption("練習1: アクションゲーム")
clock = pg.time.Clock()

## プレイヤーデータ
PLAYER_SIZE  = (40, 50)
PLAYER_SPEED = 4
# ★ playerR.png を読み込み、PLAYER_SIZE に縮小して myimgR に代入する
# ★ myimgR を左右反転した画像を myimgL に代入する
# ★ myimgR の Rect を、左上が (50, 200) になるように取得して myrect に代入する

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
    # ★ 右キーなら vx を PLAYER_SPEED に、rightFlag を True にする
    # ★ 左キーなら vx を -PLAYER_SPEED に、rightFlag を False にする
    # ★ 上キーなら vy を -PLAYER_SPEED に、下キーなら vy を PLAYER_SPEED にする

    ## プレイヤーの処理
    # ★ myrect の x に vx、y に vy を足して動かす
    # ★ rightFlag が True なら myimgR を、そうでなければ myimgL を myrect の位置に描画する

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
