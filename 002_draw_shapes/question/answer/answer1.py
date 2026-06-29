"""四角を斜めに3秒移動させて、その後拡大させる"""
import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("斜め移動して拡大")
clock = pg.time.Clock()

myrect = pg.Rect(100, 100, 100, 100)
start_time = pg.time.get_ticks()

while True:
    screen.fill(pg.Color("WHITE"))

    elapsed = pg.time.get_ticks() - start_time  # 経過時間(ミリ秒)

    if elapsed < 3000:
        # 3秒間は斜めに移動
        myrect.x += 2
        myrect.y += 2
    else:
        # 3秒後は拡大
        myrect.width += 1
        myrect.height += 1

    pg.draw.rect(screen, pg.Color("RED"), myrect)
    pg.display.update()
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
