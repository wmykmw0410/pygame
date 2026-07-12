WIDTH, HEIGHT = 300, 600
FPS = 60

ROWS = 20
COLS = 10
CELL_SIZE = 30

BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
BLUE = (0, 100, 255)
WHITE = (255, 255, 255)

# 落下速度
FALL_INTERVAL_INIT = 500
FALL_INTERVAL_MIN = 100
FALL_SPEED_STEP_LINES = 5
FALL_SPEED_STEP_MS = 50

# フォントサイズ
FONT_SIZE = 28
FONT_SIZE_TITLE = 52

# 描画パラメータ
GRID_BORDER_WIDTH = 1
SCORE_POS = (5, 5)
OVERLAY_ALPHA = 160
OVERLAY_TITLE_OFFSET_Y = 30
OVERLAY_SUBTITLE_OFFSET_Y = 20

TETRIMINO_SHAPES = {
    "I": {
        "shape": [
            [1, 1, 1, 1],
        ],
        "color": (0, 240, 240),
    },
    "O": {
        "shape": [
            [1, 1],
            [1, 1],
        ],
        "color": (240, 240, 0),
    },
    "T": {
        "shape": [
            [0, 1, 0],
            [1, 1, 1],
        ],
        "color": (160, 0, 240),
    },
    "S": {
        "shape": [
            [0, 1, 1],
            [1, 1, 0],
        ],
        "color": (0, 240, 0),
    },
    "Z": {
        "shape": [
            [1, 1, 0],
            [0, 1, 1],
        ],
        "color": (240, 0, 0),
    },
    "J": {
        "shape": [
            [1, 0, 0],
            [1, 1, 1],
        ],
        "color": (0, 0, 240),
    },
    "L": {
        "shape": [
            [0, 0, 1],
            [1, 1, 1],
        ],
        "color": (240, 160, 0),
    },
}
