"""
練習2: 左右でキャラクタが動くプログラム
01_keyboard/ex02.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(画像を読み込む → Rectを取得する → キーで vx を決める → Rectを動かして描画する)

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  1. MOVE_SPEED の 5 を 1 や 20 に変える → 動く速さは?
  2. vx = MOVE_SPEED と vx = -MOVE_SPEED を入れ替える → 動く向きは?
  3. vx = 0 の行を、ループの外(MOVE_SPEED の下)に移動する → キーを離すとどうなる?
  4. キーを押し続けて画面の右端まで進む → 画面の外に出ると?
  5. topleft=(300, 200) を (0, 400) に変える → 動き始める位置は?
  6. 上キー・下キーでも動くように、vy と myrect.y を使って足す
"""
# ゲームの準備
import pygame as pg
import sys

pg.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("練習2: 左右でキャラクタが動く")
clock = pg.time.Clock()
MOVE_SPEED = 5

# ★ 05_event_process/images/playerR.png を読み込んで imageR に代入する

# ★ imageR の Rect を、左上が (300, 200) になるように取得して myrect に代入する


# ループ
while True:

    # 画面を初期化する
    screen.fill(pg.Color("WHITE"))
    # ★ 移動量 vx を 0 にする

    # ユーザ入力
    # ★ 押されているキーを調べて key に代入する

    # 絵を描いたり、判定したりする
    # ★ 右キーなら vx を MOVE_SPEED にする

    # ★ 左キーなら vx を -MOVE_SPEED にする

    # ★ myrect.x に vx を足す

    # ★ imageR を myrect の位置に描画する

    # 画面を表示する
    pg.display.update()
    clock.tick(FPS)

    # 閉じるボタンを押したら終了
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
