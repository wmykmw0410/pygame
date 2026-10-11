"""
四角形が横に移動する
"""
# ゲームの準備をする
import pygame as pg
import sys

pg.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("四角形が横に移動する")
clock = pg.time.Clock()
myrect = pg.Rect(100,100,100,150)

# この下をずっとループする
while True:
    # 画面を初期化する
    screen.fill(pg.Color("WHITE"))
    # 絵を描いたり、判定したりする
    myrect.x += 1
    pg.draw.rect(screen, pg.Color("RED"), myrect)
    
    # 画面を表示する
    pg.display.update()
    clock.tick(FPS)
    # 閉じるボタンを押されたら終了
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            