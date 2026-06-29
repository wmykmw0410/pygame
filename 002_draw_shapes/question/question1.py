"""練習問題1: 四角を斜めに移動させて、その後拡大させる

・四角を画面に表示する
・3秒間、斜め方向に移動させる
・3秒後、移動を止めて四角を拡大させ続ける

ヒント:
・経過時間は pg.time.get_ticks() で取得できる（単位: ミリ秒）
・3秒 = 3000ミリ秒
・斜め移動は rect.x と rect.y を同時に変化させる
・拡大は rect.width と rect.height を増やす
・Rectの大きさを変えても基準点（左上）は変わらない
"""

import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("斜め移動して拡大")
clock = pg.time.Clock()

# 四角の初期位置と大きさを設定する

# 開始時刻を記録する

while True:
    screen.fill(pg.Color("WHITE"))

    # 経過時間を取得する

    # 3秒間は斜めに移動、3秒後は拡大する

    # 四角を描く

    pg.display.update()
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
