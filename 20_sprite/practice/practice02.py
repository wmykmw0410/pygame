"""
練習2: Group で複数の敵をまとめて動かす
example/ex02.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(Enemy クラスは ex01 と同じ。3枚の画像から3体を作って Group に入れ、update() と draw() をまとめて呼ぶ)
実行のしかた: リポジトリのルートで python 20_sprite/practice/practice02.py

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  1. ENEMY_X_GAP を 50 にする → 最初の並びはどうなる?
  2. enemy_imgs に enemy1.png と enemy2.png をもう1つずつ足す → 敵は何体になる?
  3. enemies.draw(screen) の行を消す → 画面はどうなる?
  4. enemies.update() の行を消す → 敵はどうなる?
"""
from pathlib import Path
import pygame as pg
import sys
import random

pg.init()
WIDTH, HEIGHT = 600, 400
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("練習2: Group で複数の敵を動かす")
clock  = pg.time.Clock()
IMG_DIR = Path(__file__).resolve().parent.parent / "images"
FPS = 60

ENEMY_SPEED_CHOICES = [-3, -2, 2, 3]
ENEMY_START_X = 100
ENEMY_START_Y = 100
ENEMY_X_GAP   = 150

# ★ Enemy クラスを定義する(ex01 と同じ)


# ★ enemy_imgs に、enemy1.png, enemy2.png, enemy3.png を読み込んだ画像のリストを作る

# ★ enemies = pg.sprite.Group() を作り、enumerate() で画像を取り出して、横に ENEMY_X_GAP ずつずらした位置に Enemy を add() する

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill(pg.Color("NAVY"))

    # ★ enemies.update() で全員を動かし、enemies.draw(screen) で全員を描く

    pg.display.update()
    clock.tick(FPS)
