"""
イベント方式でキーとマウスの入力を検知するプログラム
スペースキーを押すと四角が表示され、マウス左クリックで消える
"""
import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("イベント方式の入力検知")
clock = pg.time.Clock()

show_rect = False

while True:
    screen.fill(pg.Color("WHITE"))

    # 絵を描いたり、判定したりする
    if show_rect:
        pg.draw.rect(screen, pg.Color("RED"), (300, 200, 200, 200))

    pg.display.update()
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        # キーを押した瞬間(1回だけ実行)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                show_rect = True
                print("スペース押した: 四角を表示")

        # マウス左ボタンを押した瞬間(1回だけ実行)
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                show_rect = False
                print("マウス押した: 四角を消す")
