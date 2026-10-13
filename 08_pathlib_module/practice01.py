"""
練習1: pathlibモジュールの使用方法
pathlib_module.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(Path を読み込む → このファイルのあるフォルダ BASE_DIR を求める → 画像フォルダ IMG_DIR を作る → 画像を表示する)
(ウィンドウと同時に、ターミナルにもパスが表示される)

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  実行する前に、結果を予想してみよう
  1. print で表示される CURRENT_DIR は、相対パス? 絶対パス?
  2. BASE_DIR の .parent を .parent.parent に変えて、BASE_DIR を print する → どのフォルダになる? 画像は表示される?
  3. Path(__file__).resolve().parents[0] / parents[1] / parents[2] をそれぞれ print する → どのフォルダ?
  4. IMG_DIR / "car.png" を IMG_DIR / "nothing.png" に変える → どうなる?
  5. ターミナルで 08_pathlib_module フォルダへ cd してから、python practice01.py で実行する → 画像は表示される?
"""
# ★ pathlib から Path を読み込む
import pygame as pg
import sys

pg.init()

# ★ このファイル自身のパス CURRENT_DIR を Path(__file__) で作る
# ★ このファイルが入っているフォルダ BASE_DIR を、Path(__file__).resolve().parent で求める

# ★ BASE_DIR の中の images フォルダ IMG_DIR を、/ 演算子で作る

# ★ CURRENT_DIR と BASE_DIR を print で表示する

WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("練習1: Image Display Sample")
clock = pg.time.Clock()

# ★ IMG_DIR / "car.png" の画像を読み込んで player_img に代入する
# ★ player_img の Rect を、左上が (WIDTH // 2, HEIGHT // 2) になるように取得して player_rect に代入する

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill("WHITE")
    # ★ player_img を player_rect の位置に描画する
    pg.display.update()
    clock.tick(FPS)
