# ex02: パーティー化する（勇者1人 → 3人のパーティー、バトルゲーム完成）
# → ex01 の Character 共通の attack() をやめ、take_damage() / draw() / max_hp を追加する
# → Player・Enemy それぞれの attack() でダメージ計算にランダム幅を持たせ、Enemy は複数のPlayerを相手にする
# → メッセージは messages リストで管理し、直近3件を画面下部に表示する

import pygame as pg
import sys
import random
from pathlib import Path

pg.init()
screen = pg.display.set_mode((600, 400))
pg.display.set_caption("ex02: バトルゲーム（完成）")
clock  = pg.time.Clock()
FONT   = Path(__file__).resolve().parent.parent / "fonts" / "NotoSansCJKjp-Regular.otf"
font   = pg.font.Font(FONT, 24)
font_s = pg.font.Font(FONT, 20)
WHITE  = pg.Color("WHITE")


# ── ex01 との違い: Character 共通の attack() をやめ、take_damage() / draw() / max_hp を追加した ──
class Character():
    def __init__(self, name, hp, rect, color):
        self.name   = name
        self.hp     = hp
        self.max_hp = hp
        self.rect   = rect
        self.color  = color

    def is_alive(self):
        return self.hp > 0

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
        hp_s = font_s.render(f"HP: {self.hp} / {self.max_hp}", True, WHITE)
        screen.blit(hp_s, hp_s.get_rect(centerx=self.rect.centerx, top=self.rect.bottom + 6))


class Player(Character):
    def __init__(self, name, cx, color, hp, attack_power):
        rect = pg.Rect(cx - 30, 200, 60, 60)
        super().__init__(name, hp, rect, color)   # ← Character の __init__ を呼ぶ
        self.attack_power = attack_power

    # is_alive() / take_damage() / draw() は Character から継承

    def attack(self, target):
        dmg = random.randint(self.attack_power - 5, self.attack_power + 5)
        target.take_damage(dmg)   # ← Character から継承したメソッドを使う
        return f"{self.name}の攻撃! {dmg}ダメージ!"


# ── ex01 との違い: attack_power / attack() を追加して反撃できるようにした ──
class Enemy(Character):
    def __init__(self, name, hp, attack_power):
        rect = pg.Rect(0, 40, 70, 70)
        rect.centerx = 300
        super().__init__(name, hp, rect, pg.Color("DARKGREEN"))   # ← Character の __init__ を呼ぶ
        self.attack_power = attack_power

    # is_alive() / take_damage() / draw() は Character から継承

    def attack(self, target):
        dmg = random.randint(self.attack_power - 3, self.attack_power + 3)
        target.take_damage(dmg)
        return f"{self.name}の反撃! {target.name}に{dmg}ダメージ!"


enemy = Enemy("スライム", 80, 12)
party = [
    Player("勇者",    100, pg.Color("ROYALBLUE"), hp=100, attack_power=25),
    Player("魔法使い", 300, pg.Color("PURPLE"),    hp=70,  attack_power=35),
    Player("戦士",    500, pg.Color("FIREBRICK"), hp=130, attack_power=20),
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
            alive = []
            for p in party:
                if p.is_alive():
                    alive.append(p)

            # パーティーの攻撃
            attacker = random.choice(alive)
            messages.append(attacker.attack(enemy))

            if not enemy.is_alive():
                messages.append("スライムをたおした!")
                game_over = True
            else:
                # 敵の反撃
                target = random.choice(alive)
                messages.append(enemy.attack(target))

                # 全滅チェック（enemy の反撃で全員倒れたら、次の alive が空になってしまうため）
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
