"""
練習1: どのキーが押されているか画面に出力する
01_keyboard/ex01.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(押されているキーを調べる → 右キー・左キーが押されていたら、それぞれ表示する)

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  1. 右キーを押し続ける → 表示はどうなる?(1回だけ? 続けて?)
  2. 右キーと左キーを同時に押す → どうなる?
  3. pg.K_RIGHT を pg.K_UP や pg.K_SPACE に変える → 反応するキーはどう変わる?
  4. 上キー・下キー用の if を2つ足して、それぞれ "UP" "DOWN" を表示する
"""
# ゲームを準備する
import pygame as pg
import sys

pg.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("練習1: どのキーが押されているか出力する")
clock = pg.time.Clock()

# ループ
while True:

    # 画面を初期化する
    screen.fill(pg.Color("WHITE"))

    # ユーザからの入力を調べる
    # ★ 押されているキーを調べて key に代入する

    # ★ 右キーが押されていたら "RIGHT" と表示する

    # ★ 左キーが押されていたら "LEFT" と表示する

    # 画面を表示する
    pg.display.update()
    clock.tick(FPS)

    # 閉じるボタンを押したら終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
