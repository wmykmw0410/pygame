# ex05: UFO の速さをインスタンスごとに変える（完成）
# → UFO クラスに speed 属性を追加してインスタンスごとに落下速度を変える
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


SHIP_SIZE = 50


class MyShip():
    def __init__(self, img):
        self.img  = img
        self.rect = pg.Rect(400, 500, SHIP_SIZE, SHIP_SIZE)

    def update(self, mx):
        self.rect.x = mx - SHIP_SIZE // 2

    def draw(self):
        screen.blit(self.img, self.rect)

    def reset(self):
        self.rect.x = 400
        self.rect.y = 500


UFO_SIZE = 50
UFO_COUNT = 10
UFO_SPEED_RANGE = (5, 15)
OFFSCREEN_Y = -100


# ── ex04 との違い: speed 属性を追加してインスタンスごとに速さを変えた ──
class UFO():
    def __init__(self, img, x, y, speed):
        self.img   = img
        self.rect  = pg.Rect(x, y, UFO_SIZE, UFO_SIZE)
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.rect.x = random.randint(0, WIDTH)
            self.rect.y = OFFSCREEN_Y

    def draw(self):
        screen.blit(self.img, self.rect)

    def respawn(self):
        self.rect.x = random.randint(0, WIDTH)
        self.rect.y = OFFSCREEN_Y


BULLET_SIZE  = 16
BULLET_SPEED = 15


class Bullet():
    def __init__(self, img):
        self.img  = img
        self.rect = pg.Rect(0, OFFSCREEN_Y, BULLET_SIZE, BULLET_SIZE)

    def shoot(self, x, y):
        if not self.is_active():
            self.rect.x = x
            self.rect.y = y
            pg.mixer.Sound(SOUND_DIR / "pi.wav").play()

    def update(self):
        if self.is_active():
            self.rect.y -= BULLET_SPEED

    def draw(self):
        if self.is_active():
            screen.blit(self.img, self.rect)

    def is_active(self):
        return self.rect.y >= 0

    def deactivate(self):
        self.rect.y = OFFSCREEN_Y

    def reset(self):
        self.rect.y = OFFSCREEN_Y


REPLAY_BTN_POS   = (320, 480)
RESULT_FONT_SIZE = 150
SCORE_FONT_SIZE  = 40
SCORE_POS        = (20, 20)
SCORE_PER_HIT    = 10

myimg  = pg.image.load(IMG_DIR / "myship.png")
myimg  = pg.transform.scale(myimg, (SHIP_SIZE, SHIP_SIZE))
myship = MyShip(myimg)

bulletimg = pg.image.load(IMG_DIR / "bullet.png")
bulletimg = pg.transform.scale(bulletimg, (BULLET_SIZE, BULLET_SIZE))
bullet    = Bullet(bulletimg)

ufoimg = pg.image.load(IMG_DIR / "UFO.png")
ufoimg = pg.transform.scale(ufoimg, (UFO_SIZE, UFO_SIZE))
ufos   = []
for i in range(UFO_COUNT):
    ufos.append(UFO(ufoimg, random.randint(0, WIDTH), OFFSCREEN_Y * i, random.randint(*UFO_SPEED_RANGE)))

replay_img = pg.image.load(IMG_DIR / "replaybtn.png")

pushFlag = False
page     = 1
score    = 0


def button_to_jump(btn, newpage):
    global page, pushFlag
    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()
    if mdown[0]:
        if btn.collidepoint(mx, my) and not pushFlag:
            pg.mixer.Sound(SOUND_DIR / "pi.wav").play()
            page = newpage
            pushFlag = True
    else:
        pushFlag = False


def gamestage():
    global page, score
    screen.fill(pg.Color("NAVY"))
    (mx, my) = pg.mouse.get_pos()
    mdown = pg.mouse.get_pressed()

    myship.update(mx)
    myship.draw()

    if mdown[0]:
        bullet.shoot(myship.rect.x + SHIP_SIZE // 2 - BULLET_SIZE // 2, myship.rect.y)
    bullet.update()
    bullet.draw()

    for ufo in ufos:
        ufo.update()
        ufo.draw()
        if ufo.rect.colliderect(myship.rect):
            page = 2
            pg.mixer.Sound(SOUND_DIR / "down.wav").play()
        if ufo.rect.colliderect(bullet.rect) and bullet.is_active():
            score += SCORE_PER_HIT
            ufo.respawn()
            bullet.deactivate()
            pg.mixer.Sound(SOUND_DIR / "piko.wav").play()

    font = pg.font.Font(None, SCORE_FONT_SIZE)
    text = font.render("SCORE:" + str(score), True, pg.Color("WHITE"))
    screen.blit(text, SCORE_POS)


def gamereset():
    global score
    score = 0
    myship.reset()
    bullet.reset()
    for i in range(UFO_COUNT):
        ufos[i].respawn()


def gameover():
    screen.fill(pg.Color("NAVY"))
    font = pg.font.Font(None, RESULT_FONT_SIZE)
    text = font.render("GAMEOVER", True, pg.Color("RED"))
    screen.blit(text, (100, 200))
    btn1 = screen.blit(replay_img, REPLAY_BTN_POS)
    font = pg.font.Font(None, SCORE_FONT_SIZE)
    text = font.render("SCORE:" + str(score), True, pg.Color("WHITE"))
    screen.blit(text, SCORE_POS)
    button_to_jump(btn1, 1)
    if page == 1:
        gamereset()


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
