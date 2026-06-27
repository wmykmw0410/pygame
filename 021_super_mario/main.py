from pathlib import Path
import pygame as pg
import sys

pg.init()

BASE_DIR  = Path(__file__).resolve().parent
IMG_DIR   = BASE_DIR.parent / "009_actiongame" / "images"
SND_DIR   = BASE_DIR.parent / "009_actiongame" / "sounds"

WIDTH, HEIGHT = 800, 600
WORLD_WIDTH   = 2400    # ステージ全体の幅（画面幅 × 3）
FPS = 60

GRAVITY    = 0.6
JUMP_POWER = -13
SPEED      = 5

PLAYING    = 1
GAME_OVER  = 2
GAME_CLEAR = 3

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("スーパーマリオ")
clock = pg.time.Clock()


class Player:
    def __init__(self, img_r, img_l):
        self.img_r      = img_r
        self.img_l      = img_l
        self.rect       = pg.Rect(60, 480, 40, 50)
        self.vx         = 0
        self.vy         = 0
        self.on_ground  = False
        self.face_right = True

    def jump(self):
        if self.on_ground:
            self.vy        = JUMP_POWER
            self.on_ground = False
            pg.mixer.Sound(SND_DIR / "pi.wav").play()

    def update(self, platforms):
        # 横移動と壁衝突（X のみ先に解決）
        self.rect.x += self.vx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WORLD_WIDTH:
            self.rect.right = WORLD_WIDTH
        for p in platforms:
            if self.rect.colliderect(p):
                if self.vx > 0:
                    self.rect.right = p.left
                elif self.vx < 0:
                    self.rect.left = p.right

        # 重力を加算
        self.vy += GRAVITY
        if self.vy > 15:
            self.vy = 15

        # 縦移動と足場衝突（Y のみ解決）
        self.on_ground = False
        self.rect.y += int(self.vy)
        for p in platforms:
            if self.rect.colliderect(p):
                if self.vy > 0:           # 落下中 → 足場の上に乗る
                    self.rect.bottom = p.top
                    self.vy          = 0
                    self.on_ground   = True
                elif self.vy < 0:         # 上昇中 → 天井に当たる
                    self.rect.top = p.bottom
                    self.vy       = 0

    def draw(self, scroll_x):
        # ワールド座標 → スクリーン座標に変換して描画
        draw_rect = pg.Rect(self.rect.x - scroll_x, self.rect.y, self.rect.w, self.rect.h)
        if self.face_right:
            screen.blit(self.img_r, draw_rect)
        else:
            screen.blit(self.img_l, draw_rect)

    def reset(self):
        self.rect.x     = 60
        self.rect.y     = 480
        self.vx         = 0
        self.vy         = 0
        self.on_ground  = False
        self.face_right = True


class Enemy:
    SPEED = 2

    def __init__(self, img_r, img_l, x, y, left_limit, right_limit):
        self.img_r       = img_r
        self.img_l       = img_l
        self.rect        = pg.Rect(x, y, 50, 50)
        self.vx          = self.SPEED
        self.alive       = True
        self.left_limit  = left_limit
        self.right_limit = right_limit
        self.init_x      = x
        self.init_y      = y

    def update(self):
        if not self.alive:
            return
        self.rect.x += self.vx
        if self.rect.right >= self.right_limit:
            self.vx = -self.SPEED
        if self.rect.left <= self.left_limit:
            self.vx = self.SPEED

    def is_stomped_by(self, player):
        if not self.alive:
            return False
        if player.vy <= 0:                                # 落下中でないと踏みつけにならない
            return False
        if not self.rect.colliderect(player.rect):
            return False
        if player.rect.bottom <= self.rect.centery + 10: # プレイヤーの足が敵の上半分にある
            return True
        return False

    def draw(self, scroll_x):
        if not self.alive:
            return
        draw_rect = pg.Rect(self.rect.x - scroll_x, self.rect.y, self.rect.w, self.rect.h)
        if self.vx >= 0:
            screen.blit(self.img_r, draw_rect)
        else:
            screen.blit(self.img_l, draw_rect)

    def reset(self):
        self.rect.x = self.init_x
        self.rect.y = self.init_y
        self.vx     = self.SPEED
        self.alive  = True


