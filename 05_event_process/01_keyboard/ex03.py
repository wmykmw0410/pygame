"""左右でキャラクタが動くプログラム"""
# ゲームの準備
import pygame as pg
import sys

pg.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("左右でキャラクタが動く(向き反転)")
clock = pg.time.Clock()
MOVE_SPEED = 5

imageR = pg.image.load("05_event_process/images/playerR.png")
imageL = pg.transform.flip(imageR, True, False)
myrect = imageR.get_rect(topleft=(300, 200))
rightFlag = True

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
        rightFlag = True
    if key[pg.K_LEFT]:
        vx = -MOVE_SPEED
        rightFlag = False
    myrect.x += vx

    if rightFlag:
        screen.blit(imageR, myrect)
    else:
        screen.blit(imageL, myrect)

    # 画面を表示する
    pg.display.update()
    clock.tick(FPS)

    # 閉じるボタンを押したら終了
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
