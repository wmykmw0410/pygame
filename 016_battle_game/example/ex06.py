# ex06: 複数の敵と連戦する
# → enemy_queue で戦う順序を管理し、スライムを倒したらドラゴンと戦う

import pygame as pg
import sys
import random
from pathlib import Path

pg.init()
screen = pg.display.set_mode((600, 400))
pg.display.set_caption("ex06: 連戦")
clock  = pg.time.Clock()
FONT   = Path(__file__).resolve().parent.parent / "fonts" / "NotoSansCJKjp-Regular.otf"
font   = pg.font.Font(FONT, 24)
font_s = pg.font.Font(FONT, 20)
WHITE  = pg.Color("WHITE")


class Character():
    def __init__(self, name, hp):
        self.name   = name
        self.hp     = hp
        self.max_hp = hp

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0


class Player(Character):
    def __init__(self, name, cx, color, hp, attack):
        super().__init__(name, hp)   # ← Character の __init__ を呼ぶ
        self.attack = attack
        self.rect   = pg.Rect(cx - 30, 230, 60, 60)
        self.color  = color

    # is_alive() / take_damage() は Character から継承 → 書かなくてよい

    def draw(self):
        color = self.color if self.is_alive() else pg.Color("GRAY")
        pg.draw.rect(screen, color, self.rect)
        name_s = font.render(self.name, True, WHITE)
        screen.blit(name_s, name_s.get_rect(centerx=self.rect.centerx, bottom=self.rect.top - 6))
        hp_s = font_s.render(f"HP: {self.hp} / {self.max_hp}", True, WHITE)
        screen.blit(hp_s, hp_s.get_rect(centerx=self.rect.centerx, top=self.rect.bottom + 6))


# ── ex05 との違い: color / size を引数で受け取れるようにした ──
class Enemy(Character):
    def __init__(self, name, hp, attack, color="DARKGREEN", size=70):
        super().__init__(name, hp)   # ← Character の __init__ を呼ぶ
        self.attack = attack
        self.color  = pg.Color(color)
        self.rect   = pg.Rect(0, 40, size, size)
        self.rect.centerx = 300

    # is_alive() / take_damage() は Character から継承 → 書かなくてよい

    def draw(self):
        color = self.color if self.is_alive() else pg.Color("GRAY")
        pg.draw.rect(screen, color, self.rect)
        name_s = font.render(self.name, True, WHITE)
        screen.blit(name_s, name_s.get_rect(centerx=300, bottom=self.rect.top - 6))
        hp_s = font_s.render(f"HP: {self.hp} / {self.max_hp}", True, WHITE)
        screen.blit(hp_s, hp_s.get_rect(centerx=300, top=self.rect.bottom + 6))


# ── ex05 との違い: enemy_queue で次の敵を管理する ──
enemy_queue = [
    Enemy("ドラゴン", 200, 20, color="DARKRED", size=90),
]
enemy = Enemy("スライム", 80, 12)
party = [
    Player("勇者",    100, pg.Color("ROYALBLUE"), hp=100, attack=25),
    Player("魔法使い", 300, pg.Color("PURPLE"),    hp=70,  attack=35),
    Player("戦士",    500, pg.Color("FIREBRICK"), hp=130, attack=20),
]

messages  = ["スライムが現れた！", "SPACE: 攻撃"]
game_over = False

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and not game_over:
            messages = []

            # 生存しているプレイヤーをリストに集める
            alive = [p for p in party if p.is_alive()]

            # パーティーの攻撃
            attacker = random.choice(alive)
            dmg = random.randint(attacker.attack - 5, attacker.attack + 5)
            enemy.take_damage(dmg)   # ← Character から継承したメソッドを使う
            messages.append(f"{attacker.name}の攻撃! {dmg}ダメージ!")

            if not enemy.is_alive():
                messages.append(f"{enemy.name}をたおした!")
                # ── ex05 との違い: 次の敵がいれば交代する ──
                if enemy_queue:
                    enemy = enemy_queue.pop(0)
                    messages.append(f"{enemy.name}が現れた！")
                    messages.append("SPACE: 攻撃")
                else:
                    messages.append("全ての敵をたおした！")
                    game_over = True
            else:
                # 敵の反撃
                target = random.choice(alive)
                edm = random.randint(enemy.attack - 3, enemy.attack + 3)
                target.take_damage(edm)
                messages.append(f"{enemy.name}の反撃! {target.name}に{edm}ダメージ!")

                # 全滅チェック
                if not any(p.is_alive() for p in party):
                    messages.append("パーティーは全滅した…")
                    game_over = True
                else:
                    messages.append("SPACE: 攻撃")

    screen.fill(pg.Color("DARKSLATEGRAY"))

    enemy.draw()
    for p in party:
        p.draw()

    show_msgs = messages[-3:]
    line_h  = font_s.get_linesize()
    start_y = 400 - line_h * len(show_msgs) - 4
    for i, msg in enumerate(show_msgs):
        s = font_s.render(msg, True, pg.Color("WHITE"))
        screen.blit(s, s.get_rect(centerx=300, top=start_y + i * line_h))

    pg.display.update()
    clock.tick(60)