# リソース読み込み
myimgR    = pg.image.load(IMG_DIR / "playerR.png")
myimgR    = pg.transform.scale(myimgR, (40, 50))
myimgL    = pg.transform.flip(myimgR, True, False)

enemyimgR = pg.image.load(IMG_DIR / "obake.png")
enemyimgR = pg.transform.scale(enemyimgR, (50, 50))
enemyimgL = pg.transform.flip(enemyimgR, True, False)

replay_img = pg.image.load(IMG_DIR / "replaybtn.png")

player = Player(myimgR, myimgL)

# 地面と浮き足場（すべてワールド座標）
#
#  ゾーン1 (0〜800)        ゾーン2 (800〜1600)       ゾーン3 (1600〜2400)
#
#                                                              [GOAL]
#              [==]                    [===]        [==]  [==========]
#   [===] [=========]    [====]    [=======]   [====]  [======]
#   [地面=================================================(y=530)====]
#
GROUND    = pg.Rect(0, 530, WORLD_WIDTH, 70)
platforms = [
    GROUND,
    # ゾーン1
    pg.Rect(120,  420, 160, 20),
    pg.Rect(350,  350, 140, 20),
    pg.Rect(240,  290, 100, 20),
    pg.Rect(560,  280, 200, 20),
    # ゾーン2
    pg.Rect(880,  440, 120, 20),
    pg.Rect(1060, 370, 180, 20),
    pg.Rect(1280, 300, 150, 20),
    pg.Rect(1480, 390, 140, 20),
    # ゾーン3
    pg.Rect(1680, 430, 100, 20),
    pg.Rect(1840, 360, 120, 20),
    pg.Rect(2020, 280, 150, 20),
    pg.Rect(2230, 310, 130, 20),
    pg.Rect(2300, 230, 120, 20),   # ゴール直前の高台
]

# ゴール（高台の上）
goal_rect = pg.Rect(2360, 150, 30, 80)

# 敵（left_limit / right_limit はワールド座標）
enemies = [
    # ゾーン1
    Enemy(enemyimgR, enemyimgL,  300, 480,   50,  550),   # 地面
    Enemy(enemyimgR, enemyimgL,  370, 300,  350,  490),   # 中段足場
    Enemy(enemyimgR, enemyimgL,  580, 230,  560,  700),   # 高い足場
    # ゾーン2
    Enemy(enemyimgR, enemyimgL,  900, 480,  800, 1200),   # 地面
    Enemy(enemyimgR, enemyimgL, 1080, 320, 1060, 1240),   # 中段足場
    Enemy(enemyimgR, enemyimgL, 1300, 250, 1280, 1430),   # 高い足場
    # ゾーン3
    Enemy(enemyimgR, enemyimgL, 1700, 480, 1600, 2000),   # 地面
    Enemy(enemyimgR, enemyimgL, 1860, 310, 1840, 1960),   # 中段足場
    Enemy(enemyimgR, enemyimgL, 2040, 230, 2020, 2170),   # 高い足場
]

scroll_x = 0
pushFlag  = False
page      = PLAYING


def update_scroll():
    global scroll_x
    # プレイヤーが画面左から 200px の位置になるようカメラを動かす
    target = player.rect.x - 200
    if target < 0:
        target = 0
    if target > WORLD_WIDTH - WIDTH:
        target = WORLD_WIDTH - WIDTH
    scroll_x = target


def draw_rect_world(rect, color):
    """ワールド座標の Rect をスクリーン座標に変換して描画する"""
    draw_r = pg.Rect(rect.x - scroll_x, rect.y, rect.w, rect.h)
    pg.draw.rect(screen, color, draw_r)


