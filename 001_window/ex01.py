"""四角を描くプログラム"""
# ゲームの準備をする
import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((800,600))
pg.display.set_caption("四角を描くプログラム")
clock = pg.time.Clock()

# この下をずっとループする
while True:
    # 画面の初期化する
    screen.fill(pg.Color("WHITE"))
    # 絵を描いたり、判定したりする
    pg.draw.rect(screen, pg.Color("RED"), (100, 100, 100, 150))
    # 画面を表示する
    pg.display.update()
    clock.tick(60)
    # 閉じるボタンが押されたら終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()