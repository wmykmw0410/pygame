"""ボールをバーで打ち返す"""
from pathlib import Path
import pygame as pg
import sys
import random

pg.init()
BASE_DIR = Path(__file__).resolve().parent.parent
IMG_DIR  = BASE_DIR / "images"
SND_DIR  = BASE_DIR / "sounds"

WIDTH, HEIGHT = 800, 600

FPS = 60

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("BreakoutClone")
clock = pg.time.Clock()

# データ
## バーデータ
BAR_SIZE = (100, 20)
barrect = pg.Rect(400, 500, *BAR_SIZE)

## ボールデータ
BALL_SIZE = 30
INITIAL_VX_RANGE = (-10, 10)
INITIAL_VY = -5
BOUNCE_VY_RANGE = (-10, -5)
ballimg = pg.image.load(IMG_DIR / "kaeru.png")
ballimg = pg.transform.scale(ballimg, (BALL_SIZE, BALL_SIZE))
ballrect = pg.Rect(400, 450, BALL_SIZE, BALL_SIZE)
vx = random.randint(*INITIAL_VX_RANGE)
vy = INITIAL_VY

## ゲームステージ
def gamestage():
    global vx, vy
    screen.fill(pg.Color("NAVY"))

    (mx, my) = pg.mouse.get_pos()

    ## バーの処理
    barrect.x = mx - BAR_SIZE[0] // 2
    pg.draw.rect(screen, pg.Color("CYAN"), barrect)

    ## ボールの処理
    if ballrect.y < 0:
        vy = -vy
    if ballrect.x < 0 or ballrect.x > WIDTH - BALL_SIZE:
        vx = -vx
    if barrect.colliderect(ballrect):
        vx = int(((ballrect.x + BALL_SIZE // 2) - (barrect.x + BAR_SIZE[0] // 2)) / 4)
        vy = random.randint(*BOUNCE_VY_RANGE)
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
    clock.tick(FPS)
