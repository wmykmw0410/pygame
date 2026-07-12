"""ブロックをたくさん並べる"""
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

## ブロックデータ
blocks = []
for yy in range(4):
    for xx in range(7):
        blocks.append(pg.Rect(50 + xx * 100, 40 + yy * 50, 80, 30))

## メインループで使う変数
pushFlag = False
page = 1
score = 0

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
    global vx, vy, page, score
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
        pg.mixer.Sound(SND_DIR / "down.wav").play()
    ballrect.x += vx
    ballrect.y += vy
    screen.blit(ballimg, ballrect)

    ## ブロックの処理
    for n, block in enumerate(blocks):
        pg.draw.rect(screen, pg.Color("GOLD"), block)
        if block.colliderect(ballrect):
            pg.mixer.Sound(SND_DIR / "piko.wav").play()
            vy = -vy
            blocks[n] = pg.Rect(0, 0, 0, 0)
            score += 1
            if score == 28:
                pg.mixer.Sound(SND_DIR / "up.wav").play()
                page = 3

## データのリセット
def gamereset():
    global vx, vy, score, blocks
    vx = random.randint(-10, 10)
    vy = -5
    ballrect.x = 400
    ballrect.y = 450
    score = 0
    blocks = []
    for yy in range(4):
        for xx in range(7):
            blocks.append(pg.Rect(50 + xx * 100, 40 + yy * 50, 80, 30))

## ゲームオーバー
def gameover():
    gamereset()
    screen.fill(pg.Color("NAVY"))
    font = pg.font.Font(None, 150)
    text = font.render("GAMEOVER", True, pg.Color("RED"))
    screen.blit(text, (100, 200))
    btn1 = screen.blit(replay_img, (320, 480))
    button_to_jump(btn1, 1)

## ゲームクリア
def gameclear():
    gamereset()
    screen.fill(pg.Color("GOLD"))
    font = pg.font.Font(None, 150)
    text = font.render("GAMECLEAR", True, pg.Color("RED"))
    screen.blit(text, (60, 200))
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
    elif page == 3:
        gameclear()

    pg.display.update()
    clock.tick(60)
