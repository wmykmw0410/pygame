"""紙芝居のページを増やす"""
import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("ページ切り替え")
clock = pg.time.Clock()

img1 = pg.image.load("007_switch_screen/images/flower1.png")
img2 = pg.image.load("007_switch_screen/images/flower2.png")
img3 = pg.image.load("007_switch_screen/images/flower3.png")
img4 = pg.image.load("007_switch_screen/images/flower4.png")
next_img = pg.image.load("007_switch_screen/images/nextbtn.png")

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
    button_to_jump(btn1, 3)

def page3():
    screen.blit(img3, (0, 0))
    btn1 = screen.blit(next_img, (600, 540))
    button_to_jump(btn1, 4)

def page4():
    screen.blit(img4, (0, 0))
    btn1 = screen.blit(next_img, (600, 540))
    button_to_jump(btn1, 1)


page = 1

while True:
    if page == 1:
        page1()
    elif page == 2:
        page2()
    elif page == 3:
        page3()
    elif page == 4:
        page4()

    pg.display.update()
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
