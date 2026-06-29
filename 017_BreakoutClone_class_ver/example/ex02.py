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

screen = pg.display.set_mode((800, 600))
pg.display.set_caption("BreakoutClone")
clock = pg.time.Clock()


# ── ex01 との違い: ボールのデータと処理を Ball クラスにまとめた ──
class Ball():
    def __init__(self, img):
        self.img  = img
        self.rect = pg.Rect(400, 450, 30, 30)
        self.vx   = random.randint(-10, 10)
        self.vy   = -5

    def bounce_wall(self):
        if self.rect.y < 0:
            self.vy = -self.vy
        if self.rect.x < 0 or self.rect.x > 800 - 30:
            self.vx = -self.vx

    def bounce_bar(self, barrect):
        if barrect.colliderect(self.rect):
            self.vx = int(((self.rect.x + 15) - (barrect.x + 50)) / 4)
            self.vy = random.randint(-10, -5)
            pg.mixer.Sound(SND_DIR / "pi.wav").play()

    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

    def draw(self):
        screen.blit(self.img, self.rect)

    def is_out(self):
        return self.rect.y > 600

    def reset(self):
        self.rect.x = 400
        self.rect.y = 450
        self.vx = random.randint(-10, 10)
        self.vy = -5


ballimg = pg.image.load(IMG_DIR / "kaeru.png")
ballimg = pg.transform.scale(ballimg, (30, 30))
ball    = Ball(ballimg)

barrect    = pg.Rect(400, 500, 100, 20)
replay_img = pg.image.load(IMG_DIR / "replaybtn.png")

blocks = []
for yy in range(4):
    for xx in range(7):
        blocks.append(pg.Rect(50 + xx * 100, 40 + yy * 50, 80, 30))

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

    barrect.x = mx - 50
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
            if score == 28:
                pg.mixer.Sound(SND_DIR / "up.wav").play()
                page = 3


def gamereset():
    global score, blocks
    ball.reset()
    score  = 0
    blocks = []
    for yy in range(4):
        for xx in range(7):
            blocks.append(pg.Rect(50 + xx * 100, 40 + yy * 50, 80, 30))


def gameover():
    gamereset()
    screen.fill(pg.Color("NAVY"))
    font = pg.font.Font(None, 150)
    text = font.render("GAMEOVER", True, pg.Color("RED"))
    screen.blit(text, (100, 200))
    btn1 = screen.blit(replay_img, (320, 480))
    button_to_jump(btn1, 1)


def gameclear():
    gamereset()
    screen.fill(pg.Color("GOLD"))
    font = pg.font.Font(None, 150)
    text = font.render("GAMECLEAR", True, pg.Color("RED"))
    screen.blit(text, (60, 200))
    btn1 = screen.blit(replay_img, (320, 480))
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
    clock.tick(60)
