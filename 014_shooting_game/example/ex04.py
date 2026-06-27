"""弾でUFOを撃ち落とす"""
from pathlib import Path
import pygame as pg
import sys
import random

pg.init()
BASE_DIR  = Path(__file__).resolve().parent.parent
IMG_DIR   = BASE_DIR / "images"
SOUND_DIR = BASE_DIR / "sounds"

screen = pg.display.set_mode((800, 600))
pg.display.set_caption("シューティングゲーム")
clock = pg.time.Clock()

# データ
## 自機データ
myimg = pg.image.load(IMG_DIR / "myship.png")
myimg = pg.transform.scale(myimg, (50, 50))
myrect = pg.Rect(400, 500, 50, 50)

## 弾データ
bulletimg = pg.image.load(IMG_DIR / "bullet.png")
bulletimg = pg.transform.scale(bulletimg, (16, 16))
bulletrect = pg.Rect(400, -100, 16, 16)

## UFOデータ
ufoimg = pg.image.load(IMG_DIR / "UFO.png")
ufoimg = pg.transform.scale(ufoimg, (50, 50))
ufos = []
for i in range(10):
    ux = random.randint(0, 800)
    uy = -100 * i
    ufos.append(pg.Rect(ux, uy, 50, 50))

## ボタンデータ
replay_img = pg.image.load(IMG_DIR / "replaybtn.png")

## メインループで使う変数
pushFlag = False
page = 1

## btnを押したら、newpageにジャンプする
def button_to_jump(btn, newpage):
    global page, pushFlag
    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()
    if mdown[0]:
        if btn.collidepoint(mx, my) and not pushFlag:
            pg.mixer.Sound(SOUND_DIR / "pi.wav").play()
            page = newpage
            pushFlag = True
    else:
        pushFlag = False

## ゲームステージ
def gamestage():
    global page
    screen.fill(pg.Color("NAVY"))
    (mx, my) = pg.mouse.get_pos()
    mdown = pg.mouse.get_pressed()

    ## 自機の処理
    myrect.x = mx - 25
    screen.blit(myimg, myrect)

    ## 弾の処理
    if mdown[0] and bulletrect.y < 0:
        bulletrect.x = myrect.x + 25 - 8
        bulletrect.y = myrect.y
        pg.mixer.Sound(SOUND_DIR / "pi.wav").play()
    if bulletrect.y >= 0:
        bulletrect.y -= 15
        screen.blit(bulletimg, bulletrect)

    ## UFOの処理
    for ufo in ufos:
        ufo.y += 10
        screen.blit(ufoimg, ufo)
        if ufo.y > 600:
            ufo.x = random.randint(0, 800)
            ufo.y = -100
        ## 自機とUFOの衝突処理
        if ufo.colliderect(myrect):
            page = 2
            pg.mixer.Sound(SOUND_DIR / "down.wav").play()
        ## 弾とUFOの衝突処理
        if ufo.colliderect(bulletrect):
            ufo.y = -100
            ufo.x = random.randint(0, 800)
            bulletrect.y = -100
            pg.mixer.Sound(SOUND_DIR / "piko.wav").play()

## データのリセット
def gamereset():
    myrect.x = 400
    myrect.y = 500
    bulletrect.y = -100
    for i in range(10):
        ufos[i] = pg.Rect(random.randint(0, 800), -100 * i, 50, 50)

## ゲームオーバー
def gameover():
    gamereset()
    screen.fill(pg.Color("NAVY"))
    font = pg.font.Font(None, 150)
    text = font.render("GAMEOVER", True, pg.Color("RED"))
    screen.blit(text, (100, 200))
    btn1 = screen.blit(replay_img, (320, 480))
    button_to_jump(btn1, 1)

# ループ
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    if page == 1:
        gamestage()
    elif page == 2:
        gameover()

    pg.display.update()
    clock.tick(60)
