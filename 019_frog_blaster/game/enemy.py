from pathlib import Path
import pygame as pg
import random

BASE_DIR = Path(__file__).resolve().parent
IMG_DIR  = BASE_DIR / "images"

class Enemy():
    def __init__(self):
        x = random.randint(100, 500)
        y = -100
        self.image    = pg.image.load(IMG_DIR / "enemy1.png")
        self.rect     = pg.Rect(x, y, 50, 50)
        self.vx       = random.uniform(-4, 4)
        self.vy       = random.uniform(1, 4)
        self.maxhp    = 100
        self.hp       = 100
        self.is_alive = True

    def update(self):
        if self.rect.x < 0 or self.rect.x > 550:
            self.vx = -self.vx
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.y > 650:
            self.is_alive = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        rect1 = pg.Rect(self.rect.x, self.rect.y - 20, 4, 20)
        h     = (self.hp / self.maxhp) * 20
        rect2 = pg.Rect(self.rect.x, self.rect.y - h, 4, h)
        pg.draw.rect(screen, pg.Color("RED"),   rect1)
        pg.draw.rect(screen, pg.Color("GREEN"), rect2)


class FlameEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(IMG_DIR / "enemy2.png")
        self.vx    = random.uniform(-2, 2)
        self.vy    = random.uniform(5, 7)


class IceEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.image  = pg.image.load(IMG_DIR / "enemy3.png")
        self.maxhp  = 150
        self.hp     = 150


class BombEffect():
    def __init__(self, rect, effects) -> None:
        self._images = [
            pg.image.load(IMG_DIR / f"bomb_{i}.png") for i in range(6)
        ]
        self._image   = self._images[0]
        self._effects = effects
        self._rect    = rect
        self._cnt     = 0

    def update(self):
        self._cnt += 1
        idx = self._cnt // 5
        if idx <= 5:
            self._image = self._images[idx]
        else:
            self._effects.remove(self)

    def draw(self, screen):
        screen.blit(self._image, self._rect)


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
