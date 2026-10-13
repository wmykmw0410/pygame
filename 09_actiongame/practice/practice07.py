"""
練習7: 追いかけてくるオバケ
example/ex07.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(毎フレーム、プレイヤーの方向に ENEMY_SPEED ずつ近づく → 向きに合わせた画像を描画する → 触れたらゲームオーバー)
リポジトリのルートで実行する(python 09_actiongame/practice/practice07.py)

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  実行する前に、結果を予想してみよう
  1. オバケはどの方向に近づいてくる? プレイヤーが動かないと、オバケはどうなる?
  2. ENEMY_SPEED の 1 を 3 や 5 に変える → オバケの速さは? プレイヤー(PLAYER_SPEED = 4)より速いと?
  3. オバケがプレイヤーと同じ高さになったとき、オバケの動きをよく見る → どうなっている?
  4. 縦方向の追いかけ(ovy を決める if〜else)を、ovy = 0 に書き換える → オバケの動きは?
  5. オバケに触れる → 画面はどうなる?(音も聞く)
  6. gamereset() の中の enemyrect.x = 650、enemyrect.y = 200 の2行を消す → リプレイしたとき、オバケはどこにいる?
"""
from pathlib import Path
import pygame as pg
import sys
import random

pg.init()
BASE_DIR = Path(__file__).resolve().parent.parent
IMG_DIR = BASE_DIR / "images"
SND_DIR = BASE_DIR / "sounds"
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("練習7: アクションゲーム")
clock = pg.time.Clock()

## プレイヤーデータ
PLAYER_SIZE  = (40, 50)
PLAYER_SPEED = 4
myimgR = pg.image.load(IMG_DIR / "playerR.png")
myimgR = pg.transform.scale(myimgR, PLAYER_SIZE)
myimgL = pg.transform.flip(myimgR, True, False)
myrect = myimgR.get_rect(topleft=(50, 200))

## 壁データ
WALL_THICKNESS = 20
walls = [pg.Rect(0, 0, WIDTH, WALL_THICKNESS),
         pg.Rect(0, 0, WALL_THICKNESS, HEIGHT),
         pg.Rect(WIDTH - WALL_THICKNESS, 0, WALL_THICKNESS, HEIGHT),
         pg.Rect(0, HEIGHT - WALL_THICKNESS, WIDTH, WALL_THICKNESS)]

## 罠データ
TRAP_COUNT   = 20
TRAP_SPACING = 30
TRAP_SIZE    = (30, 30)
TRAP_START_X = 150
TRAP_Y_MIN   = 20
TRAP_Y_MAX   = 550
trapimg = pg.image.load(IMG_DIR / "uni.png")
trapimg = pg.transform.scale(trapimg, TRAP_SIZE)
traps = []
for i in range(TRAP_COUNT):
    wx = TRAP_START_X + i * TRAP_SPACING
    wy = random.randint(TRAP_Y_MIN, TRAP_Y_MAX)
    traps.append(pg.Rect(wx, wy, *TRAP_SIZE))

## ボタンデータ
REPLAY_BTN_POS   = (320, 480)
RESULT_FONT_SIZE = 150
replay_img = pg.image.load(IMG_DIR / "replaybtn.png")
goalrect = pg.Rect(750, 250, 30, 100)

## オバケデータ
ENEMY_SIZE  = (50, 50)
ENEMY_SPEED = 1
# ★ obake.png を読み込み、ENEMY_SIZE に縮小して enemyimgR に代入する
# ★ enemyimgR を左右反転した画像を enemyimgL に代入する
# ★ enemyimgR の Rect を、左上が (650, 200) になるように取得して enemyrect に代入する

## メインループで使う変数
rightFlag = True
pushFlag = False
page = 1

