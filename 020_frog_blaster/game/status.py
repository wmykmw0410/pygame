import pygame as pg

WIDTH = 600

STATUS_FONT_SIZE    = 32
STATUS_BAR_HEIGHT   = 36
STATUS_BG_ALPHA     = 128
DISTANCE_PER_TICK   = 2
STATUS_DISTANCE_POS = (20, 10)
STATUS_SCORE_POS    = (380, 10)

class Observer:
    def update(self, ntype):
        pass


class Status(Observer):
    def __init__(self) -> None:
        self.font  = pg.font.Font(None, STATUS_FONT_SIZE)
        self.board = pg.Surface((WIDTH, STATUS_BAR_HEIGHT), pg.SRCALPHA)
        self.reset()

    def reset(self):
        self.distance = 0
        self.score    = 0

    def update(self, ntype):
        if ntype == "distance":
            self.distance += DISTANCE_PER_TICK
        if ntype == "score":
            self.score += 1

    def draw(self, screen):
        pg.draw.rect(self.board, (0, 0, 0, STATUS_BG_ALPHA), pg.Rect(0, 0, WIDTH, STATUS_BAR_HEIGHT))
        screen.blit(self.board, (0, 0))
        info1 = self.font.render(f"DISTANCE : {self.distance}", True, pg.Color("WHITE"))
        info2 = self.font.render(f"SCORE : {self.score}",      True, pg.Color("WHITE"))
        screen.blit(info1, STATUS_DISTANCE_POS)
        screen.blit(info2, STATUS_SCORE_POS)
