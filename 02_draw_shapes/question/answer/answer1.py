"""四角を斜めに3秒移動させて、その後拡大させる"""
import pygame as pg
import sys

pg.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("斜め移動して拡大")
clock = pg.time.Clock()

MOVE_DURATION_MS = 3000  # 斜め移動を続ける時間(ミリ秒) = 3秒
MOVE_SPEED = 2

myrect = pg.Rect(100, 100, 100, 100)
start_time = pg.time.get_ticks()

while True:
    screen.fill(pg.Color("WHITE"))

    elapsed = pg.time.get_ticks() - start_time  # 経過時間(ミリ秒)

    if elapsed < MOVE_DURATION_MS:
        # 3秒間は斜めに移動
        myrect.x += MOVE_SPEED
        myrect.y += MOVE_SPEED
    else:
        # 3秒後は拡大
        myrect.width += 1
        myrect.height += 1

    pg.draw.rect(screen, pg.Color("RED"), myrect)
    pg.display.update()
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
