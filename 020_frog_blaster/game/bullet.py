from pathlib import Path
import pygame as pg

BASE_DIR = Path(__file__).resolve().parent
IMG_DIR  = BASE_DIR / "images"

class Bullet():
    def __init__(self, rect) -> None:
        x = rect.x + 17
        y = rect.y - 10
        self.image    = pg.image.load(IMG_DIR / "bullet.png")
        self.rect     = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.vy       = -8
        self.is_alive = True

    def update(self):
        self.rect.y += self.vy
        if self.rect.y < -100:
            self.is_alive = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
