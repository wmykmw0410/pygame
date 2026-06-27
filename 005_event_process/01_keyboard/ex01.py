"""どのキーが押されているか画面に出力する"""
# ゲームを準備する
import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("どのキーが押されているか出力する")
clock = pg.time.Clock()

# ループ
while True:

    # 画面を初期化する
    screen.fill(pg.Color("WHITE"))

    # ユーザからの入力を調べる
    key = pg.key.get_pressed()
    if key[pg.K_RIGHT]:
        print("RIGHT")
    if key[pg.K_LEFT]:
        print("LEFT")

    # 画面を表示する
    pg.display.update()
    clock.tick(60)

    # 閉じるボタンを押したら終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
