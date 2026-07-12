# ex03: Character 基底クラスを作る
# → 共通処理を Character にまとめ、Player(Character) として派生させる

import pygame as pg
import sys
from pathlib import Path

pg.init()
screen = pg.display.set_mode((600, 400))
pg.display.set_caption("ex03: Character 基底クラス")
clock  = pg.time.Clock()
FONT   = Path(__file__).resolve().parent.parent / "fonts" / "NotoSansCJKjp-Regular.otf"
font   = pg.font.Font(FONT, 24)
font_s = pg.font.Font(FONT, 20)
WHITE  = pg.Color("WHITE")


# ── ex02 との違い: 名前・HP・生死判定を Character 基底クラスにまとめた ──
class Character():
    def __init__(self, name, hp):
        self.name = name
        self.hp   = hp

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0


class Player(Character):
    def __init__(self, name, cx, color, hp):
        super().__init__(name, hp)   # ← Character の __init__ を呼ぶ
        self.rect  = pg.Rect(cx - 30, 200, 60, 60)
        self.color = color

    # is_alive() / take_damage() は Character から継承 → 書かなくてよい

    def draw(self):
        if self.is_alive():
            color = self.color
        else:
            color = pg.Color("GRAY")
        pg.draw.rect(screen, color, self.rect)
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
