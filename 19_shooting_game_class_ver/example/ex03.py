# ex03: UFO クラスを作る
# → UFO をクラス化してリストで複数インスタンスを管理する
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


UFO_SIZE  = 50
UFO_COUNT = 10
UFO_SPEED = 10
OFFSCREEN_Y = -100


# ── ex02 との違い: UFO を UFO クラスにまとめた ──
class UFO():
    def __init__(self, img, x, y):
        self.img  = img
        self.rect = pg.Rect(x, y, UFO_SIZE, UFO_SIZE)

    def update(self):
        self.rect.y += UFO_SPEED
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
REPLAY_BTN_POS   = (320, 480)
RESULT_FONT_SIZE = 150
SCORE_FONT_SIZE  = 40
SCORE_POS        = (20, 20)
SCORE_PER_HIT    = 10

myimg  = pg.image.load(IMG_DIR / "myship.png")
myimg  = pg.transform.scale(myimg, (SHIP_SIZE, SHIP_SIZE))
myship = MyShip(myimg)

bulletimg  = pg.image.load(IMG_DIR / "bullet.png")
bulletimg  = pg.transform.scale(bulletimg, (BULLET_SIZE, BULLET_SIZE))
bulletrect = pg.Rect(400, OFFSCREEN_Y, BULLET_SIZE, BULLET_SIZE)

ufoimg = pg.image.load(IMG_DIR / "UFO.png")
ufoimg = pg.transform.scale(ufoimg, (UFO_SIZE, UFO_SIZE))
ufos   = []
for i in range(UFO_COUNT):
    ufos.append(UFO(ufoimg, random.randint(0, WIDTH), OFFSCREEN_Y * i))

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

    if mdown[0] and bulletrect.y < 0:
        bulletrect.x = myship.rect.x + SHIP_SIZE // 2 - BULLET_SIZE // 2
        bulletrect.y = myship.rect.y
        pg.mixer.Sound(SOUND_DIR / "pi.wav").play()
    if bulletrect.y >= 0:
        bulletrect.y -= BULLET_SPEED
        screen.blit(bulletimg, bulletrect)

    for ufo in ufos:
        ufo.update()
        ufo.draw()
        if ufo.rect.colliderect(myship.rect):
            page = 2
            pg.mixer.Sound(SOUND_DIR / "down.wav").play()
        if ufo.rect.colliderect(bulletrect):
            score += SCORE_PER_HIT
            ufo.respawn()
            bulletrect.y = OFFSCREEN_Y
            pg.mixer.Sound(SOUND_DIR / "piko.wav").play()

    font = pg.font.Font(None, SCORE_FONT_SIZE)
    text = font.render("SCORE:" + str(score), True, pg.Color("WHITE"))
    screen.blit(text, SCORE_POS)


def gamereset():
    global score
    score = 0
    myship.reset()
    bulletrect.y = OFFSCREEN_Y
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
