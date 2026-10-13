"""
練習1: Sprite で1体を動かす
example/ex01.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(pg.sprite.Sprite を継承した Enemy クラスを作る → 1体作って、動かして描く)
実行のしかた: リポジトリのルートで python 20_sprite/practice/practice01.py

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  1. ENEMY_SPEED_CHOICES を [1] にする → 動きはどうなる?
  2. ENEMY_SPEED_CHOICES を [0, 3] にして、何度か実行し直す → 動きはどうなる?
  3. ENEMY_START_POS を (500, 300) にする → どこから動き始める?
  4. update() の中の self.vy = -self.vy の行を消す → 上や下の壁に当たるとどうなる?
  5. FPS を 10 にする → 動きはどうなる?
"""
from pathlib import Path
import pygame as pg
import sys
import random

pg.init()
WIDTH, HEIGHT = 600, 400
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("練習1: 1体を動かす")
clock  = pg.time.Clock()
IMG_DIR = Path(__file__).resolve().parent.parent / "images"
FPS = 60

ENEMY_SPEED_CHOICES = [-3, -2, 2, 3]
ENEMY_START_POS     = (100, 100)

# ★ pg.sprite.Sprite を継承した Enemy クラスを定義する
#   __init__(self, img, x, y): super().__init__() を呼ぶ
#     self.image に img を入れる
#     self.rect に、self.image.get_rect(topleft=(x, y)) を入れる
#     self.vx と self.vy に、ENEMY_SPEED_CHOICES から random.choice() で選んだ値を入れる
#   update(self): self.rect.x と self.rect.y を vx, vy だけ動かす
#     左右の壁(0 と WIDTH)に当たったら vx の向きを逆にする
#     上下の壁(0 と HEIGHT)に当たったら vy の向きを逆にする


# ★ enemy_img に enemy1.png を読み込み、ENEMY_START_POS の位置に Enemy を作って enemy に入れる(座標は * で展開する)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill(pg.Color("NAVY"))

    # ★ enemy.update() を呼び、screen.blit() で enemy.image を enemy.rect の位置に描く

    pg.display.update()
    clock.tick(FPS)
