import math
import random
import pygame as pg
from .level import get_level

HEIGHT       = 600
SHIP_SIZE    = 50
UFO_SIZE     = 50
OFFSCREEN_Y  = -100
UFO_X_MAX    = 800 - UFO_SIZE   # WIDTH(800) - UFO_SIZE。ジグザグ・リスポーン時のX座標の上限
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

    def draw(self, screen):
        screen.blit(self.img, self.rect)

    def respawn(self):
        self.rect.x = random.randint(0, UFO_X_MAX)
        self.rect.y = OFFSCREEN_Y
        self.phase  = random.randint(0, 360)
