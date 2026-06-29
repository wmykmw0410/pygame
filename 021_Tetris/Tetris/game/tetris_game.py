from __future__ import annotations

import random
import pygame as pg
from config import (
    ROWS, COLS, TETORIMINO_SHAPES,
    FALL_INTERVAL_INIT, FALL_INTERVAL_MIN,
    FALL_SPEED_STEP_LINES, FALL_SPEED_STEP_MS,
)
from game.tetrimino import Tetrimino, Grid


class TetrisGame:
    """ゲーム状態・ロジック・入力処理を管理する。"""

    def __init__(self) -> None:
        self.grid: Grid = []
        for _ in range(ROWS):
            row = []
            for _ in range(COLS):
                row.append(0)
            self.grid.append(row)
        self.current_piece: Tetrimino = self._spawn_piece()
        self.total_lines: int = 0

        self.fall_interval: int = FALL_INTERVAL_INIT
        self.min_interval: int = FALL_INTERVAL_MIN
        self.last_fall: int = pg.time.get_ticks()

        self.game_over: bool = False

    def _spawn_piece(self) -> Tetrimino:
        """ランダムなテトリミノを生成してスポーン位置に配置する。"""
        mino_data = random.choice(list(TETORIMINO_SHAPES.values()))
        shape_copy = []
        for row in mino_data["shape"]:
            shape_copy.append(row[:])
        piece = Tetrimino(
            shape=shape_copy,
            color=mino_data["color"],
            x=0,
            y=0
        )
        piece.spawn_tetrimino(COLS)
        return piece

    def _clear_lines(self) -> None:
        """揃った行を消去し、スコアと落下速度を更新する。"""
        new_grid = []
        for row in self.grid:
            has_empty = False
            for cell in row:
                if cell == 0:
                    has_empty = True
                    break
            if has_empty:
                new_grid.append(row)
        cleared = ROWS - len(new_grid)

        empty_rows = []
        for _ in range(cleared):
            row = []
            for _ in range(COLS):
                row.append(0)
            empty_rows.append(row)
        self.grid = empty_rows + new_grid
        self.total_lines += cleared
        self.fall_interval = max(
            self.min_interval,
            FALL_INTERVAL_INIT - (self.total_lines // FALL_SPEED_STEP_LINES) * FALL_SPEED_STEP_MS,
        )

    def update(self) -> None:
        """落下タイマーに基づいてピースを更新する。"""
        now = pg.time.get_ticks()
        if now - self.last_fall >= self.fall_interval:
            if self.current_piece.can_move(0, 1, self.grid, ROWS, COLS):
                self.current_piece.move(0, 1)
            else:
                self.current_piece.lock(self.grid)
                self._clear_lines()
                self.current_piece = self._spawn_piece()
                if not self.current_piece.can_move(0, 0, self.grid, ROWS, COLS):
                    self.game_over = True
            self.last_fall = now

    def handle_input(self, event: pg.event.Event) -> None:
        """キー入力に応じてピースを操作する。

        Args:
            event: 処理対象の pygame キーボードイベント。
        """
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
