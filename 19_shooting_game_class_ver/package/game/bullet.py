from pathlib import Path
import pygame as pg

BASE_DIR  = Path(__file__).resolve().parent.parent.parent
SOUND_DIR = BASE_DIR / "sounds"

BULLET_SIZE  = 16
BULLET_SPEED = 15
OFFSCREEN_Y  = -100


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

    def draw(self, screen):
        if self.is_active():
            screen.blit(self.img, self.rect)

    def is_active(self):
        return self.rect.y >= 0

    def deactivate(self):
        self.rect.y = OFFSCREEN_Y

    def reset(self):
        self.rect.y = OFFSCREEN_Y
