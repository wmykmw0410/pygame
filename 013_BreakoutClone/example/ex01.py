"""ボールをバーで打ち返す"""
from pathlib import Path
import pygame as pg
import sys
import random

pg.init()
BASE_DIR = Path(__file__).resolve().parent.parent
IMG_DIR  = BASE_DIR / "images"
SND_DIR  = BASE_DIR / "sounds"

screen = pg.display.set_mode((800, 600))
pg.display.set_caption("BreakoutClone")
clock = pg.time.Clock()

# データ
## バーデータ
barrect = pg.Rect(400, 500, 100, 20)

## ボールデータ
ballimg = pg.image.load(IMG_DIR / "kaeru.png")
ballimg = pg.transform.scale(ballimg, (30, 30))
ballrect = pg.Rect(400, 450, 30, 30)
vx = random.randint(-10, 10)
vy = -5

## ゲームステージ
def gamestage():
    global vx, vy
    screen.fill(pg.Color("NAVY"))

    (mx, my) = pg.mouse.get_pos()

    ## バーの処理
    barrect.x = mx - 50
    pg.draw.rect(screen, pg.Color("CYAN"), barrect)

    ## ボールの処理
    if ballrect.y < 0:
        vy = -vy
    if ballrect.x < 0 or ballrect.x > 800 - 30:
        vx = -vx
    if barrect.colliderect(ballrect):
        vx = int(((ballrect.x + 15) - (barrect.x + 50)) / 4)
        vy = random.randint(-10, -5)
        pg.mixer.Sound(SND_DIR / "pi.wav").play()
    ballrect.x += vx
    ballrect.y += vy
    screen.blit(ballimg, ballrect)

# ループ
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    gamestage()
    pg.display.update()
    clock.tick(60)
