"""
練習3: 敵同士の衝突判定
example/ex03.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(Enemy に bounce() を足す → Group を sprites() でリストにして、総当たりで colliderect() を調べる)
実行のしかた: リポジトリのルートで python 20_sprite/practice/practice03.py

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  1. ENEMY_X_GAP を 30 にする → 最初から重なっている敵は、どうなる?
  2. bounce() の中の self.vy = -self.vy の行を消す → 敵同士がぶつかったとき、どうなる?
  3. 衝突判定の enemy_list[i].bounce() と enemy_list[j].bounce() を pass に変える → 敵同士がぶつかると、どうなる?
"""
from pathlib import Path
import pygame as pg
import sys
import random

pg.init()
WIDTH, HEIGHT = 600, 400
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("練習3: 敵同士がぶつかったら跳ね返る")
clock  = pg.time.Clock()
IMG_DIR = Path(__file__).resolve().parent.parent / "images"
FPS = 60

ENEMY_SPEED_CHOICES = [-3, -2, 2, 3]
ENEMY_START_X = 100
ENEMY_START_Y = 100
ENEMY_X_GAP   = 150

# ★ Enemy クラスを定義する(ex02 と同じ。さらに bounce(self) で vx と vy の向きを逆にする)


# ★ enemy_imgs を読み込み、enemies の Group を作る(ex02 と同じ)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill(pg.Color("NAVY"))

    # ★ enemies.update() を呼ぶ
    # ★ enemy_list = enemies.sprites() でリストにする
    # ★ 2重の for ループ(i と、i + 1 以降の j)で、rect.colliderect() が True なら、2体とも bounce() を呼ぶ
    # ★ enemies.draw(screen) を呼ぶ

    pg.display.update()
    clock.tick(FPS)
