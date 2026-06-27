WIDTH  = 420       # 300 (グリッド) + 120 (サイドパネル)
HEIGHT = 600
FPS    = 60

ROWS      = 20
COLS      = 10
CELL_SIZE = 30
MINI_CELL = 18     # NEXT / HOLD プレビュー用のセルサイズ

GRID_W  = COLS * CELL_SIZE   # 300
PANEL_X = GRID_W             # サイドパネルの開始 X 座標

BLACK = (0,   0,   0)
GRAY  = (80,  80,  80)
WHITE = (255, 255, 255)

FALL_INTERVAL_INIT    = 500
FALL_INTERVAL_MIN     = 100
FALL_SPEED_STEP_LINES = 5
FALL_SPEED_STEP_MS    = 50

FONT_SIZE       = 22
FONT_SIZE_TITLE = 52

GRID_BORDER_WIDTH = 1
OVERLAY_ALPHA     = 160

# 消去ライン数 → 点数 (0〜4ライン)
SCORE_TABLE = [0, 100, 300, 500, 800]

TETORIMINO_SHAPES = {
    "I": {"shape": [[1, 1, 1, 1]],          "color": (0, 240, 240)},
    "O": {"shape": [[1, 1], [1, 1]],         "color": (240, 240, 0)},
    "T": {"shape": [[0, 1, 0], [1, 1, 1]],  "color": (160, 0, 240)},
    "S": {"shape": [[0, 1, 1], [1, 1, 0]],  "color": (0, 240, 0)},
    "Z": {"shape": [[1, 1, 0], [0, 1, 1]],  "color": (240, 0, 0)},
    "J": {"shape": [[1, 0, 0], [1, 1, 1]],  "color": (0, 0, 240)},
    "L": {"shape": [[0, 0, 1], [1, 1, 1]],  "color": (240, 160, 0)},
}
