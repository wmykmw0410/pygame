from pathlib import Path
import pygame as pg

BASE_DIR = Path(__file__).resolve().parent
IMG_DIR  = BASE_DIR / "images"

RESULT_FONT_SIZE = 50
RESULT_MSG_POS   = (120, 380)
RESULT_IMG_POS   = (50, 200)

class ResultScene():
    def __init__(self, game) -> None:
        font = pg.font.Font(None, RESULT_FONT_SIZE)
        self.game      = game
        self.msg       = font.render("Press SPACE to replay.", True, pg.Color("WHITE"))
        self.gameover  = pg.image.load(IMG_DIR / "gameover.png")
        self.gameclear = pg.image.load(IMG_DIR / "gameclear.png")

    def update(self):
        key = pg.key.get_pressed()
        if key[pg.K_SPACE]:
            self.game.reset()

    def draw(self, screen):
        screen.blit(self.msg, RESULT_MSG_POS)
        if self.game.is_cleared:
            screen.blit(self.gameclear, RESULT_IMG_POS)
        else:
            screen.blit(self.gameover, RESULT_IMG_POS)
