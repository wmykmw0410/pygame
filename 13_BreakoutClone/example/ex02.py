"""ボールが画面の下に移動したらゲームオーバー"""
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

## ボタンデータ
REPLAY_BTN_POS   = (320, 480)
RESULT_FONT_SIZE = 150
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
    if ballrect.y > HEIGHT:
        page = 2
        pg.mixer.Sound(SND_DIR / "down.wav").play()
    ballrect.x += vx
    ballrect.y += vy
    screen.blit(ballimg, ballrect)

## データのリセット
def gamereset():
    global vx, vy
    vx = random.randint(*INITIAL_VX_RANGE)
    vy = INITIAL_VY
    ballrect.x = 400
    ballrect.y = 450

## ゲームオーバー
def gameover():
    gamereset()
    screen.fill(pg.Color("NAVY"))
    font = pg.font.Font(None, RESULT_FONT_SIZE)
    text = font.render("GAMEOVER", True, pg.Color("RED"))
    screen.blit(text, (100, 200))
    btn1 = screen.blit(replay_img, REPLAY_BTN_POS)
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
    clock.tick(FPS)
