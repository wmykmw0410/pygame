"""辞書の基本 解答"""

player = {
    "name": "太郎",
    "hp": 100,
    "level": 5,
}

print(player["name"])   # 太郎
print(player["hp"])     # 100

player["mp"] = 50       # 追加
player["hp"] = 80       # 変更
del player["level"]     # 削除

for key, value in player.items():
    print(key, value)
