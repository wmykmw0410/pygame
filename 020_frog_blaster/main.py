import pygame as pg
from game import GameManager, ResultScene

WIDTH, HEIGHT = 600, 650
FPS = 60

def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Frog Blaster")
    clock = pg.time.Clock()

    game   = GameManager()
    result = ResultScene(game)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill(pg.Color("NAVY"))

        if game.is_playing:
            game.update()
        else:
            result.update()

        game.draw(screen)
        if not game.is_playing:
            result.draw(screen)

        pg.display.update()
        clock.tick(FPS)

    pg.quit()

if __name__ == "__main__":
    main()
