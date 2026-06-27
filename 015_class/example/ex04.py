# ex04: 関数だけで書いてみる
# → プレイヤーが増えると変数と関数がどんどん増えていく問題を確認する

import pygame as pg
import sys
from pathlib import Path

pg.init()
screen = pg.display.set_mode((600, 400))
pg.display.set_caption("ex04: 関数で書く")
clock  = pg.time.Clock()
FONT   = Path(__file__).resolve().parent.parent / "fonts" / "NotoSansCJKjp-Regular.otf"
font   = pg.font.Font(FONT, 24)
font_s = pg.font.Font(FONT, 20)
WHITE  = pg.Color("WHITE")

# プレイヤー3人分のデータを変数で管理
name1, hp1, color1 = "勇者",    100, pg.Color("ROYALBLUE")
name2, hp2, color2 = "魔法使い",  70, pg.Color("PURPLE")
name3, hp3, color3 = "戦士",    130, pg.Color("FIREBRICK")


def draw_player(name, cx, color, hp):
    rect = pg.Rect(cx - 30, 200, 60, 60)
    pg.draw.rect(screen, color, rect)
    name_s = font.render(name, True, WHITE)
    screen.blit(name_s, name_s.get_rect(centerx=cx, bottom=194))
    hp_s = font_s.render(f"HP: {hp}", True, WHITE)
    screen.blit(hp_s, hp_s.get_rect(centerx=cx, top=266))


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            hp1 -= 10
            hp2 -= 10
            hp3 -= 10

    screen.fill(pg.Color("DARKSLATEGRAY"))
    draw_player(name1, 100, color1, hp1)
    draw_player(name2, 300, color2, hp2)
    draw_player(name3, 500, color3, hp3)

    msg = font_s.render("SPACE: 全員に 10 ダメージ", True, pg.Color("LIGHTGRAY"))
    screen.blit(msg, msg.get_rect(centerx=300, top=340))

    pg.display.update()
    clock.tick(60)
