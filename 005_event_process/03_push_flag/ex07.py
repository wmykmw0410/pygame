"""マウスでボタンを押したか調べるプログラム"""
# ゲームの準備
import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("マウスでボタンを押したか調べる(フラグ)")
clock = pg.time.Clock()
next_img = pg.image.load("../images/nextbtn.png")
pushFlag = False

# ループ
while True:

    # 画面の初期化
    screen.fill(pg.Color("WHITE"))
    btn = screen.blit(next_img, (350, 200))

    # ユーザーからの入力を調べる
    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()

    # 絵を描いたり、判定したりする
    # 左ボタンが押された時、マウスで押した点(mx,my)が
    # ボタンの絵の範囲"btn"に入っていたら「押した」と表示する
    # フラグを使って押した瞬間だけ1回だけ表示する
    if mdown[0]:
        if btn.collidepoint(mx, my) and not pushFlag:
            print("押した")
            pushFlag = True
    else:
        pushFlag = False

    # 画面を表示する
    pg.display.update()
    clock.tick(60)

    # 閉じるボタンが押されたら終了
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
