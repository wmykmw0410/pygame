"""
練習4: キー操作で Group を操作する
example/ex04.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(spawn_enemy() で Group に追加する → ↑で追加、↓でランダムに1体削除、SPACEで全削除、敵の数を画面に表示する)
実行のしかた: リポジトリのルートで python 20_sprite/practice/practice04.py

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  1. MAX_ENEMIES を 5 にして、↑キーを何度も押す → 敵は何体まで増える?
  2. ↓キーの処理の if len(enemies) > 0: を if True: に変えて、SPACE で全削除してから ↓キーを押す → どうなる?
  3. COUNT_POS を (400, 350) にする → 数の表示はどうなる?
  4. FONT_SIZE を 60 にする → 数の表示はどうなる?
  5. spawn_enemy() の WIDTH - ENEMY_SIZE を WIDTH にして、↑キーで敵を増やす → 出現する位置はどうなる?
"""
from pathlib import Path
import pygame as pg
import sys
import random

pg.init()
WIDTH, HEIGHT = 600, 400
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("練習4: ↑追加 / ↓削除 / SPACEで全削除")
clock  = pg.time.Clock()
IMG_DIR = Path(__file__).resolve().parent.parent / "images"
FPS = 60

FONT_SIZE = 28
font      = pg.font.Font(None, FONT_SIZE)
COUNT_POS = (10, 10)

MAX_ENEMIES = 20

ENEMY_SPEED_CHOICES = [-3, -2, 2, 3]
ENEMY_SIZE    = 50
ENEMY_START_X = 100
ENEMY_START_Y = 100
ENEMY_X_GAP   = 150

# ★ Enemy クラスを定義する(ex02 と同じ)


# ★ spawn_enemy() を定義する
#   len(enemies) が MAX_ENEMIES 以上なら return する
#   enemy_imgs からランダムに1枚選び、画面に収まる範囲のランダムな位置に Enemy を作って enemies.add() する


# ★ enemy_imgs を読み込み、最初の3体を enemies に入れる(ex02 と同じ)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        # ★ KEYDOWN のとき: ↑なら spawn_enemy()、↓なら(敵がいれば)ランダムに1体 remove()、SPACE なら enemies.empty()

    screen.fill(pg.Color("NAVY"))

    # ★ enemies.update() と enemies.draw(screen) を呼ぶ

    # ★ font.render() で、f"Enemies: {len(enemies)}" を白い文字にして、COUNT_POS に描く

    pg.display.update()
    clock.tick(FPS)
