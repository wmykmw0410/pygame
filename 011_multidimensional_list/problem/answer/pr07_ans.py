"""辞書のメソッド 解答"""

items = {
    "name": "りんご",
    "price": 120,
    "count": 5,
}

print(items.keys())           # dict_keys(['name', 'price', 'count'])
print(items.values())         # dict_values(['りんご', 120, 5])
print("price" in items)       # True
print(items.get("stock", 0))  # 0（キーが存在しないのでデフォルト値）
