"""
練習8: イベント方式でキーとマウスの入力を検知するプログラム
04_event/ex08.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(スペースキーを押した瞬間に四角を表示する / マウス左ボタンを押した瞬間に四角を消す)

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  1. pg.K_SPACE を pg.K_RETURN に変える → 四角を出すキーは?
  2. スペースキーを押し続ける → 表示は何回?
  3. event.button == 1 を 3 に変える → どのボタンで消える?(左ボタンは?)
  4. pg.MOUSEBUTTONDOWN を pg.MOUSEBUTTONUP に変える → いつ消える?
  5. pg.KEYDOWN を pg.KEYUP に変える → いつ表示される?
"""
import pygame as pg
import sys

pg.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("練習8: イベント方式の入力検知")
clock = pg.time.Clock()

show_rect = False

while True:
    screen.fill(pg.Color("WHITE"))

    # 絵を描いたり、判定したりする
    # ★ show_rect が True なら、(300, 200) に幅200・高さ200の赤い四角を描く

    pg.display.update()
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        # キーを押した瞬間(1回だけ実行)
        # ★ スペースキーが押されたら、show_rect を True にして「スペース押した: 四角を表示」と表示する

        # マウス左ボタンを押した瞬間(1回だけ実行)
        # ★ マウス左ボタンが押されたら、show_rect を False にして「マウス押した: 四角を消す」と表示する
