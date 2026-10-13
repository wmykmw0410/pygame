"""
練習4: 進む道を選択する紙芝居
03_page_branch/ex04.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(1つのページに2つのボタンを置いて、押したボタンに応じて別のページへ進む)
リポジトリのルートで実行する(python 07_switch_screen/03_page_branch/practice04.py)

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  1. 左のボタン、右のボタンをそれぞれ押す → どのページに進む?
  2. page1 の button_to_jump(btn1, 2) と (btn2, 3) の数字を入れ替える → 左のボタンはどこへ進む?
  3. 2つのボタンの間(何もない場所)をクリックする → どうなる?
  4. REPLAY_BTN_POS の (600, 520) を (100, 100) に変える → リプレイボタンの位置は?
"""
import pygame as pg
import sys

pg.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("練習4: 枝分かれ紙芝居")
clock = pg.time.Clock()

img1 = pg.image.load("07_switch_screen/images/root1.png")
img2 = pg.image.load("07_switch_screen/images/root2.png")
img3 = pg.image.load("07_switch_screen/images/root3.png")
next_img = pg.image.load("07_switch_screen/images/nextbtn.png")
replay_img = pg.image.load("07_switch_screen/images/replaybtn.png")

pushFlag = False
REPLAY_BTN_POS = (600, 520)


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

# ★ ページ1の関数 page1 を作る(img1 を描画 → next_img を (90, 220) と (590, 220) に描画して btn1, btn2 に受け取る
#     → btn1 を押したらページ2へ、btn2 を押したらページ3へ)

# ★ ページ2の関数 page2 を作る(img2 を描画 → replay_img を REPLAY_BTN_POS に描画 → 押したらページ1へ)

# ★ ページ3の関数 page3 を作る(img3 を描画 → replay_img を REPLAY_BTN_POS に描画 → 押したらページ1へ)


page = 1

while True:
    # ★ page が 1, 2, 3 のとき、それぞれ page1(), page2(), page3() を呼ぶ

    pg.display.update()
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
