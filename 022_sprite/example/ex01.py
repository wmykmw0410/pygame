# ex01: Sprite クラスで1体を動かす
# → pg.sprite.Sprite を継承すると、image と rect を持つのが「お約束」になる

from pathlib import Path
import pygame as pg
import sys
import random

pg.init()
WIDTH, HEIGHT = 600, 400
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("ex01: 1体を動かす")
clock  = pg.time.Clock()
IMG_DIR = Path(__file__).resolve().parent.parent / "images"


class Enemy(pg.sprite.Sprite):
    def __init__(self, img, x, y):
        super().__init__()          # ← Sprite の __init__ を呼ぶ
        self.image = img            # ← Sprite のお約束: self.image を持つ
        self.rect  = self.image.get_rect(topleft=(x, y))  # ← Sprite のお約束: self.rect を持つ
        self.vx    = random.choice([-3, -2, 2, 3])
        self.vy    = random.choice([-3, -2, 2, 3])

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        # 壁に当たったら跳ね返る
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.vx = -self.vx
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.vy = -self.vy


enemy_img = pg.image.load(IMG_DIR / "enemy1.png")
enemy = Enemy(enemy_img, 100, 100)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill(pg.Color("NAVY"))

    enemy.update()
    screen.blit(enemy.image, enemy.rect)

    pg.display.update()
    clock.tick(60)