## btnを押したら、newpageにジャンプする
def button_to_jump(btn, newpage):
    global page, pushFlag
    # ユーザーからの入力を調べる
    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()
    if mdown[0]:
        if btn.collidepoint(mx, my) and not pushFlag:
            pg.mixer.Sound(SND_DIR / "pi.wav").play()
            page = newpage
            pushFlag = True
    else:
        pushFlag = False

# ゲームステージ
def gamestage():
    global rightFlag, page

    # 画面を初期化する
    screen.fill(pg.Color("DEEPSKYBLUE"))
    vx = 0
    vy = 0

    # ユーザーからの入力
    key = pg.key.get_pressed()

    # 描画や判定
    if key[pg.K_RIGHT]:
        vx = PLAYER_SPEED
        rightFlag = True
    if key[pg.K_LEFT]:
        vx = -PLAYER_SPEED
        rightFlag = False
    if key[pg.K_UP]:
        vy = -PLAYER_SPEED
    if key[pg.K_DOWN]:
        vy = PLAYER_SPEED

    ## プレイヤーの処理
    myrect.x += vx
    myrect.y += vy
    if myrect.collidelist(walls) != -1:
        myrect.x -= vx
        myrect.y -= vy

    if rightFlag:
        screen.blit(myimgR, myrect)
    else:
        screen.blit(myimgL, myrect)

    ## 壁の処理
    for wall in walls:
        pg.draw.rect(screen, pg.Color("DARKGREEN"), wall)

    ## 罠の処理
    for trap in traps:
        screen.blit(trapimg, trap)
    if myrect.collidelist(traps) != -1:  # 罠に触れたらゲームオーバー
        pg.mixer.Sound(SND_DIR / "pi.wav").play()
        page = 2

    ## ゴールの処理
    pg.draw.rect(screen, pg.Color("GOLD"), goalrect)
    if myrect.colliderect(goalrect):  # ゴールに触れたらゲームクリア
        pg.mixer.Sound(SND_DIR / "up.wav").play()
        page = 3

    ## オバケの処理
    # ★ オバケがプレイヤーより左なら ovx を ENEMY_SPEED に、そうでなければ -ENEMY_SPEED にする
    # ★ オバケがプレイヤーより上なら ovy を ENEMY_SPEED に、そうでなければ -ENEMY_SPEED にする
    # ★ enemyrect の x に ovx、y に ovy を足して動かす
    # ★ ovx が正(右向き)なら enemyimgR を、そうでなければ enemyimgL を enemyrect の位置に描画する
    # ★ myrect が enemyrect と衝突したら、down.wav の音を鳴らして、page を 2 にする

## データのリセット
def gamereset():
    myrect.x = 50
    myrect.y = 100
    for d in range(TRAP_COUNT):
        traps[d].x = TRAP_START_X + d * TRAP_SPACING
        traps[d].y = random.randint(TRAP_Y_MIN, TRAP_Y_MAX)
    # ★ オバケも最初の位置 (650, 200) に戻す

## ゲームオーバー
def gameover():
    gamereset()
    screen.fill(pg.Color("NAVY"))
    font = pg.font.Font(None, RESULT_FONT_SIZE)
    text = font.render("GAMEOVER", True, pg.Color("RED"))
    screen.blit(text, (100, 200))
    btn1 = screen.blit(replay_img, REPLAY_BTN_POS)
    # 描画や判定
    button_to_jump(btn1, 1)

## ゲームクリア
def gameclear():
    gamereset()
    screen.fill(pg.Color("GOLD"))
    font = pg.font.Font(None, RESULT_FONT_SIZE)
    text = font.render("GAMECLEAR", True, pg.Color("RED"))
    screen.blit(text, (60, 200))
    btn1 = screen.blit(replay_img, REPLAY_BTN_POS)
    # 描画や判定
    button_to_jump(btn1, 1)

# ループ
while True:
    if page == 1:
        gamestage()
    elif page == 2:
        gameover()
    elif page == 3:
        gameclear()
    # 画面を表示する
    pg.display.update()
    clock.tick(FPS)

    # 終了
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
