"""UFOを降らせる"""
from pathlib import Path
import pygame as pg
import sys
import random

pg.init()
BASE_DIR  = Path(__file__).resolve().parent.parent
IMG_DIR   = BASE_DIR / "images"
SOUND_DIR = BASE_DIR / "sounds"

WIDTH, HEIGHT = 800, 600

FPS = 60

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("シューティングゲーム")
clock = pg.time.Clock()

# データ
## 自機データ
SHIP_SIZE = 50
myimg = pg.image.load(IMG_DIR / "myship.png")
myimg = pg.transform.scale(myimg, (SHIP_SIZE, SHIP_SIZE))
myrect = pg.Rect(400, 500, SHIP_SIZE, SHIP_SIZE)

## 弾データ
BULLET_SIZE  = 16
BULLET_SPEED = 15
OFFSCREEN_Y  = -100
bulletimg = pg.image.load(IMG_DIR / "bullet.png")
bulletimg = pg.transform.scale(bulletimg, (BULLET_SIZE, BULLET_SIZE))
bulletrect = pg.Rect(400, OFFSCREEN_Y, BULLET_SIZE, BULLET_SIZE)

## UFOデータ
UFO_SIZE  = 50
UFO_COUNT = 10
UFO_SPEED = 10
ufoimg = pg.image.load(IMG_DIR / "UFO.png")
ufoimg = pg.transform.scale(ufoimg, (UFO_SIZE, UFO_SIZE))
ufos = []
for i in range(UFO_COUNT):
    ux = random.randint(0, WIDTH)
    uy = OFFSCREEN_Y * i
    ufos.append(pg.Rect(ux, uy, UFO_SIZE, UFO_SIZE))

## ゲームステージ
def gamestage():
    screen.fill(pg.Color("NAVY"))
    (mx, _) = pg.mouse.get_pos()
    mdown = pg.mouse.get_pressed()

    ## 自機の処理
    myrect.x = mx - SHIP_SIZE // 2
    screen.blit(myimg, myrect)

    ## 弾の処理
    if mdown[0] and bulletrect.y < 0:
        bulletrect.x = myrect.x + SHIP_SIZE // 2 - BULLET_SIZE // 2
        bulletrect.y = myrect.y
        pg.mixer.Sound(SOUND_DIR / "pi.wav").play()
    if bulletrect.y >= 0:
        bulletrect.y -= BULLET_SPEED
        screen.blit(bulletimg, bulletrect)

    ## UFOの処理
    for ufo in ufos:
        ufo.y += UFO_SPEED
        screen.blit(ufoimg, ufo)
        if ufo.y > HEIGHT:
            ufo.x = random.randint(0, WIDTH)
            ufo.y = OFFSCREEN_Y

# ループ
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    gamestage()
    pg.display.update()
    clock.tick(FPS)
