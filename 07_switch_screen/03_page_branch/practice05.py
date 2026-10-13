"""
練習5: 枝分かれを追加する
03_page_branch/ex05.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(ページ1 → ページ2, 3 へ分岐 / ページ3 → ページ4, 5 へ分岐 / ページ2, 4, 5 → ページ1 へ戻る)
リポジトリのルートで実行する(python 07_switch_screen/03_page_branch/practice05.py)

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  1. ページ1の右 → ページ3の左、右のボタンをそれぞれ押す → どのページに進む?
  2. page3 の button_to_jump(btn1, 4) と (btn2, 5) の数字を入れ替える → 左のボタンはどこへ進む?
  3. page2 のリプレイボタンのジャンプ先 1 を 3 に変える → ページ2のリプレイボタンを押すと?
"""
import pygame as pg
import sys

pg.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("練習5: 枝分かれ紙芝居")
clock = pg.time.Clock()

img1 = pg.image.load("07_switch_screen/images/root1.png")
img2 = pg.image.load("07_switch_screen/images/root2.png")
img3 = pg.image.load("07_switch_screen/images/root3.png")
# ★ root4.png を読み込んで img4 に、root5.png を読み込んで img5 に代入する
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

def page1():
    screen.blit(img1, (0, 0))
    btn1 = screen.blit(next_img, (90, 220))
    btn2 = screen.blit(next_img, (590, 220))
    button_to_jump(btn1, 2)
    button_to_jump(btn2, 3)

def page2():
    screen.blit(img2, (0, 0))
    btn1 = screen.blit(replay_img, REPLAY_BTN_POS)
    button_to_jump(btn1, 1)

# ★ ページ3の関数 page3 を作る(img3 を描画 → next_img を (190, 320) と (490, 320) に描画して btn1, btn2 に受け取る
#     → btn1 を押したらページ4へ、btn2 を押したらページ5へ)

# ★ ページ4の関数 page4 を作る(img4 を描画 → replay_img を REPLAY_BTN_POS に描画 → 押したらページ1へ)

# ★ ページ5の関数 page5 を作る(img5 を描画 → replay_img を REPLAY_BTN_POS に描画 → 押したらページ1へ)


page = 1

while True:
    if page == 1:
        page1()
    elif page == 2:
        page2()
    # ★ page が 3, 4, 5 のとき、それぞれ page3(), page4(), page5() を呼ぶ分岐を足す

    pg.display.update()
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
