# ex02: Group で複数の敵を動かす
# → pg.sprite.Group にまとめると、更新も描画も1行ずつで済む

from pathlib import Path
import pygame as pg
import sys
import random

pg.init()
WIDTH, HEIGHT = 600, 400
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("ex02: Group で複数の敵を動かす")
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


enemy_imgs = [
    pg.image.load(IMG_DIR / "enemy1.png"),
    pg.image.load(IMG_DIR / "enemy2.png"),
    pg.image.load(IMG_DIR / "enemy3.png"),
]

# ── ex01 との違い: リストの代わりに Group を使う ──
enemies = pg.sprite.Group()
for i, img in enumerate(enemy_imgs):
    x = 100 + i * 150
    y = 100
    enemies.add(Enemy(img, x, y))   # ← Group に追加する

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill(pg.Color("NAVY"))

    # ── ex01 との違い: for ループが不要になった ──
    enemies.update()        # ← 全員の update() をまとめて呼ぶ
    enemies.draw(screen)    # ← 全員の image を rect の位置にまとめて描画する

    pg.display.update()
    clock.tick(60)
