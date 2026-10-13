"""
練習6: マウスでボタンを押したか調べるプログラム
03_push_flag/ex06.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(ボタン画像を描いて範囲(Rect)を受け取る → 左ボタンが押されていて、マウスの点がボタンの範囲に入っていたら表示する)

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  1. ボタンの外をクリックする → 表示される?
  2. ボタンの上でボタンを押し続ける → 表示はどうなる?
  3. screen.blit(next_img, (350, 200)) の (350, 200) を (100, 400) に変える → 反応する場所はどこ?
  4. print("押した") の文字を変える
"""
# ゲームの準備
import pygame as pg
import sys

pg.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("練習6: マウスでボタンを押したか調べる")
clock = pg.time.Clock()
next_img = pg.image.load("05_event_process/images/nextbtn.png")

# ループ
while True:

    # 画面の初期化
    screen.fill(pg.Color("WHITE"))
    # ★ next_img を (350, 200) に描画して、その範囲を btn に代入する

    # ユーザーからの入力を調べる
    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()

    # 絵を描いたり、判定したりする
    # ★ 左ボタンが押されていて、マウスの点(mx, my)が btn の範囲に入っていたら「押した」と表示する

    # 画面を表示する
    pg.display.update()
    clock.tick(FPS)

    # 閉じるボタンが押されたら終了
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
