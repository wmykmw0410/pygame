"""
青色でhello!と表示する
"""
# 1.ゲームの準備をする
import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("青色でhello!と表示する")
clock = pg.time.Clock()
font = pg.font.Font(None, 50)
textImg = font.render("hello!", True, pg.Color("BLUE"))

# 2.この下をずっとループする
while True:
    # 3.画像を初期化する
    screen.fill(pg.Color("WHITE"))
    # 5.絵を描いたり、判定したりする
    screen.blit(textImg, (200,100))
    # 6.画像を表示する
    pg.display.update()
    clock.tick(60)
    # 7.閉じすボタンを押したら終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()