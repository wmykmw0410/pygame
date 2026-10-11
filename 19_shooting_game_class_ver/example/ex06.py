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

WIDTH, HEIGHT = 800, 600

FPS = 60

screen = pg.display.set_mode((WIDTH, HEIGHT))
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


SHIP_SIZE = 50


class MyShip:
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
OFFSCREEN_Y = -100
UFO_X_MAX = WIDTH - UFO_SIZE   # ジグザグ・リスポーン時のX座標の上限(750)
ZIGZAG_STEP  = 3
ZIGZAG_RANGE = 6
CHASE_STEP   = 3


class UFO:
    def __init__(self, img, x, y):
        self.img       = img
        self.rect      = pg.Rect(x, y, UFO_SIZE, UFO_SIZE)
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
            self.phase += ZIGZAG_STEP
            dx = int(math.sin(math.radians(self.phase)) * ZIGZAG_RANGE)
            self.rect.x += dx
            if self.rect.x < 0:
                self.rect.x = 0
            if self.rect.x > UFO_X_MAX:
                self.rect.x = UFO_X_MAX

        elif self.move_type == "chase":
            target_x = ship_x - SHIP_SIZE // 2
            if self.rect.x < target_x:
                self.rect.x += CHASE_STEP
            elif self.rect.x > target_x:
                self.rect.x -= CHASE_STEP

        if self.rect.y > HEIGHT:
            self.respawn()

    def draw(self):
        screen.blit(self.img, self.rect)

    def respawn(self):
        self.rect.x = random.randint(0, UFO_X_MAX)
        self.rect.y = OFFSCREEN_Y
        self.phase  = random.randint(0, 360)


BULLET_SIZE  = 16
BULLET_SPEED = 15


class Bullet:
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
    ufos.append(UFO(ufoimg, random.randint(0, UFO_X_MAX), OFFSCREEN_Y * i))

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
        bullet.shoot(myship.rect.x + SHIP_SIZE // 2 - BULLET_SIZE // 2, myship.rect.y)
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
            score += SCORE_PER_HIT
            ufo.respawn()
            bullet.deactivate()
            pg.mixer.Sound(SOUND_DIR / "piko.wav").play()

    font  = pg.font.Font(None, SCORE_FONT_SIZE)
    small = pg.font.Font(None, 28)

    score_text = font.render("SCORE: " + str(score), True, pg.Color("WHITE"))
    screen.blit(score_text, SCORE_POS)

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
    for i in range(UFO_COUNT):
        ufos[i].respawn()


def gameover():
    screen.fill(pg.Color("NAVY"))
    font = pg.font.Font(None, RESULT_FONT_SIZE)
    text = font.render("GAMEOVER", True, pg.Color("RED"))
    screen.blit(text, (100, 200))
    btn1 = screen.blit(replay_img, REPLAY_BTN_POS)
    font = pg.font.Font(None, SCORE_FONT_SIZE)
    text = font.render("SCORE: " + str(score), True, pg.Color("WHITE"))
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
