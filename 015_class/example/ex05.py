# ex05: Player クラスにまとめる
# → ex04 の変数・関数を1つのクラスにまとめてリストで管理する

import pygame as pg
import sys
from pathlib import Path

pg.init()
screen = pg.display.set_mode((600, 400))
pg.display.set_caption("ex05: Player クラス")
clock  = pg.time.Clock()
FONT   = Path(__file__).resolve().parent.parent / "fonts" / "NotoSansCJKjp-Regular.otf"
font   = pg.font.Font(FONT, 24)
font_s = pg.font.Font(FONT, 20)
WHITE  = pg.Color("WHITE")


# ── ex04 との違い: データと処理を Player クラスにまとめた ──
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


# リストで管理できるのでまとめて処理できる
party = [
    Player("勇者",    100, pg.Color("ROYALBLUE"), hp=100),
    Player("魔法使い", 300, pg.Color("PURPLE"),    hp=70),
    Player("戦士",    500, pg.Color("FIREBRICK"), hp=130),
]

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            for p in party:
                p.take_damage(10)   # まとめて処理できる

    screen.fill(pg.Color("DARKSLATEGRAY"))
    for p in party:
        p.draw()

    msg = font_s.render("SPACE: 全員に 10 ダメージ", True, pg.Color("LIGHTGRAY"))
    screen.blit(msg, msg.get_rect(centerx=300, top=340))

    pg.display.update()
    clock.tick(60)
