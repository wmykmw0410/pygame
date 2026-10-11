import pygame as pg

SHIP_SIZE = 50


class MyShip:
    def __init__(self, img):
        self.img  = img
        self.rect = pg.Rect(400, 500, SHIP_SIZE, SHIP_SIZE)

    def update(self, mx):
        self.rect.x = mx - SHIP_SIZE // 2

    def draw(self, screen):
        screen.blit(self.img, self.rect)

    def reset(self):
        self.rect.x = 400
        self.rect.y = 500
