# ex02: Ball クラスにまとめる
# → ボールのデータ（rect・vx・vy）と処理（移動・跳ね返り・描画）を1つのクラスに集約する
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


# ── ex01 との違い: ボールのデータと処理を Ball クラスにまとめた ──
BALL_SIZE = 30
INITIAL_VX_RANGE = (-10, 10)
INITIAL_VY = -5
BOUNCE_VY_RANGE = (-10, -5)
BAR_SIZE = (100, 20)


class Ball():
    def __init__(self, img):
        self.img  = img
        self.rect = pg.Rect(400, 450, BALL_SIZE, BALL_SIZE)
        self.vx   = random.randint(*INITIAL_VX_RANGE)
        self.vy   = INITIAL_VY

    def bounce_wall(self):
        if self.rect.y < 0:
            self.vy = -self.vy
        if self.rect.x < 0 or self.rect.x > WIDTH - BALL_SIZE:
            self.vx = -self.vx

    def bounce_bar(self, barrect):
        if barrect.colliderect(self.rect):
            self.vx = int(((self.rect.x + BALL_SIZE // 2) - (barrect.x + BAR_SIZE[0] // 2)) / 4)
            self.vy = random.randint(*BOUNCE_VY_RANGE)
            pg.mixer.Sound(SND_DIR / "pi.wav").play()

    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

    def draw(self):
        screen.blit(self.img, self.rect)

    def is_out(self):
        return self.rect.y > HEIGHT

    def reset(self):
        self.rect.x = 400
        self.rect.y = 450
        self.vx = random.randint(*INITIAL_VX_RANGE)
        self.vy = INITIAL_VY


ballimg = pg.image.load(IMG_DIR / "kaeru.png")
ballimg = pg.transform.scale(ballimg, (BALL_SIZE, BALL_SIZE))
ball    = Ball(ballimg)

barrect    = pg.Rect(400, 500, *BAR_SIZE)
REPLAY_BTN_POS   = (320, 480)
RESULT_FONT_SIZE = 150
replay_img = pg.image.load(IMG_DIR / "replaybtn.png")

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

pushFlag = False
page     = 1
score    = 0


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


def gamestage():
    global page, score
    screen.fill(pg.Color("NAVY"))
    (mx, my) = pg.mouse.get_pos()

    barrect.x = mx - BAR_SIZE[0] // 2
    pg.draw.rect(screen, pg.Color("CYAN"), barrect)

    ball.bounce_wall()
    ball.bounce_bar(barrect)
    if ball.is_out():
        page = 2
        pg.mixer.Sound(SND_DIR / "pi.wav").play()
    ball.move()
    ball.draw()

    for n, block in enumerate(blocks):
        pg.draw.rect(screen, pg.Color("GOLD"), block)
        if block.colliderect(ball.rect):
            pg.mixer.Sound(SND_DIR / "piko.wav").play()
            ball.vy = -ball.vy
            blocks[n] = pg.Rect(0, 0, 0, 0)
            score += 1
            if score == BLOCK_ROWS * BLOCK_COLS:
                pg.mixer.Sound(SND_DIR / "up.wav").play()
                page = 3


def gamereset():
    global score, blocks
    ball.reset()
    score  = 0
    blocks = []
    for yy in range(BLOCK_ROWS):
        for xx in range(BLOCK_COLS):
            blocks.append(pg.Rect(BLOCK_START[0] + xx * BLOCK_SPACING[0],
                                   BLOCK_START[1] + yy * BLOCK_SPACING[1], *BLOCK_SIZE))


def gameover():
    gamereset()
    screen.fill(pg.Color("NAVY"))
    font = pg.font.Font(None, RESULT_FONT_SIZE)
    text = font.render("GAMEOVER", True, pg.Color("RED"))
    screen.blit(text, (100, 200))
    btn1 = screen.blit(replay_img, REPLAY_BTN_POS)
    button_to_jump(btn1, 1)


def gameclear():
    gamereset()
    screen.fill(pg.Color("GOLD"))
    font = pg.font.Font(None, RESULT_FONT_SIZE)
    text = font.render("GAMECLEAR", True, pg.Color("RED"))
    screen.blit(text, (60, 200))
    btn1 = screen.blit(replay_img, REPLAY_BTN_POS)
    button_to_jump(btn1, 1)


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
