# ex04: キーボードで Group への追加・削除・全削除を操作する
# → ↑キーで敵を1体追加、↓キーでランダムに1体削除、SPACEキーで全削除する

from pathlib import Path
import pygame as pg
import sys
import random

pg.init()
WIDTH, HEIGHT = 600, 400
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("ex04: ↑追加 / ↓削除 / SPACEで全削除")
clock  = pg.time.Clock()
IMG_DIR = Path(__file__).resolve().parent.parent / "images"
font    = pg.font.Font(None, 28)

MAX_ENEMIES = 20   # 増えすぎないように上限を決めておく


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

        # 壁に当たったら跳ね返る（このステップでは spawn_enemy() は呼ばない）
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.vx = -self.vx
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.vy = -self.vy


def spawn_enemy():
    if len(enemies) >= MAX_ENEMIES:
        return
    img = random.choice(enemy_imgs)
    x   = random.randint(0, WIDTH - 50)
    y   = random.randint(0, HEIGHT - 50)
    enemies.add(Enemy(img, x, y))   # ← Group に1体追加する


enemy_imgs = [
    pg.image.load(IMG_DIR / "enemy1.png"),
    pg.image.load(IMG_DIR / "enemy2.png"),
    pg.image.load(IMG_DIR / "enemy3.png"),
]

enemies = pg.sprite.Group()
for i, img in enumerate(enemy_imgs):
    enemies.add(Enemy(img, 100 + i * 150, 100))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                spawn_enemy()
            if event.key == pg.K_DOWN:
                if len(enemies) > 0:
                    enemies.remove(random.choice(enemies.sprites()))   # ← Group からランダムに1体取り除く
            if event.key == pg.K_SPACE:
                enemies.empty()   # ← Group の中身を1回で全部取り除く

    screen.fill(pg.Color("NAVY"))

    enemies.update()
    enemies.draw(screen)

    count_s = font.render(f"Enemies: {len(enemies)}", True, pg.Color("WHITE"))
    screen.blit(count_s, (10, 10))

    pg.display.update()
    clock.tick(60)
