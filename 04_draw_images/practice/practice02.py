"""
練習2: 車の画像サイズを変更する
example/ex02.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(画像を読み込む → サイズを(50, 50)に変更する → 描画する)

動いたら、数字を書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  1. (50, 50) を (200, 200) や (10, 10) に変える
  2. (200, 50) や (50, 200) に変える → 画像はどうなる?
  3. 元のサイズは (100, 100)。比率をそろえて (150, 150) にすると?
"""
# 1.ゲームの準備をする
import pygame as pg
import sys

pg.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("練習2: 車の画像サイズを変更する")
clock = pg.time.Clock()
# ★ 画像を読み込んで img1 に代入する

# ★ img1 のサイズを (50, 50) に変更して img1 に入れ直す


# 2.この下をずっとループする
while True:
    # 3.画像を初期化する
    screen.fill(pg.Color("WHITE"))
    # 5.絵を描いたり、判定したりする
    # ★ img1 を (100, 100) に描画する

    # 6.画像を表示する
    pg.display.update()
    clock.tick(FPS)
    # 7.閉じるボタンを押したら終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
