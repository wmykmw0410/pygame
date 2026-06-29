import pygame as pg
from config import (
    ROWS, COLS, CELL_SIZE, MINI_CELL,
    WIDTH, HEIGHT, PANEL_X,
    BLACK, GRAY, WHITE,
    FONT_SIZE, FONT_SIZE_TITLE,
    GRID_BORDER_WIDTH, OVERLAY_ALPHA,
    TETORIMINO_SHAPES,
)


class Renderer:
    def __init__(self, screen):
        self.screen     = screen
        self.font       = pg.font.SysFont(None, FONT_SIZE)
        self.title_font = pg.font.SysFont(None, FONT_SIZE_TITLE)

    def draw(self, game):
        self.screen.fill(BLACK)
        self._draw_grid(game.grid)
        self._draw_ghost(game.current_piece, game.grid)
        self._draw_tetrimino(game.current_piece)
        self._draw_panel(game)

    # ── グリッド ──────────────────────────────────────────────

    def _draw_grid(self, grid):
        for row in range(ROWS):
            for col in range(COLS):
                x    = col * CELL_SIZE
                y    = row * CELL_SIZE
                rect = pg.Rect(x, y, CELL_SIZE, CELL_SIZE)
                if grid[row][col]:
                    pg.draw.rect(self.screen, grid[row][col], rect)
                pg.draw.rect(self.screen, GRAY, rect, GRID_BORDER_WIDTH)

    # ── 現在のピース ──────────────────────────────────────────

    def _draw_tetrimino(self, piece):
        for row_idx, row in enumerate(piece.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    x    = (piece.x + col_idx) * CELL_SIZE
                    y    = (piece.y + row_idx) * CELL_SIZE
                    rect = pg.Rect(x, y, CELL_SIZE, CELL_SIZE)
                    pg.draw.rect(self.screen, piece.color, rect)
                    pg.draw.rect(self.screen, GRAY, rect, GRID_BORDER_WIDTH)

    # ── ゴーストピース ────────────────────────────────────────

    def _calc_ghost_dy(self, piece, grid):
        dy = 0
        while piece.can_move(0, dy + 1, grid, ROWS, COLS):
            dy += 1
        return dy

    def _draw_ghost(self, piece, grid):
        dy = self._calc_ghost_dy(piece, grid)
        if dy == 0:
            return
        for row_idx, row in enumerate(piece.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    x    = (piece.x + col_idx) * CELL_SIZE
                    y    = (piece.y + dy + row_idx) * CELL_SIZE
                    rect = pg.Rect(x, y, CELL_SIZE, CELL_SIZE)
                    pg.draw.rect(self.screen, piece.color, rect, 2)  # 枠線のみ

    # ── ミニプレビュー（NEXT / HOLD 共通） ───────────────────

    def _draw_mini_piece(self, shape, color, origin_x, origin_y):
        for row_idx, row in enumerate(shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    x    = origin_x + col_idx * MINI_CELL
                    y    = origin_y + row_idx * MINI_CELL
                    rect = pg.Rect(x, y, MINI_CELL, MINI_CELL)
                    pg.draw.rect(self.screen, color, rect)
                    pg.draw.rect(self.screen, GRAY, rect, 1)

    # ── サイドパネル ──────────────────────────────────────────

    def _draw_panel(self, game):
        panel_cx = PANEL_X + (WIDTH - PANEL_X) // 2   # パネル中央 X = 360

        # 区切り線
        pg.draw.line(self.screen, GRAY, (PANEL_X, 0), (PANEL_X, HEIGHT), 1)

        # NEXT
        label = self.font.render("NEXT", True, WHITE)
        self.screen.blit(label, label.get_rect(centerx=panel_cx, y=20))
        shape  = game.next_piece.shape
        color  = game.next_piece.color
        origin_x = PANEL_X + (WIDTH - PANEL_X - len(shape[0]) * MINI_CELL) // 2
        self._draw_mini_piece(shape, color, origin_x, 50)

        # HOLD
        label = self.font.render("HOLD", True, WHITE)
        self.screen.blit(label, label.get_rect(centerx=panel_cx, y=170))
        if game.hold_kind is not None:
            shape  = TETORIMINO_SHAPES[game.hold_kind]["shape"]
            color  = TETORIMINO_SHAPES[game.hold_kind]["color"]
            if not game.can_hold:
                color = GRAY   # ホールド済みは暗くする
            origin_x = PANEL_X + (WIDTH - PANEL_X - len(shape[0]) * MINI_CELL) // 2
            self._draw_mini_piece(shape, color, origin_x, 200)
        else:
            hint = self.font.render("H key", True, GRAY)
            self.screen.blit(hint, hint.get_rect(centerx=panel_cx, y=205))

        # SCORE
        label = self.font.render("SCORE", True, WHITE)
        self.screen.blit(label, label.get_rect(centerx=panel_cx, y=320))
        val = self.font.render(str(game.score), True, WHITE)
        self.screen.blit(val, val.get_rect(centerx=panel_cx, y=350))

        # LINES
        label = self.font.render("LINES", True, WHITE)
        self.screen.blit(label, label.get_rect(centerx=panel_cx, y=400))
        val = self.font.render(str(game.total_lines), True, WHITE)
        self.screen.blit(val, val.get_rect(centerx=panel_cx, y=430))

    # ── オーバーレイ（スタート / ゲームオーバー） ─────────────

    def draw_overlay(self, title, subtitle):
        overlay = pg.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(OVERLAY_ALPHA)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))

        cx         = WIDTH // 2
        title_surf = self.title_font.render(title, True, WHITE)
        sub_surf   = self.font.render(subtitle, True, GRAY)
        self.screen.blit(title_surf, title_surf.get_rect(center=(cx, HEIGHT // 2 - 30)))
        self.screen.blit(sub_surf,   sub_surf.get_rect(center=(cx, HEIGHT // 2 + 20)))
