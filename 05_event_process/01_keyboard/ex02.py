"""左右でキャラクタが動くプログラム"""
# ゲームの準備
import pygame as pg
import sys

pg.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("左右でキャラクタが動く")
clock = pg.time.Clock()
MOVE_SPEED = 5

imageR = pg.image.load("05_event_process/images/playerR.png")
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
        vx = MOVE_SPEED
    if key[pg.K_LEFT]:
        vx = -MOVE_SPEED
    myrect.x += vx
    screen.blit(imageR, myrect)

    # 画面を表示する
    pg.display.update()
    clock.tick(FPS)

    # 閉じるボタンを押したら終了
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
