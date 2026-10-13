"""
練習1: 車の画像を表示する
example/ex01.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(画像を読み込む → 描画する)

動いたら、数字を書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  1. 描画する位置 (100, 100) を (400, 300) に変える
  2. (0, 0) や (750, 550) に変える → 画面の端ではどうなる?
  3. 同じ画像を、少しずらした位置にもう1回 blit する → どちらが上に重なる?
     その2行の順番を入れ替えると?
"""
# 1.ゲームの準備をする
import pygame as pg
import sys

pg.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("練習1: 車の画像を表示する")
clock = pg.time.Clock()
# ★ 画像を読み込んで img1 に代入する


# ★ 画像のデフォルトサイズを表示する


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
