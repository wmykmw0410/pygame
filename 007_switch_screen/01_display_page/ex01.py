"""ページ1が表示されるプログラム"""
import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("ページ切り替え")
clock = pg.time.Clock()

img1 = pg.image.load("007_switch_screen/images/flower1.png")
img2 = pg.image.load("007_switch_screen/images/flower2.png")


def page1():
    screen.blit(img1, (0, 0))

def page2():
    screen.blit(img2, (0, 0))


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
