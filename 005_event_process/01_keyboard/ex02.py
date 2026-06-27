"""左右でキャラクタが動くプログラム"""
# ゲームの準備
import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("左右でキャラクタが動く")
clock = pg.time.Clock()
imageR = pg.image.load("../images/playerR.png")
myrect = imageR.get_rect(topleft=(300, 200))

# ループ
while True:

    # 画面を初期化する
    screen.fill(pg.Color("WHITE"))
    vx = 0

    # ユーザ入力
    key = pg.key.get_pressed()

    # 絵を描いたり、判定したりする
    if key[pg.K_RIGHT]:
        vx = 5
    if key[pg.K_LEFT]:
        vx = -5
    myrect.x += vx
    screen.blit(imageR, myrect)

    # 画面を表示する
    pg.display.update()
    clock.tick(60)

    # 閉じるボタンを押したら終了
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
