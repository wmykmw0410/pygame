# ex02: MyShip クラスにまとめる
# → 自機のデータ（rect・img）と処理（移動・描画）を MyShip クラスに集約する
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


# ── ex01 との違い: 自機を MyShip クラスにまとめた ──
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


myimg  = pg.image.load(IMG_DIR / "myship.png")
myimg  = pg.transform.scale(myimg, (50, 50))
myship = MyShip(myimg)

bulletimg  = pg.image.load(IMG_DIR / "bullet.png")
bulletimg  = pg.transform.scale(bulletimg, (16, 16))
bulletrect = pg.Rect(400, -100, 16, 16)

ufoimg = pg.image.load(IMG_DIR / "UFO.png")
ufoimg = pg.transform.scale(ufoimg, (50, 50))
ufos   = []
for i in range(10):
    ux = random.randint(0, 800)
    uy = -100 * i
    ufos.append(pg.Rect(ux, uy, 50, 50))

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
        bulletrect.x = myship.rect.x + 25 - 8
        bulletrect.y = myship.rect.y
        pg.mixer.Sound(SOUND_DIR / "pi.wav").play()
    if bulletrect.y >= 0:
        bulletrect.y -= 15
        screen.blit(bulletimg, bulletrect)

    for ufo in ufos:
        ufo.y += 10
        screen.blit(ufoimg, ufo)
        if ufo.y > 600:
            ufo.x = random.randint(0, 800)
            ufo.y = -100
        if ufo.colliderect(myship.rect):
            page = 2
            pg.mixer.Sound(SOUND_DIR / "down.wav").play()
        if ufo.colliderect(bulletrect):
            score += 10
            ufo.y = -100
            ufo.x = random.randint(0, 800)
            bulletrect.y = -100
            pg.mixer.Sound(SOUND_DIR / "piko.wav").play()

    font = pg.font.Font(None, 40)
    text = font.render("SCORE:" + str(score), True, pg.Color("WHITE"))
    screen.blit(text, (20, 20))


def gamereset():
    global score
    score = 0
    myship.reset()
    bulletrect.y = -100
    for i in range(10):
        ufos[i] = pg.Rect(random.randint(0, 800), -100 * i, 50, 50)


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
