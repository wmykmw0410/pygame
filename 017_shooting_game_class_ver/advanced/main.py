# 発展版: 得点によって UFO の速度と移動パターンが変化する
import math
from pathlib import Path
import pygame as pg
import sys
import random

pg.init()
BASE_DIR  = Path(__file__).resolve().parent.parent
IMG_DIR   = BASE_DIR / "images"
SOUND_DIR = BASE_DIR / "sounds"

screen = pg.display.set_mode((800, 600))
pg.display.set_caption("シューティングゲーム 発展版")
clock = pg.time.Clock()

# 難易度テーブル（スコアが高い順に並べる）
LEVELS = [
    {"min_score": 300, "name": "CHASE",  "speed": 10, "move": "chase",  "bg": (60,  0,   0)},
    {"min_score": 200, "name": "ZIGZAG", "speed":  7, "move": "zigzag", "bg": (0,   50,  0)},
    {"min_score": 100, "name": "FAST",   "speed":  7, "move": "fast",   "bg": (50,  0,   80)},
    {"min_score":   0, "name": "NORMAL", "speed":  4, "move": "normal", "bg": (0,   0,   128)},
]


def get_level(score):
    for lv in LEVELS:
        if score >= lv["min_score"]:
            return lv
    return LEVELS[-1]


class MyShip:
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


class UFO:
    def __init__(self, img, x, y):
        self.img       = img
        self.rect      = pg.Rect(x, y, 50, 50)
        self.speed     = 4
        self.move_type = "normal"
        self.phase     = random.randint(0, 360)   # 各 UFO の位相をずらす

    def set_difficulty(self, score):
        lv             = get_level(score)
        self.speed     = lv["speed"]
        self.move_type = lv["move"]

    def update(self, ship_x):
        self.rect.y += self.speed

        if self.move_type == "zigzag":
            self.phase += 3
            dx = int(math.sin(math.radians(self.phase)) * 6)
            self.rect.x += dx
            if self.rect.x < 0:
                self.rect.x = 0
            if self.rect.x > 750:
                self.rect.x = 750

        elif self.move_type == "chase":
            target_x = ship_x - 25
            if self.rect.x < target_x:
                self.rect.x += 3
            elif self.rect.x > target_x:
                self.rect.x -= 3

        if self.rect.y > 600:
            self.respawn()

    def draw(self):
        screen.blit(self.img, self.rect)

    def respawn(self):
        self.rect.x = random.randint(0, 750)
        self.rect.y = -100
        self.phase  = random.randint(0, 360)


class Bullet:
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
    ufos.append(UFO(ufoimg, random.randint(0, 750), -100 * i))

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
    lv = get_level(score)
    screen.fill(lv["bg"])

    (mx, my) = pg.mouse.get_pos()
    mdown = pg.mouse.get_pressed()

    myship.update(mx)
    myship.draw()

    if mdown[0]:
        bullet.shoot(myship.rect.x + 25 - 8, myship.rect.y)
    bullet.update()
    bullet.draw()

    for ufo in ufos:
        ufo.set_difficulty(score)
        ufo.update(myship.rect.x)
        ufo.draw()
        if ufo.rect.colliderect(myship.rect):
            page = 2
            pg.mixer.Sound(SOUND_DIR / "down.wav").play()
        if ufo.rect.colliderect(bullet.rect) and bullet.is_active():
            score += 10
            ufo.respawn()
            bullet.deactivate()
            pg.mixer.Sound(SOUND_DIR / "piko.wav").play()

    font  = pg.font.Font(None, 40)
    small = pg.font.Font(None, 28)

    score_text = font.render("SCORE: " + str(score), True, pg.Color("WHITE"))
    screen.blit(score_text, (20, 20))

    lv_text = font.render("LEVEL: " + lv["name"], True, pg.Color("YELLOW"))
    screen.blit(lv_text, (20, 58))

    # 次のレベルまでの残りスコアを表示
    next_score = 0
    for lv_data in reversed(LEVELS):
        if lv_data["min_score"] > score:
            next_score = lv_data["min_score"]
            break
    if next_score > 0:
        remain = next_score - score
        hint = small.render("NEXT LV: " + str(remain) + " pts", True, pg.Color("LIGHTGRAY"))
        screen.blit(hint, (20, 90))


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
    text = font.render("SCORE: " + str(score), True, pg.Color("WHITE"))
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
