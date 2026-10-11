# ex01: CLI版（15_class Q3）を pygame化する
# → Character・Enemy の継承構造はそのまま、print() の代わりに画面に描画する
# → 描画のため rect・image を Character に追加している（Q3からの変更点）

from pathlib import Path
import pygame as pg
import sys

pg.init()
WIDTH, HEIGHT = 600, 400
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("ex01: CLI版をpygame化する")
clock  = pg.time.Clock()
FONT   = Path(__file__).resolve().parent.parent / "fonts" / "NotoSansCJKjp-Regular.otf"
font   = pg.font.Font(FONT, 24)
font_s = pg.font.Font(FONT, 20)
WHITE  = pg.Color("WHITE")

IMG_DIR   = Path(__file__).resolve().parent.parent / "images"
hero_img  = pg.image.load(IMG_DIR / "yuusya_game.png").convert_alpha()
slime_img = pg.image.load(IMG_DIR / "fantasy_game_character_slime.png").convert_alpha()


# ── 15_class の Q3 との違い: 画面に描画するため rect・image を追加した ──
class Character():
    def __init__(self, name, attack_power, rect, image):
        self.name         = name
        self.hp           = 100
        self.attack_power = attack_power
        self.rect         = rect
        # 画像の縦横比を保ったまま rect に収まるサイズへ縮小する（画像が正方形とは限らないため）
        iw, ih = image.get_size()
        scale  = min(rect.w / iw, rect.h / ih)
        self.image = pg.transform.smoothscale(image, (int(iw * scale), int(ih * scale)))

    def attack(self, target):
        target.hp -= self.attack_power
        return f"{self.name}の攻撃! {target.name}に{self.attack_power}ダメージ!"

    def is_alive(self):
        return self.hp > 0


class Enemy(Character):
    def __init__(self, name, attack_power, rect, image):
        super().__init__(name, attack_power, rect, image)
        self.hp = 150

    def attack(self, target):
        dmg = int(self.attack_power * 1.5)
        target.hp -= dmg
        return f"{self.name}の攻撃! {target.name}に{dmg}ダメージ!"


PLAYER_SIZE = 60
ENEMY_SIZE  = 70
player_rect = pg.Rect(270, 230, PLAYER_SIZE, PLAYER_SIZE)
enemy_rect  = pg.Rect(0, 40, ENEMY_SIZE, ENEMY_SIZE)
enemy_rect.centerx = WIDTH // 2

player = Character("勇者", attack_power=30, rect=player_rect, image=hero_img)
enemy  = Enemy("スライム", attack_power=15, rect=enemy_rect, image=slime_img)

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
        screen.blit(player.image, player.image.get_rect(center=player.rect.center))
    else:
        screen.blit(pg.transform.grayscale(player.image), player.image.get_rect(center=player.rect.center))
    player_s = font.render(f"{player.name}  HP:{player.hp}", True, WHITE)
    screen.blit(player_s, player_s.get_rect(centerx=player.rect.centerx, bottom=player.rect.top - 6))

    if enemy.is_alive():
        screen.blit(enemy.image, enemy.image.get_rect(center=enemy.rect.center))
    else:
        screen.blit(pg.transform.grayscale(enemy.image), enemy.image.get_rect(center=enemy.rect.center))
    enemy_s = font.render(f"{enemy.name}  HP:{enemy.hp}", True, WHITE)
    screen.blit(enemy_s, enemy_s.get_rect(centerx=enemy.rect.centerx, bottom=enemy.rect.top - 6))

    msg = font_s.render(message, True, WHITE)
    msg_rect = msg.get_rect(centerx=WIDTH // 2, top=345)
    screen.blit(msg, msg_rect)
    sub_s = font_s.render(sub_message, True, WHITE)
    screen.blit(sub_s, sub_s.get_rect(centerx=WIDTH // 2, bottom=msg_rect.top - 2))

    pg.display.update()
    clock.tick(FPS)
