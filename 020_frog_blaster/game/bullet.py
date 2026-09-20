from pathlib import Path
import pygame as pg

BASE_DIR = Path(__file__).resolve().parent
IMG_DIR  = BASE_DIR / "images"

BULLET_OFFSET = (17, -10)
BULLET_SPEED  = 8
OFFSCREEN_Y   = -100

class Bullet():
    def __init__(self, rect) -> None:
        x = rect.x + BULLET_OFFSET[0]
        y = rect.y + BULLET_OFFSET[1]
        self.image    = pg.image.load(IMG_DIR / "bullet.png")
        self.rect     = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.vy       = -BULLET_SPEED
        self.is_alive = True

    def update(self):
        self.rect.y += self.vy
        if self.rect.y < OFFSCREEN_Y:
            self.is_alive = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
