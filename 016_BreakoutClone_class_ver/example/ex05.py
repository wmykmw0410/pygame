# ex05: ボールを複数に増やす
# → ball 1個 → balls リストで複数インスタンスを管理する
# → 画面外に出たボールをリストから除き、全滅でゲームオーバー
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


class Ball():
    def __init__(self, img, x):
        self.img  = img
        self.rect = pg.Rect(x, 450, 30, 30)
        self.vx   = random.randint(-10, 10)
        self.vy   = -5

    def bounce_wall(self):
        if self.rect.y < 0:
            self.vy = -self.vy
        if self.rect.x < 0 or self.rect.x > 800 - 30:
            self.vx = -self.vx

    def bounce_bar(self, bar):
        if bar.rect.colliderect(self.rect):
            self.vx = int(((self.rect.x + 15) - (bar.rect.x + 50)) / 4)
            self.vy = random.randint(-10, -5)
            pg.mixer.Sound(SND_DIR / "pi.wav").play()

    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

    def draw(self):
        screen.blit(self.img, self.rect)

    def is_out(self):
        return self.rect.y > 600


ROW_COLORS = ["RED", "ORANGE", "YELLOW", "GREEN"]


class Block():
    def __init__(self, x, y, color):
        self.rect   = pg.Rect(x, y, 80, 30)
        self.color  = color
        self.active = True

    def draw(self):
        if self.active:
            pg.draw.rect(screen, self.color, self.rect)

    def check_hit(self, ball):
        if self.active and self.rect.colliderect(ball.rect):
            self.active = False
            ball.vy = -ball.vy
            pg.mixer.Sound(SND_DIR / "piko.wav").play()
            return True
        return False


class Bar():
    def __init__(self):
        self.rect = pg.Rect(400, 500, 100, 20)

    def update(self, mx):
        self.rect.x = mx - 50

    def draw(self):
        pg.draw.rect(screen, pg.Color("CYAN"), self.rect)


def make_blocks():
    result = []
    for yy in range(4):
        color = pg.Color(ROW_COLORS[yy])
        for xx in range(7):
            result.append(Block(50 + xx * 100, 40 + yy * 50, color))
    return result


def make_balls():
    # ── ex04 との違い: ボールを3個、横に並べて生成する ──
    result = []
    result.append(Ball(ballimg, 200))
    result.append(Ball(ballimg, 400))
    result.append(Ball(ballimg, 600))
    return result


ballimg    = pg.image.load(IMG_DIR / "kaeru.png")
ballimg    = pg.transform.scale(ballimg, (30, 30))
bar        = Bar()
replay_img = pg.image.load(IMG_DIR / "replaybtn.png")
blocks     = make_blocks()
balls      = make_balls()

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
    global page, score, blocks, balls
    screen.fill(pg.Color("NAVY"))
    (mx, my) = pg.mouse.get_pos()

    bar.update(mx)
    bar.draw()

    # ── ex04 との違い: balls リストを回して、画面外のボールを除く ──
    alive_balls = []
    for ball in balls:
        ball.bounce_wall()
        ball.bounce_bar(bar)
        ball.move()
        ball.draw()
        if not ball.is_out():
            alive_balls.append(ball)
    balls = alive_balls

    if len(balls) == 0:
        page = 2
        pg.mixer.Sound(SND_DIR / "pi.wav").play()

    for block in blocks:
        block.draw()
        for ball in balls:
            if block.check_hit(ball):
                score += 1
                if score == 28:
                    pg.mixer.Sound(SND_DIR / "up.wav").play()
                    page = 3


def gamereset():
    global score, blocks, balls
    score  = 0
    blocks = make_blocks()
    balls  = make_balls()


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
