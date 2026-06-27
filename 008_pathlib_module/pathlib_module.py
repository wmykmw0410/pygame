"""
pathlibモジュールの使用方法
"""
from pathlib import Path
import pygame as pg
import sys

pg.init()

CURRENT_DIR = Path(__file__)
BASE_DIR = Path(__file__).resolve().parent

IMG_DIR = BASE_DIR / "images"

print("現在のパス : ", CURRENT_DIR)
print("親ディレクトリのパス : ", BASE_DIR)

WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Image Display Sample")
clock = pg.time.Clock()

player_img = pg.image.load(IMG_DIR / "car.png")
player_rect = player_img.get_rect(topleft=(WIDTH // 2, HEIGHT // 2))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill("WHITE")
    screen.blit(player_img, player_rect)
    pg.display.update()
    clock.tick(60)
