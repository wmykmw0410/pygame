from pathlib import Path
import pygame as pg

BASE_DIR = Path(__file__).resolve().parent
IMG_DIR  = BASE_DIR / "images"

class ResultScene():
    def __init__(self, game) -> None:
        font = pg.font.Font(None, 50)
        self._game      = game
        self._msg       = font.render("Press SPACE to replay.", True, pg.Color("WHITE"))
        self._gameover  = pg.image.load(IMG_DIR / "gameover.png")
        self._gameclear = pg.image.load(IMG_DIR / "gameclear.png")

    def update(self):
        key = pg.key.get_pressed()
        if key[pg.K_SPACE]:
            self._game.reset()

    def draw(self, screen):
        screen.blit(self._msg, (120, 380))
        if self._game.is_cleared:
            screen.blit(self._gameclear, (50, 200))
        else:
            screen.blit(self._gameover, (50, 200))
