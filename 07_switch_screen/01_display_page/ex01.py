"""ページ1が表示されるプログラム"""
import pygame as pg
import sys

pg.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("ページ切り替え")
clock = pg.time.Clock()

img1 = pg.image.load("07_switch_screen/images/flower1.png")
img2 = pg.image.load("07_switch_screen/images/flower2.png")


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
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
