"""
練習3: 車の画像が横に移動する(大きさ:(50,50))
example/ex03.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(画像を読み込む → サイズ変更 → Rectを取得 → Rectを動かして描画する)

動いたら、数字を書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  1. myrect.x += 1 の 1 を 5 や -1 に変える → 動く速さと向きは?
  2. その下に myrect.y += 1 を足す → どの向きに動く?
  3. topleft=(100, 100) を (0, 400) に変える → 動き始める位置は?
  4. topleft=(100, 100) を center=(400, 300) に変える → 画像はどこから動き始める?
  5. FPS = 60 を 10 に変える → 動きはどう見える?
"""
# ゲームの準備をする
import pygame as pg
import sys

pg.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("練習3: 車の画像が横に移動する")
clock = pg.time.Clock()
# ★ 画像を読み込んで img1 に代入する

# ★ img1 のサイズを (50, 50) に変更して img1 に入れ直す

# ★ img1.get_rect() で topleft=(100, 100) の Rect を取得して myrect に代入する


# この下をずっとループする
while True:
    # 画面を初期化する
    screen.fill(pg.Color("WHITE"))
    # 絵を描いたり、判定したりする
    # ★ myrect.x を 1 ずつ増やす

    # ★ img1 を myrect の位置に描画する

    # 画面を表示する
    pg.display.update()
    clock.tick(FPS)
    # 閉じるボタンを押されたら終了
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
