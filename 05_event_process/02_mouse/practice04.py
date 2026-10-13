"""
練習4: マウスを押して位置を表示するプログラム
02_mouse/ex04.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(マウスのボタンと座標を調べる → 左ボタンが押されていたら座標を表示する)

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  1. ボタンを押さずにマウスを動かす → 表示される?
  2. ボタンを押したままマウスを動かす → 表示はどうなる?
  3. mdown[0] を mdown[2] に変える → どのボタンで表示される?
  4. mdown[0] のままで右ボタンを押す → 表示される?
  5. print(mx, my) を print("x =", mx, "y =", my) に変える → 表示はどう変わる?
"""
# ゲームの準備
import pygame as pg
import sys

pg.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("練習4: マウスを押して位置を表示する")
clock = pg.time.Clock()

# ループ
while True:

    # 画面の初期化
    screen.fill(pg.Color("WHITE"))

    # ユーザからの入力を調べる
    # ★ マウスのボタンの状態を調べて mdown に代入する

    # ★ マウスの座標を調べて (mx, my) に代入する

    # 絵を描いたり、判定する
    # ★ 左ボタンが押されていたら、マウスの座標を表示する

    # 画面を表示する
    pg.display.update()
    clock.tick(FPS)

    # 閉じるボタンが押されたら、終了
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
