class Tetrimino:
    def __init__(self, shape, color, x, y, kind=""):
        self.shape = shape
        self.color = color
        self.x     = x
        self.y     = y
        self.kind  = kind   # "I" / "O" / "T" など（ホールド復元に使用）

    def rotate_right(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

    def rotate_left(self):
        self.shape = [list(row) for row in zip(*self.shape)][::-1]

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def spawn_tetrimino(self, cols=10):
        self.x = (cols - len(self.shape[0])) // 2
        self.y = 0

    def lock(self, grid):
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    grid[self.y + row_idx][self.x + col_idx] = self.color

    def can_move(self, dx, dy, grid, rows, cols):
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
