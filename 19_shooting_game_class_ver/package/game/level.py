# 難易度テーブル（スコアが高い順に並べる）
LEVELS = [
    {"min_score": 300, "name": "CHASE",  "speed": 10, "move": "chase",  "bg": (60,  0,   0)},
    {"min_score": 200, "name": "ZIGZAG", "speed":  7, "move": "zigzag", "bg": (0,   50,  0)},
    {"min_score": 100, "name": "FAST",   "speed":  7, "move": "fast",   "bg": (50,  0,   80)},
    {"min_score":   0, "name": "NORMAL", "speed":  4, "move": "normal", "bg": (0,   0,   128)},
]


def get_level(score):
    for lv in LEVELS:
        if score >= lv["min_score"]:
            return lv
    return LEVELS[-1]
