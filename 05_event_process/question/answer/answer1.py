"""マウスの座標をトレースして文字を書くプログラム

・左ボタンを押している間、マウスの動きに沿って線を描く
・ボタンを離すと描くのをやめる
・Cキーを押すと画面をまっさらにする
"""

import pygame as pg
import sys

pg.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("マウスで文字を書く")
clock = pg.time.Clock()

PEN_COLOR = pg.Color("BLACK")
PEN_WIDTH = 4

canvas = pg.Surface((WIDTH, HEIGHT))
canvas.fill(pg.Color("WHITE"))

prev_pos = (0, 0)
drawFlag = False   # True: 直前のフレームも描いていた（線をつなぐ） / False: 今回が描き始め（点を打つ）

while True:
    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()
    key = pg.key.get_pressed()

    if mdown[0]:
        if drawFlag:
            pg.draw.line(canvas, PEN_COLOR, prev_pos, (mx, my), PEN_WIDTH)
        else:
            pg.draw.circle(canvas, PEN_COLOR, (mx, my), PEN_WIDTH // 2)
        prev_pos = (mx, my)
        drawFlag = True
    else:
        drawFlag = False

    if key[pg.K_c]:
        canvas.fill(pg.Color("WHITE"))

    screen.fill(pg.Color("WHITE"))
    screen.blit(canvas, (0, 0))

    pg.display.update()
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
