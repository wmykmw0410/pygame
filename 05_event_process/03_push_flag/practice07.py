"""
練習7: マウスでボタンを押したか調べるプログラム(フラグ)
03_push_flag/ex07.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(フラグ pushFlag を用意する → 押した瞬間だけ1回表示する → ボタンを離したらフラグを戻す)

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  1. ボタンの上でボタンを押し続ける → 表示は何回?
  2. 一度離して、もう一度押す → どうなる?
  3. pushFlag = True の行を消す → どうなる?
  4. else: と pushFlag = False の2行を消す → 離してもう一度押すとどうなる?
  5. ボタンの外で押したまま、マウスをボタンの上に動かす → どうなる?
"""
# ゲームの準備
import pygame as pg
import sys

pg.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("練習7: マウスでボタンを押したか調べる(フラグ)")
clock = pg.time.Clock()
next_img = pg.image.load("05_event_process/images/nextbtn.png")
# ★ 押したかどうかを覚えるフラグ pushFlag を False にしておく


# ループ
while True:

    # 画面の初期化
    screen.fill(pg.Color("WHITE"))
    btn = screen.blit(next_img, (350, 200))

    # ユーザーからの入力を調べる
    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()

    # 絵を描いたり、判定したりする
    # ★ 左ボタンが押されている間: マウスの点がボタンの範囲に入っていて、まだ pushFlag が False なら
    #     「押した」と表示して、pushFlag を True にする
    # ★ 左ボタンが押されていないとき: pushFlag を False に戻す

    # 画面を表示する
    pg.display.update()
    clock.tick(FPS)

    # 閉じるボタンが押されたら終了
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
