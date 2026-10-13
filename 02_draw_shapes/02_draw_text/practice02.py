"""
練習2: 青色でhello!と表示する
02_draw_text/ex02.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(フォントを用意する → 文字列の画像を作る → 描画する)

動いたら、数字や文字を書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  1. 文字サイズ 50 を 100 や 20 に変える
  2. "hello!" を "good morning" に変える → 文字数が増えると?
  3. "hello!" を "こんにちは" に変える → どう表示される?
  4. 色 pg.Color("BLUE") を pg.Color("RED") や pg.Color(0, 128, 0) に変える
  5. 描画する位置 (200, 100) を (400, 300) や (0, 0) に変える
  6. render の True を False に変える → 文字の輪郭はどう見える?(100 などの大きいサイズで見比べる)
"""
# 1.ゲームの準備をする
import pygame as pg
import sys

pg.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("練習2: 青色でhello!と表示する")
clock = pg.time.Clock()
# ★ 文字サイズ50のフォント(デフォルト)を用意して font に代入する

# ★ font で "hello!" の画像を青色で作って textImg に代入する


# 2.この下をずっとループする
while True:
    # 3.画像を初期化する
    screen.fill(pg.Color("WHITE"))
    # 5.絵を描いたり、判定したりする
    # ★ textImg を (200, 100) に描画する

    # 6.画像を表示する
    pg.display.update()
    clock.tick(FPS)
    # 7.閉じるボタンを押したら終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
