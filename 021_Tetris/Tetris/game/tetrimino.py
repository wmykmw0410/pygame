from __future__ import annotations

Color = tuple[int, int, int]
Shape = list[list[int]]
Grid = list[list[int | Color]]


class Tetrimino:
    """テトリミノ1ピースの状態と操作を管理する。"""

    def __init__(self, shape: Shape, color: Color, x: int, y: int) -> None:
        """テトリミノを初期化する。

        Args:
            shape: ピースの形状を表す2次元リスト。
            color: ピースの描画色 (R, G, B)。
            x: グリッド上の初期列位置。
            y: グリッド上の初期行位置。
        """
        self.shape = shape
        self.color = color
        self.x = x
        self.y = y

    def rotate_right(self) -> None:
        """時計回りに90度回転する。"""
        rotated = []
        for row in zip(*self.shape[::-1]):
            rotated.append(list(row))
        self.shape = rotated

    def rotate_left(self) -> None:
        """反時計回りに90度回転する。"""
        rotated = []
        for row in zip(*self.shape):
            rotated.append(list(row))
        self.shape = rotated[::-1]

    def move(self, dx: int, dy: int) -> None:
        """ピースを (dx, dy) だけ移動する。

        Args:
            dx: 水平方向の移動量（正: 右、負: 左）。
            dy: 垂直方向の移動量（正: 下、負: 上）。
        """
        self.x += dx
        self.y += dy

    def spawn_tetrimino(self, cols: int = 10) -> None:
        """グリッド上部中央にスポーン位置を設定する。

        Args:
            cols: グリッドの列数。デフォルトは 10。
        """
        self.x = (cols - len(self.shape[0])) // 2
        self.y = 0

    def lock(self, grid: Grid) -> None:
        """ピースをグリッドに固定する。

        Args:
            grid: ピースのセルを書き込む対象グリッド。
        """
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    grid[self.y + row_idx][self.x + col_idx] = self.color

    def can_move(self, dx: int, dy: int, grid: Grid, rows: int, cols: int) -> bool:
        """(dx, dy) 方向への移動が可能かどうかを返す。

        Args:
            dx: 水平方向の移動量。
            dy: 垂直方向の移動量。
            grid: 衝突判定に使用するグリッド。
            rows: グリッドの行数。
            cols: グリッドの列数。

        Returns:
            移動可能なら True、壁・床・他ピースと衝突するなら False。
        """
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    new_x = self.x + col_idx + dx
                    new_y = self.y + row_idx + dy

                    if new_x < 0 or new_x >= cols:
                        return False
                    if new_y >= rows:
                        return False
                    if new_y >= 0 and grid[new_y][new_x]:
                        return False
        return True
