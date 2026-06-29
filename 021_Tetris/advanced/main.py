import pygame as pg
from config import WIDTH, HEIGHT, FPS
from game.tetris_game import TetrisGame
from game.tetris_renderer import Renderer

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Tetris Advanced")

START     = "start"
PLAYING   = "playing"
GAME_OVER = "game_over"


def main():
    game     = TetrisGame()
    renderer = Renderer(screen)
    state    = START
    clock    = pg.time.Clock()
    running  = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    if state == START:
                        state = PLAYING
                    elif state == GAME_OVER:
                        game  = TetrisGame()
                        state = PLAYING
                elif state == PLAYING:
                    game.handle_input(event)

        if state == PLAYING:
            game.update()
            if game.game_over:
                state = GAME_OVER

        renderer.draw(game)

        if state == START:
            renderer.draw_overlay("TETRIS", "Press SPACE to Start")
        elif state == GAME_OVER:
            renderer.draw_overlay(
                "GAME OVER",
                f"Score:{game.score}  Lines:{game.total_lines}  SPACE:Restart",
            )

        pg.display.update()
        clock.tick(FPS)

    pg.quit()


if __name__ == "__main__":
    main()
