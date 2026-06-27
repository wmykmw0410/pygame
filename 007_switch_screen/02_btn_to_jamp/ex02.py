"""ボタンでページが切り替わるプログラム"""
import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("ボタンでページ切り替え")
clock = pg.time.Clock()

img1 = pg.image.load("../images/flower1.png")
img2 = pg.image.load("../images/flower2.png")
next_img = pg.image.load("../images/nextbtn.png")

pushFlag = False


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
    btn1 = screen.blit(next_img, (600, 540))
    button_to_jump(btn1, 2)

def page2():
    screen.blit(img2, (0, 0))
    btn1 = screen.blit(next_img, (600, 540))
    button_to_jump(btn1, 1)


page = 1

while True:
    if page == 1:
        page1()
    elif page == 2:
        page2()

    pg.display.update()
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
