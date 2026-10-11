"""ブロックをたくさん並べる"""
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

## ブロックデータ
BLOCK_ROWS    = 4
BLOCK_COLS    = 7
BLOCK_START   = (50, 40)
BLOCK_SPACING = (100, 50)
BLOCK_SIZE    = (80, 30)
blocks = []
for yy in range(BLOCK_ROWS):
    for xx in range(BLOCK_COLS):
        blocks.append(pg.Rect(BLOCK_START[0] + xx * BLOCK_SPACING[0],
                               BLOCK_START[1] + yy * BLOCK_SPACING[1], *BLOCK_SIZE))

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

    ## ブロックの処理
    for n, block in enumerate(blocks):
        pg.draw.rect(screen, pg.Color("GOLD"), block)
        if block.colliderect(ballrect):
            pg.mixer.Sound(SND_DIR / "piko.wav").play()
            vy = -vy
            blocks[n] = pg.Rect(0, 0, 0, 0)
            score += 1
            if score == BLOCK_ROWS * BLOCK_COLS:
                pg.mixer.Sound(SND_DIR / "up.wav").play()
                page = 3

## データのリセット
def gamereset():
    global vx, vy, score, blocks
    vx = random.randint(*INITIAL_VX_RANGE)
    vy = INITIAL_VY
    ballrect.x = 400
    ballrect.y = 450
    score = 0
    blocks = []
    for yy in range(BLOCK_ROWS):
        for xx in range(BLOCK_COLS):
            blocks.append(pg.Rect(BLOCK_START[0] + xx * BLOCK_SPACING[0],
                                   BLOCK_START[1] + yy * BLOCK_SPACING[1], *BLOCK_SIZE))

## ゲームオーバー
def gameover():
    gamereset()
    screen.fill(pg.Color("NAVY"))
    font = pg.font.Font(None, RESULT_FONT_SIZE)
    text = font.render("GAMEOVER", True, pg.Color("RED"))
    screen.blit(text, (100, 200))
    btn1 = screen.blit(replay_img, REPLAY_BTN_POS)
    button_to_jump(btn1, 1)

## ゲームクリア
def gameclear():
    gamereset()
    screen.fill(pg.Color("GOLD"))
    font = pg.font.Font(None, RESULT_FONT_SIZE)
    text = font.render("GAMECLEAR", True, pg.Color("RED"))
    screen.blit(text, (60, 200))
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
    elif page == 3:
        gameclear()

    pg.display.update()
    clock.tick(FPS)
