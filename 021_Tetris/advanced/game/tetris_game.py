import random
import pygame as pg
from config import (
    ROWS, COLS, TETRIMINO_SHAPES,
    FALL_INTERVAL_INIT, FALL_INTERVAL_MIN,
    FALL_SPEED_STEP_LINES, FALL_SPEED_STEP_MS,
    SCORE_TABLE,
)
from game.tetrimino import Tetrimino


class TetrisGame:
    def __init__(self):
        self.grid = []
        for _ in range(ROWS):
            self.grid.append([0] * COLS)

        self.next_piece    = self._spawn_piece()
        self.current_piece = self._pop_next()
        self.hold_kind     = None   # ホールド中のミノ種類（"I" / "O" 等、None = 未ホールド）
        self.can_hold      = True   # 同じピース中に2回ホールドできないようにする

        self.total_lines   = 0
        self.score         = 0

        self.fall_interval = FALL_INTERVAL_INIT
        self.min_interval  = FALL_INTERVAL_MIN
        self.last_fall     = pg.time.get_ticks()
        self.game_over     = False

    def _spawn_piece(self):
        kind = random.choice(list(TETRIMINO_SHAPES.keys()))
        data = TETRIMINO_SHAPES[kind]
        shape_copy = []
        for row in data["shape"]:
            shape_copy.append(row[:])
        piece = Tetrimino(
            shape=shape_copy,
            color=data["color"],
            x=0,
            y=0,
            kind=kind,
        )
        piece.spawn_tetrimino(COLS)
        return piece

    def _pop_next(self):
        piece           = self.next_piece
        self.next_piece = self._spawn_piece()
        return piece

    def _make_piece(self, kind):
        data  = TETRIMINO_SHAPES[kind]
        shape_copy = []
        for row in data["shape"]:
            shape_copy.append(row[:])
        piece = Tetrimino(
            shape=shape_copy,
            color=data["color"],
            x=0,
            y=0,
            kind=kind,
        )
        piece.spawn_tetrimino(COLS)
        return piece

    def _do_hold(self):
        if not self.can_hold:
            return
        if self.hold_kind is None:
            self.hold_kind     = self.current_piece.kind
            self.current_piece = self._pop_next()
        else:
            old_hold       = self.hold_kind
            self.hold_kind = self.current_piece.kind
            self.current_piece = self._make_piece(old_hold)
        self.can_hold = False
        if not self.current_piece.can_move(0, 0, self.grid, ROWS, COLS):
            self.game_over = True

    def _clear_lines(self):
        new_grid = []
        cleared  = 0
        for row in self.grid:
            has_empty = False
            for cell in row:
                if cell == 0:
                    has_empty = True
                    break
            if has_empty:
                new_grid.append(row)
            else:
                cleared += 1

        for _ in range(cleared):
            new_grid.insert(0, [0] * COLS)
        self.grid = new_grid

        self.total_lines += cleared

        if cleared > 0:
            idx = cleared
            if idx >= len(SCORE_TABLE):
                idx = len(SCORE_TABLE) - 1
            self.score += SCORE_TABLE[idx]

        new_interval = FALL_INTERVAL_INIT - (self.total_lines // FALL_SPEED_STEP_LINES) * FALL_SPEED_STEP_MS
        if new_interval < self.min_interval:
            new_interval = self.min_interval
        self.fall_interval = new_interval

    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_fall >= self.fall_interval:
            if self.current_piece.can_move(0, 1, self.grid, ROWS, COLS):
                self.current_piece.move(0, 1)
            else:
                self.current_piece.lock(self.grid)
                self._clear_lines()
                self.can_hold      = True
                self.current_piece = self._pop_next()
                if not self.current_piece.can_move(0, 0, self.grid, ROWS, COLS):
                    self.game_over = True
            self.last_fall = now

    def handle_input(self, event):
        piece = self.current_piece

        if event.key == pg.K_LEFT:
            if piece.can_move(-1, 0, self.grid, ROWS, COLS):
                piece.move(-1, 0)

        elif event.key == pg.K_RIGHT:
            if piece.can_move(1, 0, self.grid, ROWS, COLS):
                piece.move(1, 0)

        elif event.key == pg.K_DOWN:
            if piece.can_move(0, 1, self.grid, ROWS, COLS):
                piece.move(0, 1)

        elif event.key == pg.K_UP:
            while piece.can_move(0, 1, self.grid, ROWS, COLS):
                piece.move(0, 1)

        elif event.key == pg.K_a:
            original_shape = []
            for row in piece.shape:
                original_shape.append(row[:])
            piece.rotate_left()
            if not piece.can_move(0, 0, self.grid, ROWS, COLS):
                piece.shape = original_shape

        elif event.key == pg.K_s:
            original_shape = []
            for row in piece.shape:
                original_shape.append(row[:])
            piece.rotate_right()
            if not piece.can_move(0, 0, self.grid, ROWS, COLS):
                piece.shape = original_shape

        elif event.key == pg.K_h:
            self._do_hold()
