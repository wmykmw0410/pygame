"""ボールが画面の下に移動したらゲームオーバー"""
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
            pg.mixer.Sound(SND_DIR / "pi.wav").play()
            page = newpage
            pushFlag = True
    else:
        pushFlag = False

## ゲームステージ
def gamestage():
    global vx, vy, page
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
    if ballrect.y > 600:
        page = 2
        pg.mixer.Sound(SND_DIR / "pi.wav").play()
    ballrect.x += vx
    ballrect.y += vy
    screen.blit(ballimg, ballrect)

## データのリセット
def gamereset():
    global vx, vy
    vx = random.randint(-10, 10)
    vy = -5
    ballrect.x = 400
    ballrect.y = 450

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
