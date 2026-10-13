"""
練習4: 四角形が横に移動する
03_rect_object/ex04.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(Rectを用意する → ループの中でxに1を足す → Rectを使って四角を描く)

動いたら、数字を書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  1. myrect.x += 1 の 1 を 5 や -1 に変える → 動く速さと向きは?
  2. その下に myrect.y += 1 を足す → どの向きに動く?
  3. pg.Rect(100, 100, 100, 150) の 100, 150 (幅と高さ)を変える → 何が変わる?
  4. pg.Rect(100, 100, ...) の最初の2つを (0, 400) に変える → 動き始める位置は?
  5. FPS = 60 を 10 に変える → 動きはどう見える?
  6. 画面の右端(800)まで動き続けると、四角はどうなる?
"""
# ゲームの準備をする
import pygame as pg
import sys

pg.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("練習4: 四角形が横に移動する")
clock = pg.time.Clock()
# ★ 位置(100, 100)・幅100・高さ150の Rect を作って myrect に代入する


# この下をずっとループする
while True:
    # 画面を初期化する
    screen.fill(pg.Color("WHITE"))
    # 絵を描いたり、判定したりする
    # ★ myrect.x に 1 を足す

    # ★ 赤い四角を myrect で描く

    # 画面を表示する
    pg.display.update()
    clock.tick(FPS)
    # 閉じるボタンを押されたら終了
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
