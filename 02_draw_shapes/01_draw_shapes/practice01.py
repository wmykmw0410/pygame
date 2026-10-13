"""
練習1: 四角・線・円を描く
01_draw_shapes/ex01.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(赤い四角、青い線、緑の円を描く)

動いたら、数字を書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  1. 四角の (100, 100, 100, 150) を (300, 200, 100, 150) や (100, 100, 200, 50) に変える
  2. 線の太さ 5 を 1 や 20 に変える
  3. 円の (400, 100, 150, 150) を (400, 100, 200, 100) に変える → 円はどうなる?
  4. 円の太さ 5 を 0 や 20 に変える
  5. 四角の最後に太さ(例: 5)を足す → どうなる?
  6. pg.Color("RED") を pg.Color(0, 255, 0) や pg.Color("YELLOW") に変える
  7. 円を四角と重なる位置にずらし、2行の順番を入れ替える → どちらが上に重なる?

自分で調べてみよう
  8. pygame のドキュメント(日本語訳) https://westplain.sakura.ne.jp/translate/pygame/ で pg.draw の他の関数
     (circle, polygon, arc, lines など)の使い方を調べて、「# ★ 自分で調べて図形を追加する」の下に
     図形を1つ以上追加する。引数の数字も変えて、どう変わるか確認しよう
"""
# ゲームの準備をする
import pygame as pg
import sys

pg.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("練習1: 四角を描くプログラム")
clock = pg.time.Clock()

# この下をずっとループする
while True:
    # 画面の初期化する
    screen.fill(pg.Color("WHITE"))
    # 絵を描いたり、判定したりする
    # ★ 赤い四角を (100, 100) に、幅100・高さ150で描く

    # ★ 青い線を (250, 100) から (350, 250) まで、太さ5で引く

    # ★ 緑の円を (400, 100) に、幅150・高さ150で、太さ5で描く

    # ★ 自分で調べて図形を追加する

    # 画面を表示する
    pg.display.update()
    clock.tick(FPS)
    # 閉じるボタンが押されたら終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
