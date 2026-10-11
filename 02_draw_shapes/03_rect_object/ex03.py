"""
Rectに値を入れて表示する
"""

import pygame as pg
data = pg.Rect(10, 20, 30, 40)
print("X,Y=",data.x, data.y, "幅,高さ=",data.width, data.height)

data.x += 1
print("X,Y=",data.x, data.y, "幅,高さ=",data.width, data.height)
