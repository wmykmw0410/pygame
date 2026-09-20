from pathlib import Path
import pygame as pg

BASE_DIR = Path(__file__).resolve().parent
IMG_DIR  = BASE_DIR / "images"

WIDTH = 600

PLAYER_SIZE   = 50
PLAYER_START  = (250, 550)
PLAYER_SPEED  = 10
PLAYER_MAX_HP = 150

HP_BAR_WIDTH  = 4
HP_BAR_HEIGHT = 20
HP_BAR_OFFSET = 20

ANIM_FRAME_DELAY = 5
DAMAGE_DURATION  = 20

class PlayerState():
    def __init__(self, player) -> None:
        self.player = player
        self.image  = None

    def update(self):
        pass


class IdleState(PlayerState):
    def __init__(self, player) -> None:
        super().__init__(player)
        self.image = pg.image.load(IMG_DIR / "kaeru1.png")

    def update(self):
        key = pg.key.get_pressed()
        if key[pg.K_LEFT] or key[pg.K_RIGHT]:
            return MovingState(self.player)
        return self


class MovingState(PlayerState):
    def __init__(self, player) -> None:
        super().__init__(player)
        self.images = [
            pg.image.load(IMG_DIR / "kaeru1.png"),
            pg.image.load(IMG_DIR / "kaeru2.png"),
            pg.image.load(IMG_DIR / "kaeru3.png"),
            pg.image.load(IMG_DIR / "kaeru4.png"),
        ]
        self.cnt   = 0
        self.image = self.images[0]

    def update(self):
        self.cnt  += 1
        self.image = self.images[self.cnt // ANIM_FRAME_DELAY % len(self.images)]
        key = pg.key.get_pressed()
        if not (key[pg.K_LEFT] or key[pg.K_RIGHT]):
            return IdleState(self.player)
        return self


class DamageState(PlayerState):
    def __init__(self, player) -> None:
        super().__init__(player)
        self.images  = [
            pg.image.load(IMG_DIR / "kaeru5.png"),
            pg.image.load(IMG_DIR / "kaeru6.png"),
        ]
        self.cnt     = 0
        self.image   = self.images[0]
        self.timeout = DAMAGE_DURATION

    def update(self):
        self.cnt    += 1
        self.image   = self.images[self.cnt // ANIM_FRAME_DELAY % len(self.images)]
        self.timeout -= 1
        if self.timeout < 0:
            return IdleState(self.player)
        return self


class Player():
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self.state = IdleState(self)
        self.rect  = pg.Rect(*PLAYER_START, PLAYER_SIZE, PLAYER_SIZE)
        self.speed = PLAYER_SPEED
        self.maxhp = PLAYER_MAX_HP
        self.hp    = PLAYER_MAX_HP

    def update(self):
        self.state = self.state.update()
        key = pg.key.get_pressed()
        vx = 0
        if key[pg.K_RIGHT]:
            vx =  self.speed
        if key[pg.K_LEFT]:
            vx = -self.speed
        if self.rect.x + vx < 0 or self.rect.x + vx > WIDTH - PLAYER_SIZE:
            vx = 0
        self.rect.x += vx

    def draw(self, screen):
        screen.blit(self.state.image, self.rect)
        rect1 = pg.Rect(self.rect.x, self.rect.y - HP_BAR_OFFSET, HP_BAR_WIDTH, HP_BAR_HEIGHT)
        h     = (self.hp / self.maxhp) * HP_BAR_HEIGHT
        rect2 = pg.Rect(self.rect.x, self.rect.y - h, HP_BAR_WIDTH, h)
        pg.draw.rect(screen, pg.Color("RED"),   rect1)
        pg.draw.rect(screen, pg.Color("GREEN"), rect2)

    def damage(self):
        self.state = DamageState(self)
