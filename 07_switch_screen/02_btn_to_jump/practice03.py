"""
練習3: 紙芝居のページを増やす
02_btn_to_jump/ex03.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(画像の読み込みを追加する → ページ切り替え関数を追加する → ループを修正する)
リポジトリのルートで実行する(python 07_switch_screen/02_btn_to_jump/practice03.py)

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  1. ボタンを順番に押していく → ページはどの順番で進む?
  2. page4 の button_to_jump(btn1, 1) を (btn1, 2) に変える → ページ4の次は?
  3. page2 の button_to_jump(btn1, 3) を (btn1, 1) に変える → ページ3、4には行ける?
"""
import pygame as pg
import sys

pg.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("練習3: ページ切り替え")
clock = pg.time.Clock()

img1 = pg.image.load("07_switch_screen/images/flower1.png")
img2 = pg.image.load("07_switch_screen/images/flower2.png")
# ★ flower3.png を読み込んで img3 に、flower4.png を読み込んで img4 に代入する
next_img = pg.image.load("07_switch_screen/images/nextbtn.png")

pushFlag = False
NEXT_BTN_POS = (600, 540)


def button_to_jump(btn, newpage):
    global page, pushFlag

    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()
    if mdown[0]:
        if btn.collidepoint(mx, my) and not pushFlag:
            page = newpage
            pushFlag = True
    else:
        pushFlag = False

def page1():
    screen.blit(img1, (0, 0))
    btn1 = screen.blit(next_img, NEXT_BTN_POS)
    button_to_jump(btn1, 2)

def page2():
    screen.blit(img2, (0, 0))
    btn1 = screen.blit(next_img, NEXT_BTN_POS)
    button_to_jump(btn1, 1)  # ★ ジャンプ先を 3 に書き換える

# ★ ページ3の関数 page3 を作る(img3 を描画 → ボタンを描画 → 押したらページ4へ)

# ★ ページ4の関数 page4 を作る(img4 を描画 → ボタンを描画 → 押したらページ1へ)


page = 1

while True:
    if page == 1:
        page1()
    elif page == 2:
        page2()
    # ★ page が 3 なら page3() を、4 なら page4() を呼ぶ分岐を足す

    pg.display.update()
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
