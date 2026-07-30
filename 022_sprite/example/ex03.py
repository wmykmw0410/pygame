# ex03: 敵同士がぶつかったら跳ね返る（完成）
# → Group を一覧のリストに変換し、総当たりで衝突をチェックする

from pathlib import Path
import pygame as pg
import sys
import random

pg.init()
WIDTH, HEIGHT = 600, 400
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("ex03: 敵同士がぶつかったら跳ね返る")
clock  = pg.time.Clock()
IMG_DIR = Path(__file__).resolve().parent.parent / "images"


class Enemy(pg.sprite.Sprite):
    def __init__(self, img, x, y):
        super().__init__()
        self.image = img
        self.rect  = self.image.get_rect(topleft=(x, y))
        self.vx    = random.choice([-3, -2, 2, 3])
        self.vy    = random.choice([-3, -2, 2, 3])

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.vx = -self.vx
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.vy = -self.vy

    def bounce(self):
        self.vx = -self.vx
        self.vy = -self.vy


enemy_imgs = [
    pg.image.load(IMG_DIR / "enemy1.png"),
    pg.image.load(IMG_DIR / "enemy2.png"),
    pg.image.load(IMG_DIR / "enemy3.png"),
]

enemies = pg.sprite.Group()
for i, img in enumerate(enemy_imgs):
    x = 100 + i * 150
    y = 100
    enemies.add(Enemy(img, x, y))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill(pg.Color("NAVY"))

    enemies.update()

    # ── ex02 との違い: 敵同士の総当たりで衝突をチェックする ──
    enemy_list = enemies.sprites()   # ← Group の中身をリストとして取り出す
    for i in range(len(enemy_list)):
        for j in range(i + 1, len(enemy_list)):
            if enemy_list[i].rect.colliderect(enemy_list[j].rect):
                enemy_list[i].bounce()
                enemy_list[j].bounce()

    enemies.draw(screen)

    pg.display.update()
    clock.tick(60)
