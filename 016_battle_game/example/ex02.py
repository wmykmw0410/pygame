# ex02: Player クラスにまとめる
# → ex01 の変数・関数を1つの Player クラスにまとめて、勇者オブジェクトを描画する

import pygame as pg
import sys
from pathlib import Path

pg.init()
screen = pg.display.set_mode((600, 400))
pg.display.set_caption("ex02: Player クラス")
clock  = pg.time.Clock()
FONT   = Path(__file__).resolve().parent.parent / "fonts" / "NotoSansCJKjp-Regular.otf"
font   = pg.font.Font(FONT, 24)
font_s = pg.font.Font(FONT, 20)
WHITE  = pg.Color("WHITE")


# ── ex01 との違い: データと処理を Player クラスにまとめた ──
class Player():
    def __init__(self, name, cx, color, hp):
        self.name  = name
        self.hp    = hp
        self.rect  = pg.Rect(cx - 30, 200, 60, 60)
        self.color = color

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def draw(self):
        pg.draw.rect(screen, self.color, self.rect)
        name_s = font.render(self.name, True, WHITE)
        screen.blit(name_s, name_s.get_rect(centerx=self.rect.centerx, bottom=self.rect.top - 6))
        hp_s = font_s.render(f"HP: {self.hp}", True, WHITE)
        screen.blit(hp_s, hp_s.get_rect(centerx=self.rect.centerx, top=self.rect.bottom + 6))


hero = Player("勇者", 300, pg.Color("ROYALBLUE"), hp=100)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            hero.take_damage(10)

    screen.fill(pg.Color("DARKSLATEGRAY"))
    hero.draw()

    msg = font_s.render("SPACE: 勇者に 10 ダメージ", True, pg.Color("LIGHTGRAY"))
    screen.blit(msg, msg.get_rect(centerx=300, top=340))

    pg.display.update()
    clock.tick(60)
