from __future__ import annotations

from typing import TYPE_CHECKING
import pygame as pg
from config import (
    ROWS, COLS, CELL_SIZE, WIDTH, HEIGHT, BLACK, GRAY, WHITE,
    FONT_SIZE, FONT_SIZE_TITLE,
    GRID_BORDER_WIDTH, SCORE_POS, OVERLAY_ALPHA,
    OVERLAY_TITLE_OFFSET_Y, OVERLAY_SUBTITLE_OFFSET_Y,
)
from game.tetrimino import Tetrimino, Grid

if TYPE_CHECKING:
    from game.tetris_game import TetrisGame


class Renderer:
    """pygame の画面への描画を担当する。"""

    def __init__(self, screen: pg.Surface) -> None:
        """レンダラーを初期化する。

        Args:
            screen: 描画対象の pygame サーフェス。
        """
        self.screen = screen

        self.font = pg.font.SysFont(None, FONT_SIZE)
        self.title_font = pg.font.SysFont(None, FONT_SIZE_TITLE)

    def draw(self, game: TetrisGame) -> None:
        """1フレーム分の画面全体を描画する。

        Args:
            game: 描画するゲーム状態を持つ TetrisGame インスタンス。
        """
        self.screen.fill(BLACK)
        self._draw_grid(game.grid)
        self._draw_tetrimino(game.current_piece)
        self._draw_score(game.total_lines)

    def _draw_grid(self, grid: Grid) -> None:
        """グリッドと固定済みブロックを描画する。

        Args:
            grid: 描画するグリッドデータ。
        """
        for row in range(ROWS):
            for col in range(COLS):
                x = col * CELL_SIZE
                y = row * CELL_SIZE
                rect = pg.Rect(x, y, CELL_SIZE, CELL_SIZE)

                if grid[row][col]:
                    pg.draw.rect(self.screen, grid[row][col], rect)
                pg.draw.rect(self.screen, GRAY, rect, GRID_BORDER_WIDTH)

    def _draw_tetrimino(self, piece: Tetrimino) -> None:
        """現在操作中のピースを描画する。

        Args:
            piece: 描画するテトリミノ。
        """
        for row_idx, row in enumerate(piece.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    x = (piece.x + col_idx) * CELL_SIZE
                    y = (piece.y + row_idx) * CELL_SIZE
                    rect = pg.Rect(x, y, CELL_SIZE, CELL_SIZE)

                    pg.draw.rect(self.screen, piece.color, rect)
                    pg.draw.rect(self.screen, GRAY, rect, GRID_BORDER_WIDTH)

    def _draw_score(self, total_lines: int) -> None:
        """消去済みライン数を画面左上に描画する。

        Args:
            total_lines: 現在の消去済みライン数。
        """
        text = self.font.render(f"Lines: {total_lines}", True, WHITE)
        self.screen.blit(text, SCORE_POS)

    def draw_overlay(self, title: str, subtitle: str) -> None:
        """半透明オーバーレイにタイトルとサブテキストを中央表示する。

        Args:
            title: 大きく表示するタイトル文字列。
            subtitle: タイトル下に表示するサブテキスト。
        """
        overlay = pg.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(OVERLAY_ALPHA)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))

        cx = WIDTH // 2
        title_surf = self.title_font.render(title, True, WHITE)
        sub_surf = self.font.render(subtitle, True, GRAY)

        self.screen.blit(title_surf, title_surf.get_rect(center=(cx, HEIGHT // 2 - OVERLAY_TITLE_OFFSET_Y)))
        self.screen.blit(sub_surf, sub_surf.get_rect(center=(cx, HEIGHT // 2 + OVERLAY_SUBTITLE_OFFSET_Y)))
