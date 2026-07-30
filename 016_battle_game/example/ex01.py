# ex01: CLI版（015_class Q3）を pygame化する
# → Character・Enemy の継承構造はそのまま、print() の代わりに画面に描画する
# → 描画のため rect・color を Character に追加している（Q3からの変更点）

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


# ── 015_class の Q3 との違い: 画面に描画するため rect・color を追加した ──
class Character():
    def __init__(self, name, attack_power, rect, color):
        self.name         = name
        self.hp           = 100
        self.attack_power = attack_power
        self.rect         = rect
        self.color        = color

    def attack(self, target):
        target.hp -= self.attack_power
        return f"{self.name}の攻撃! {target.name}に{self.attack_power}ダメージ!"

    def is_alive(self):
        return self.hp > 0


class Enemy(Character):
    def __init__(self, name, attack_power, rect, color):
        super().__init__(name, attack_power, rect, color)
        self.hp = 150

    def attack(self, target):
        dmg = int(self.attack_power * 1.5)
        target.hp -= dmg
        return f"{self.name}の攻撃! {target.name}に{dmg}ダメージ!"


player_rect = pg.Rect(270, 230, 60, 60)
enemy_rect  = pg.Rect(0, 40, 70, 70)
enemy_rect.centerx = 300

player = Character("勇者", attack_power=30, rect=player_rect, color=pg.Color("ROYALBLUE"))
enemy  = Enemy("スライム", attack_power=15, rect=enemy_rect, color=pg.Color("DARKGREEN"))

message     = "SPACE: 攻撃"
sub_message = ""   # 1ターンで player と enemy 両方が攻撃するので、2行に分けて表示する
game_over   = False

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and not game_over:
            sub_message = player.attack(enemy)
            if not enemy.is_alive():
                message     = f"{enemy.name}をたおした! {player.name}の勝利!"
                sub_message = ""
                game_over   = True
            else:
                message = enemy.attack(player)
                if not player.is_alive():
                    message     = f"{player.name}は倒れた… {enemy.name}の勝利!"
                    sub_message = ""
                    game_over   = True

    screen.fill(pg.Color("DARKSLATEGRAY"))

    if player.is_alive():
        color = player.color
    else:
        color = pg.Color("GRAY")
    pg.draw.rect(screen, color, player.rect)
    player_s = font.render(f"{player.name}  HP:{player.hp}", True, WHITE)
    screen.blit(player_s, player_s.get_rect(centerx=player.rect.centerx, bottom=player.rect.top - 6))

    if enemy.is_alive():
        color = enemy.color
    else:
        color = pg.Color("GRAY")
    pg.draw.rect(screen, color, enemy.rect)
    enemy_s = font.render(f"{enemy.name}  HP:{enemy.hp}", True, WHITE)
    screen.blit(enemy_s, enemy_s.get_rect(centerx=enemy.rect.centerx, bottom=enemy.rect.top - 6))

    msg = font_s.render(message, True, WHITE)
    msg_rect = msg.get_rect(centerx=300, top=345)
    screen.blit(msg, msg_rect)
    sub_s = font_s.render(sub_message, True, WHITE)
    screen.blit(sub_s, sub_s.get_rect(centerx=300, bottom=msg_rect.top - 2))

    pg.display.update()
    clock.tick(60)
