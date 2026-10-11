"""マウスの座標をトレースして文字を書くプログラム

・左ボタンを押している間、マウスの動きに沿って線を描く
・ボタンを離すと描くのをやめる
・Cキーを押すと画面をまっさらにする

ヒント:
・毎フレーム塗りつぶす screen とは別に、「描いた跡を覚えておく専用のSurface（キャンバス）」を用意する
・pg.draw.line(キャンバス, 色, 始点, 終点, 太さ) で、キャンバスに線を描く
・「直前のフレームのマウス座標」を変数に覚えておき、「今のマウス座標」までを線でつなぐと、
  点を打つだけよりも滑らかな線になる
・「直前のフレームも描いていたかどうか」は、03_push_flagと同じ考え方でフラグ（True/False）で管理する
  ボタンを押した瞬間（フラグがFalse）は「直前の座標」がまだ無いので、線の代わりに pg.draw.circle() で点を打つ
・毎フレーム screen.blit(キャンバス, (0, 0)) でキャンバスの中身を画面に表示する
"""

import pygame as pg
import sys

pg.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("マウスで文字を書く")
clock = pg.time.Clock()

PEN_COLOR = pg.Color("BLACK")
PEN_WIDTH = 4

# キャンバス（描いた跡を覚えておく専用のSurface）を白で用意する

# 直前のマウス座標を覚えておく変数を用意する
# drawFlag: True なら直前のフレームも描いていた（線をつなぐ） / False なら今回が描き始め（点を打つ）
drawFlag = False

while True:
    # ユーザからの入力を調べる（マウスの状態・座標、キーの状態）

    # 左ボタンが押されていたら
    #   drawFlag が True なら、直前の座標から今の座標まで線を引く
    #   drawFlag が False なら（押した瞬間）、今の座標に点を打つ
    #   今の座標を「直前の座標」として覚えておき、drawFlag を True にする
    # 左ボタンが押されていなければ、drawFlag を False に戻す

    # Cキーが押されたら、キャンバスを白で塗りつぶして消す

    # キャンバスの中身を画面に表示する
    screen.fill(pg.Color("WHITE"))

    pg.display.update()
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
