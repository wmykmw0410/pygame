"""
車の画像が横に移動する
大きさ:(50,50)
"""
# ゲームの準備をする
import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("車の画像が横に移動する")
clock = pg.time.Clock()
img1 = pg.image.load("../images/car.png")
img1 = pg.transform.scale(img1, (50, 50))
myrect = img1.get_rect(topleft=(100, 100))

# この下をずっとループする
while True:
    # 画面を初期化する
    screen.fill(pg.Color("WHITE"))
    # 絵を描いたり、判定したりする
    myrect.x += 1
    screen.blit(img1, myrect)
    # 画面を表示する
    pg.display.update()
    clock.tick(60)
    # 閉じるボタンを押されたら終了
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