def button_to_jump(btn, newpage):
    global page, pushFlag
    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()
    if mdown[0]:
        if btn.collidepoint(mx, my) and not pushFlag:
            pg.mixer.Sound(SND_DIR / "pi.wav").play()
            page     = newpage
            pushFlag = True
    else:
        pushFlag = False


def gamereset():
    global scroll_x
    scroll_x = 0
    player.reset()
    for enemy in enemies:
        enemy.reset()


def gamestage():
    global page
    screen.fill((135, 206, 235))   # 空色

    key = pg.key.get_pressed()
    player.vx = 0
    if key[pg.K_RIGHT]:
        player.vx          = SPEED
        player.face_right  = True
    if key[pg.K_LEFT]:
        player.vx          = -SPEED
        player.face_right  = False

    player.update(platforms)
    update_scroll()

    # 画面下に落ちたらゲームオーバー
    if player.rect.top > HEIGHT:
        pg.mixer.Sound(SND_DIR / "down.wav").play()
        page = GAME_OVER
        return

    # 地面（茶色）
    draw_rect_world(GROUND, (101, 67, 33))
    # 浮き足場（緑）
    for p in platforms[1:]:
        draw_rect_world(p, (34, 139, 34))

    # 敵の処理
    for enemy in enemies:
        enemy.update()
        enemy.draw(scroll_x)
        if enemy.is_stomped_by(player):
            enemy.alive = False
            player.vy   = -8          # 踏んだ後に小さくバウンド
            pg.mixer.Sound(SND_DIR / "up.wav").play()
        elif enemy.alive and player.rect.colliderect(enemy.rect):
            pg.mixer.Sound(SND_DIR / "down.wav").play()
            page = GAME_OVER
            return

    player.draw(scroll_x)

    # ゴール（金色の柱）
    draw_rect_world(goal_rect, pg.Color("GOLD"))
    font      = pg.font.Font(None, 30)
    goal_text = font.render("GOAL", True, pg.Color("RED"))
    screen.blit(goal_text, (goal_rect.x - scroll_x - 3, goal_rect.y - 25))
    if player.rect.colliderect(goal_rect):
        pg.mixer.Sound(SND_DIR / "up.wav").play()
        page = GAME_CLEAR

    # 進行度バー（右上 HUD）
    bar_x    = WIDTH - 220
    bar_y    = 12
    bar_w    = 200
    progress = player.rect.x / WORLD_WIDTH
    pg.draw.rect(screen, (60, 60, 60),      (bar_x, bar_y, bar_w, 10))
    pg.draw.rect(screen, pg.Color("YELLOW"), (bar_x, bar_y, int(bar_w * progress), 10))
    pg.draw.rect(screen, pg.Color("GOLD"),   (bar_x + bar_w + 4, bar_y - 3, 10, 16))  # ゴールマーク


def gameover():
    gamereset()
    screen.fill(pg.Color("NAVY"))
    font = pg.font.Font(None, 150)
    text = font.render("GAMEOVER", True, pg.Color("RED"))
    screen.blit(text, (70, 200))
    btn1 = screen.blit(replay_img, (320, 480))
    button_to_jump(btn1, PLAYING)


def gameclear():
    gamereset()
    screen.fill(pg.Color("GOLD"))
    font = pg.font.Font(None, 130)
    text = font.render("GAMECLEAR", True, pg.Color("RED"))
    screen.blit(text, (40, 200))
    btn1 = screen.blit(replay_img, (320, 480))
    button_to_jump(btn1, PLAYING)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if page == PLAYING:
                if event.key == pg.K_SPACE or event.key == pg.K_UP:
                    player.jump()

    if page == PLAYING:
        gamestage()
    elif page == GAME_OVER:
        gameover()
    elif page == GAME_CLEAR:
        gameclear()

    pg.display.update()
    clock.tick(FPS)
