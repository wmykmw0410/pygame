# ex04: Enemy を派生させ、パーティーをリストで管理する
# → ex03 の Character・Player に Enemy(Character) を追加する
# → 勇者1人だけだった ex03 から、パーティー（複数人）のリストに変える

import pygame as pg
import sys
import random
from pathlib import Path

pg.init()
screen = pg.display.set_mode((600, 400))
pg.display.set_caption("ex04: Character → Player / Enemy")
clock  = pg.time.Clock()
FONT   = Path(__file__).resolve().parent.parent / "fonts" / "NotoSansCJKjp-Regular.otf"
font   = pg.font.Font(FONT, 24)
font_s = pg.font.Font(FONT, 20)
WHITE  = pg.Color("WHITE")


# ── ex03 との違い: Enemy(Character) を追加し、パーティーをリストにした ──
class Character():
    def __init__(self, name, hp):
        self.name = name
        self.hp   = hp

    def is_alive(self):
        return self.hp > 0


class Player(Character):
    def __init__(self, name, cx, color, hp, attack):
        super().__init__(name, hp)
        self.attack = attack
        self.rect   = pg.Rect(cx - 30, 230, 60, 60)
        self.color  = color

    # is_alive() は Character から継承

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

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


class Enemy(Character):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.rect  = pg.Rect(270, 50, 60, 60)
        self.color = pg.Color("DARKGREEN")

    # is_alive() は Character から継承

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


enemy = Enemy("スライム", 80)
party = [
    Player("勇者",    100, pg.Color("ROYALBLUE"), hp=100, attack=25),
    Player("魔法使い", 300, pg.Color("PURPLE"),    hp=70,  attack=35),
    Player("戦士",    500, pg.Color("FIREBRICK"), hp=130, attack=20),
]

message   = "SPACE: 攻撃"
game_over = False

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and not game_over:
            alive = []
            for p in party:
                if p.is_alive():
                    alive.append(p)

            attacker = random.choice(alive)
            dmg = random.randint(attacker.attack - 5, attacker.attack + 5)
            enemy.hp -= dmg
            if enemy.hp < 0:
                enemy.hp = 0
            message = f"{attacker.name}の攻撃! {dmg}ダメージ!"
            if not enemy.is_alive():
                message = "スライムをたおした!"
                game_over = True

    screen.fill(pg.Color("DARKSLATEGRAY"))
    enemy.draw()
    for p in party:
        p.draw()

    msg = font_s.render(message, True, pg.Color("WHITE"))
    screen.blit(msg, msg.get_rect(centerx=300, top=345))

    pg.display.update()
    clock.tick(60)
