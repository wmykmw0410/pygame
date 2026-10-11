"""マウスを押して位置を表示するプログラム"""
# ゲームの準備
import pygame as pg
import sys

pg.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("マウスを押した場所に四角を描く")
clock = pg.time.Clock()
RECT_SIZE = 100

# ループ
while True:

    # 画面の初期化
    screen.fill(pg.Color("WHITE"))

    # ユーザからの入力を調べる
    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()

    # 絵を描いたり、判定する
    # 左ボタンが押されたら、マウスの座標を表示する
    if mdown[0]:
        pg.draw.rect(screen, pg.Color("RED"), (mx - RECT_SIZE // 2, my - RECT_SIZE // 2, RECT_SIZE, RECT_SIZE))

    # 画面を表示する
    pg.display.update()
    clock.tick(FPS)

    # 閉じるボタンが押されたら、終了
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
