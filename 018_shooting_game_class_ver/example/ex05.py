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

screen = pg.display.set_mode((800, 600))
pg.display.set_caption("シューティングゲーム")
clock = pg.time.Clock()


class MyShip():
    def __init__(self, img):
        self.img  = img
        self.rect = pg.Rect(400, 500, 50, 50)

    def update(self, mx):
        self.rect.x = mx - 25

    def draw(self):
        screen.blit(self.img, self.rect)

    def reset(self):
        self.rect.x = 400
        self.rect.y = 500


# ── ex04 との違い: speed 属性を追加してインスタンスごとに速さを変えた ──
class UFO():
    def __init__(self, img, x, y, speed):
        self.img   = img
        self.rect  = pg.Rect(x, y, 50, 50)
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 600:
            self.rect.x = random.randint(0, 800)
            self.rect.y = -100

    def draw(self):
        screen.blit(self.img, self.rect)

    def respawn(self):
        self.rect.x = random.randint(0, 800)
        self.rect.y = -100


class Bullet():
    def __init__(self, img):
        self.img  = img
        self.rect = pg.Rect(0, -100, 16, 16)

    def shoot(self, x, y):
        if not self.is_active():
            self.rect.x = x
            self.rect.y = y
            pg.mixer.Sound(SOUND_DIR / "pi.wav").play()

    def update(self):
        if self.is_active():
            self.rect.y -= 15

    def draw(self):
        if self.is_active():
            screen.blit(self.img, self.rect)

    def is_active(self):
        return self.rect.y >= 0

    def deactivate(self):
        self.rect.y = -100

    def reset(self):
        self.rect.y = -100


myimg  = pg.image.load(IMG_DIR / "myship.png")
myimg  = pg.transform.scale(myimg, (50, 50))
myship = MyShip(myimg)

bulletimg = pg.image.load(IMG_DIR / "bullet.png")
bulletimg = pg.transform.scale(bulletimg, (16, 16))
bullet    = Bullet(bulletimg)

ufoimg = pg.image.load(IMG_DIR / "UFO.png")
ufoimg = pg.transform.scale(ufoimg, (50, 50))
ufos   = []
for i in range(10):
    ufos.append(UFO(ufoimg, random.randint(0, 800), -100 * i, random.randint(5, 15)))

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
        bullet.shoot(myship.rect.x + 25 - 8, myship.rect.y)
    bullet.update()
    bullet.draw()

    for ufo in ufos:
        ufo.update()
        ufo.draw()
        if ufo.rect.colliderect(myship.rect):
            page = 2
            pg.mixer.Sound(SOUND_DIR / "down.wav").play()
        if ufo.rect.colliderect(bullet.rect) and bullet.is_active():
            score += 10
            ufo.respawn()
            bullet.deactivate()
            pg.mixer.Sound(SOUND_DIR / "piko.wav").play()

    font = pg.font.Font(None, 40)
    text = font.render("SCORE:" + str(score), True, pg.Color("WHITE"))
    screen.blit(text, (20, 20))


def gamereset():
    global score
    score = 0
    myship.reset()
    bullet.reset()
    for i in range(10):
        ufos[i].respawn()


def gameover():
    screen.fill(pg.Color("NAVY"))
    font = pg.font.Font(None, 150)
    text = font.render("GAMEOVER", True, pg.Color("RED"))
    screen.blit(text, (100, 200))
    btn1 = screen.blit(replay_img, (320, 480))
    font = pg.font.Font(None, 40)
    text = font.render("SCORE:" + str(score), True, pg.Color("WHITE"))
    screen.blit(text, (20, 20))
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
    clock.tick(60)
