import pygame as pg

class Observer:
    def update(self, ntype):
        pass


class Status(Observer):
    def __init__(self) -> None:
        self.font  = pg.font.Font(None, 32)
        self.board = pg.Surface((600, 36), pg.SRCALPHA)
        self.reset()

    def reset(self):
        self.distance = 0
        self.score    = 0

    def update(self, ntype):
        if ntype == "distance":
            self.distance += 2
        if ntype == "score":
            self.score += 1

    def draw(self, screen):
        pg.draw.rect(self.board, (0, 0, 0, 128), pg.Rect(0, 0, 600, 36))
        screen.blit(self.board, (0, 0))
        info1 = self.font.render(f"DISTANCE : {self.distance}", True, pg.Color("WHITE"))
        info2 = self.font.render(f"SCORE : {self.score}",      True, pg.Color("WHITE"))
        screen.blit(info1, (20,  10))
        screen.blit(info2, (380, 10))
