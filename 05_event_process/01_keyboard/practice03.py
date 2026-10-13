"""
練習3: 左右でキャラクタが動く(向き反転)プログラム
01_keyboard/ex03.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(左向きの画像を作る → 向きを覚えるフラグを用意する → 向きに合わせて画像を切り替えて描画する)

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  1. pg.transform.flip(imageR, True, False) を (False, True) や (True, True) に変える → 画像はどうなる?
  2. rightFlag の最初の値 True を False に変える → 最初の向きは?
  3. 左キーのときの rightFlag = False の行を消す → 左キーを押すとどうなる?
  4. 右キー・左キーのどちらも押さなくなったら、向きはどうなる?
"""
# ゲームの準備
import pygame as pg
import sys

pg.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("練習3: 左右でキャラクタが動く(向き反転)")
clock = pg.time.Clock()
MOVE_SPEED = 5

imageR = pg.image.load("05_event_process/images/playerR.png")
# ★ imageR を左右反転した画像を作って imageL に代入する

myrect = imageR.get_rect(topleft=(300, 200))
# ★ 右向きかどうかを覚えるフラグ rightFlag を True にしておく


# ループ
while True:

    # 画面を初期化する
    screen.fill(pg.Color("WHITE"))
    vx = 0

    # ユーザ入力
    key = pg.key.get_pressed()

    # 絵を描いたり、判定したりする
    if key[pg.K_RIGHT]:
        vx = MOVE_SPEED
        # ★ rightFlag を True にする
    if key[pg.K_LEFT]:
        vx = -MOVE_SPEED
        # ★ rightFlag を False にする
    myrect.x += vx

    # ★ rightFlag が True なら imageR を、そうでなければ imageL を myrect の位置に描画する

    # 画面を表示する
    pg.display.update()
    clock.tick(FPS)

    # 閉じるボタンを押したら終了
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
