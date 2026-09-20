from pathlib import Path
import pygame as pg
import random

BASE_DIR = Path(__file__).resolve().parent
IMG_DIR  = BASE_DIR / "images"

WIDTH, HEIGHT = 600, 650

ENEMY_SIZE          = 50
ENEMY_SPAWN_X_RANGE = (100, 500)
ENEMY_SPAWN_Y       = -100
ENEMY_VX_RANGE      = (-4, 4)
ENEMY_VY_RANGE      = (1, 4)
ENEMY_MAX_HP        = 100

FLAME_VX_RANGE = (-2, 2)
FLAME_VY_RANGE = (5, 7)

ICE_MAX_HP = 150

BOMB_FRAME_COUNT = 6

HP_BAR_WIDTH  = 4
HP_BAR_HEIGHT = 20
HP_BAR_OFFSET = 20

ANIM_FRAME_DELAY = 5

class Enemy():
    def __init__(self):
        x = random.randint(*ENEMY_SPAWN_X_RANGE)
        y = ENEMY_SPAWN_Y
        self.image    = pg.image.load(IMG_DIR / "enemy1.png")
        self.rect     = pg.Rect(x, y, ENEMY_SIZE, ENEMY_SIZE)
        self.vx       = random.uniform(*ENEMY_VX_RANGE)
        self.vy       = random.uniform(*ENEMY_VY_RANGE)
        self.maxhp    = ENEMY_MAX_HP
        self.hp       = ENEMY_MAX_HP
        self.is_alive = True

    def update(self):
        if self.rect.x < 0 or self.rect.x > WIDTH - ENEMY_SIZE:
            self.vx = -self.vx
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.y > HEIGHT:
            self.is_alive = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        rect1 = pg.Rect(self.rect.x, self.rect.y - HP_BAR_OFFSET, HP_BAR_WIDTH, HP_BAR_HEIGHT)
        h     = (self.hp / self.maxhp) * HP_BAR_HEIGHT
        rect2 = pg.Rect(self.rect.x, self.rect.y - h, HP_BAR_WIDTH, h)
        pg.draw.rect(screen, pg.Color("RED"),   rect1)
        pg.draw.rect(screen, pg.Color("GREEN"), rect2)


class FlameEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(IMG_DIR / "enemy2.png")
        self.vx    = random.uniform(*FLAME_VX_RANGE)
        self.vy    = random.uniform(*FLAME_VY_RANGE)


class IceEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.image  = pg.image.load(IMG_DIR / "enemy3.png")
        self.maxhp  = ICE_MAX_HP
        self.hp     = ICE_MAX_HP


class BombEffect():
    def __init__(self, rect, effects) -> None:
        self.images = []
        for i in range(BOMB_FRAME_COUNT):
            self.images.append(pg.image.load(IMG_DIR / f"bomb_{i}.png"))
        self.image   = self.images[0]
        self.effects = effects
        self.rect    = rect
        self.cnt     = 0

    def update(self):
        self.cnt += 1
        idx = self.cnt // ANIM_FRAME_DELAY
        if idx <= BOMB_FRAME_COUNT - 1:
            self.image = self.images[idx]
        else:
            self.effects.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class EnemyFactory():
    def create(self, etype):
        if etype == "flame":
            return FlameEnemy()
        elif etype == "ice":
            return IceEnemy()
        else:
            return Enemy()

    def random_create(self):
        etype = random.choice(["normal", "flame", "ice"])
        return self.create(etype)
