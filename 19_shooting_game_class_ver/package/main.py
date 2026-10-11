# 発展版をクラスごとにファイル分割したもの
from pathlib import Path
import random
import sys
import pygame as pg
from game import MyShip, UFO, Bullet, LEVELS, get_level

pg.init()
BASE_DIR  = Path(__file__).resolve().parent.parent
IMG_DIR   = BASE_DIR / "images"
SOUND_DIR = BASE_DIR / "sounds"

WIDTH, HEIGHT = 800, 600
FPS = 60

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("シューティングゲーム 発展版（ファイル分割）")
clock = pg.time.Clock()

SHIP_SIZE   = 50
UFO_SIZE    = 50
UFO_COUNT   = 10
OFFSCREEN_Y = -100
UFO_X_MAX   = WIDTH - UFO_SIZE
BULLET_SIZE = 16

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
    myship.draw(screen)

    if mdown[0]:
        bullet.shoot(myship.rect.x + SHIP_SIZE // 2 - BULLET_SIZE // 2, myship.rect.y)
    bullet.update()
    bullet.draw(screen)

    for ufo in ufos:
        ufo.set_difficulty(score)
        ufo.update(myship.rect.x)
        ufo.draw(screen)
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
