# ex01: CLI版（015_class Q3）を pygame化する
# → Character・Enemy の継承構造はそのまま、print() の代わりに画面に描画する

from pathlib import Path
import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((600, 400))
pg.display.set_caption("ex01: CLI版をpygame化する")
clock  = pg.time.Clock()
FONT   = Path(__file__).resolve().parent.parent / "fonts" / "NotoSansCJKjp-Regular.otf"
font   = pg.font.Font(FONT, 24)
font_s = pg.font.Font(FONT, 20)
WHITE  = pg.Color("WHITE")


# ── 015_class の Q3 とまったく同じクラス（print の代わりにメッセージを返す）──
class Character():
    def __init__(self, name, attack_power):
        self.name         = name
        self.hp           = 100
        self.attack_power = attack_power

    def attack(self, target):
        target.hp -= self.attack_power
        return f"{self.name}の攻撃! {target.name}に{self.attack_power}ダメージ!"

    def is_alive(self):
        return self.hp > 0


class Enemy(Character):
    def __init__(self, name, attack_power):
        super().__init__(name, attack_power)
        self.hp = 150

    def attack(self, target):
        dmg = int(self.attack_power * 1.5)
        target.hp -= dmg
        return f"{self.name}の攻撃! {target.name}に{dmg}ダメージ!"


hero = Character("勇者", attack_power=30)
boss = Enemy("ラスボス", attack_power=15)

message   = "SPACE: 攻撃"
game_over = False

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and not game_over:
            message = hero.attack(boss)
            if not boss.is_alive():
                message = f"{boss.name}をたおした! {hero.name}の勝利!"
                game_over = True
            else:
                message = boss.attack(hero)
                if not hero.is_alive():
                    message = f"{hero.name}は倒れた… {boss.name}の勝利!"
                    game_over = True

    screen.fill(pg.Color("DARKSLATEGRAY"))

    hero_s = font.render(f"{hero.name}  HP:{hero.hp}", True, WHITE)
    screen.blit(hero_s, (60, 300))
    boss_s = font.render(f"{boss.name}  HP:{boss.hp}", True, WHITE)
    screen.blit(boss_s, (60, 60))

    msg = font_s.render(message, True, WHITE)
    screen.blit(msg, msg.get_rect(centerx=300, top=200))

    pg.display.update()
    clock.tick(60)
