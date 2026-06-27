"""Rectの基準点を図示した画像を生成してrect_origin.pngに保存する"""
import pygame as pg

pg.init()

WIDTH, HEIGHT = 500, 400
surface = pg.Surface((WIDTH, HEIGHT))
surface.fill(pg.Color("WHITE"))

font = pg.font.Font(None, 24)

# Rectの位置・サイズ
rx, ry, rw, rh = 150, 100, 200, 150

# 四角形
pg.draw.rect(surface, pg.Color("SKYBLUE"), (rx, ry, rw, rh))
pg.draw.rect(surface, pg.Color("STEELBLUE"), (rx, ry, rw, rh), 2)

# 基準点の定義
points = {
    "topleft\n(x,y)":      (rx,          ry),
    "topright":             (rx + rw,     ry),
    "bottomleft":           (rx,          ry + rh),
    "bottomright":          (rx + rw,     ry + rh),
    "center":               (rx + rw//2,  ry + rh//2),
    "midtop":               (rx + rw//2,  ry),
    "midbottom":            (rx + rw//2,  ry + rh),
    "midleft":              (rx,          ry + rh//2),
    "midright":             (rx + rw,     ry + rh//2),
}

# ラベルのオフセット（点から少しずらして表示）
offsets = {
    "topleft\n(x,y)":   (-10, -30),
    "topright":          (  5, -20),
    "bottomleft":        (-10,  10),
    "bottomright":       (  5,  10),
    "center":            (  8,   5),
    "midtop":            (  5, -20),
    "midbottom":         (  5,  10),
    "midleft":           (-80,  -5),
    "midright":          (  8,  -5),
}

for name, (px, py) in points.items():
    pg.draw.circle(surface, pg.Color("RED"), (px, py), 5)
    ox, oy = offsets[name]
    for i, line in enumerate(name.split("\n")):
        img = font.render(line, True, pg.Color("BLACK"))
        surface.blit(img, (px + ox, py + oy + i * 18))

# 幅・高さのアノテーション
arrow_color = pg.Color("GRAY")
# 幅
pg.draw.line(surface, arrow_color, (rx, ry - 20), (rx + rw, ry - 20), 1)
pg.draw.line(surface, arrow_color, (rx, ry - 25), (rx, ry - 15), 1)
pg.draw.line(surface, arrow_color, (rx + rw, ry - 25), (rx + rw, ry - 15), 1)
label = font.render(f"width={rw}", True, arrow_color)
surface.blit(label, (rx + rw//2 - label.get_width()//2, ry - 38))

# 高さ
pg.draw.line(surface, arrow_color, (rx - 50, ry), (rx - 50, ry + rh), 1)
pg.draw.line(surface, arrow_color, (rx - 55, ry), (rx - 45, ry), 1)
pg.draw.line(surface, arrow_color, (rx - 55, ry + rh), (rx - 45, ry + rh), 1)
label = font.render(f"height={rh}", True, arrow_color)
surface.blit(label, (rx - 125, ry + rh//4 - 8))

pg.image.save(surface, "rect_origin.png")
print("rect_origin.png を保存しました")
pg.quit()
