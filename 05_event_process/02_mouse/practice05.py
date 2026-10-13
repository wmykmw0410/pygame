"""
練習5: マウスを押した場所に四角を描くプログラム
02_mouse/ex05.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(マウスの状態を調べる → 左ボタンが押されていたら、マウスの位置が中心になるように四角を描く)

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  1. RECT_SIZE の 100 を 20 や 200 に変える → 四角の大きさは?
  2. 左ボタンを離す → 四角はどうなる?
  3. 四角の位置の mx - RECT_SIZE // 2, my - RECT_SIZE // 2 を mx, my に変える → 四角はマウスのどこにくる?
  4. mdown[0] を mdown[2] に変える → どのボタンで描かれる?
  5. pg.Color("RED") を別の色に変える
"""
# ゲームの準備
import pygame as pg
import sys

pg.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("練習5: マウスを押した場所に四角を描く")
clock = pg.time.Clock()
RECT_SIZE = 100

# ループ
while True:

    # 画面の初期化
    screen.fill(pg.Color("WHITE"))

    # ユーザからの入力を調べる
    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()

    # 絵を描いたり、判定する
    # ★ 左ボタンが押されていたら、マウスの位置が中心になるように赤い四角(1辺 RECT_SIZE)を描く

    # 画面を表示する
    pg.display.update()
    clock.tick(FPS)

    # 閉じるボタンが押されたら、終了
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
