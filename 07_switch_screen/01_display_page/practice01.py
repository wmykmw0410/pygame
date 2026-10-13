"""
練習1: ページ1が表示されるプログラム
01_display_page/ex01.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(ページごとに関数を作る → 変数 page で表示するページを決める → ループで page を見て関数を呼ぶ)
リポジトリのルートで実行する(python 07_switch_screen/01_display_page/practice01.py)

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  1. page = 1 を page = 2 に変える → 最初に表示されるページは?
  2. page = 3 に変える(ページ3の関数も分岐も無い) → どうなる?
  3. screen.blit(img1, (0, 0)) の (0, 0) を (100, 100) に変える → 画面はどうなる?
  4. ループの中の page == 1 の分岐(if)を消す → どうなる?
"""
import pygame as pg
import sys

pg.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("練習1: ページ切り替え")
clock = pg.time.Clock()

img1 = pg.image.load("07_switch_screen/images/flower1.png")
img2 = pg.image.load("07_switch_screen/images/flower2.png")


# ★ ページ1の関数 page1 を作る(img1 を (0, 0) に描画する)


# ★ ページ2の関数 page2 を作る(img2 を (0, 0) に描画する)


# ★ 今のページを表す変数 page を 1 にしておく


while True:
    # ★ page が 1 なら page1() を、2 なら page2() を呼ぶ

    pg.display.update()
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
