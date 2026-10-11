"""他のRectとの衝突判定"""
from pathlib import Path
import pygame as pg
import sys

pg.init()
BASE_DIR = Path(__file__).resolve().parent.parent
IMG_DIR = BASE_DIR / "images"
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("アクションゲーム")
clock = pg.time.Clock()

## プレイヤーデータ
PLAYER_SIZE  = (40, 50)
PLAYER_SPEED = 4
myimgR = pg.image.load(IMG_DIR / "playerR.png")
myimgR = pg.transform.scale(myimgR, PLAYER_SIZE)
myimgL = pg.transform.flip(myimgR, True, False)
myrect = myimgR.get_rect(topleft=(50, 200))

## 障害物データ
boxrect = pg.Rect(300, 200, 100, 100)

## メインループで使う変数
rightFlag = True

# ゲームステージ
def gamestage():
    global rightFlag

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
    if myrect.colliderect(boxrect):  # 障害物と衝突したら移動を戻す
        myrect.x -= vx
        myrect.y -= vy

    if rightFlag:
        screen.blit(myimgR, myrect)
    else:
        screen.blit(myimgL, myrect)

    ## 障害物の処理
    pg.draw.rect(screen, pg.Color("DARKGREEN"), boxrect)

# ループ
while True:
    gamestage()
    # 画面を表示する
    pg.display.update()
    clock.tick(FPS)

    # 終了
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
