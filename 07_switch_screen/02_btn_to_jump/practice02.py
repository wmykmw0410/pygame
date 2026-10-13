"""
練習2: ボタンでページが切り替わるプログラム
02_btn_to_jump/ex02.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(押したら1回だけジャンプするボタン関数 button_to_jump を作る → 各ページから呼び出す)
リポジトリのルートで実行する(python 07_switch_screen/02_btn_to_jump/practice02.py)

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  1. NEXT_BTN_POS の (600, 540) を (100, 100) に変える → ボタンの位置と、反応する場所は?
  2. page1 の button_to_jump(btn1, 2) を (btn1, 1) に変える → ボタンを押すと?
  3. button_to_jump の中の pushFlag = True の行を消す → ボタンを押し続けるとどうなる?
  4. button_to_jump の中の global page, pushFlag の行を消す → どうなる?
"""
import pygame as pg
import sys

pg.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("練習2: ボタンでページ切り替え")
clock = pg.time.Clock()

img1 = pg.image.load("07_switch_screen/images/flower1.png")
img2 = pg.image.load("07_switch_screen/images/flower2.png")
next_img = pg.image.load("07_switch_screen/images/nextbtn.png")

pushFlag = False
NEXT_BTN_POS = (600, 540)


# ★ ボタンを押したら page を newpage にする関数 button_to_jump(btn, newpage) を作る
#     (global で page と pushFlag を使う / 押した瞬間だけ1回ジャンプするように pushFlag で管理する)


# ★ ページ1の関数 page1 を作る(img1 を描画 → next_img を NEXT_BTN_POS に描画して btn1 に受け取る → btn1 を押したらページ2へ)


# ★ ページ2の関数 page2 を作る(img2 を描画 → next_img を NEXT_BTN_POS に描画して btn1 に受け取る → btn1 を押したらページ1へ)


page = 1

while True:
    # ★ page が 1 なら page1() を、2 なら page2() を呼ぶ

    pg.display.update()
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
