"""リストのよく使うメソッド"""

fruits = ["apple", "banana", "cherry"]

# 追加
fruits.append("mango")       # 末尾に追加
print(fruits)                # ['apple', 'banana', 'cherry', 'mango']

fruits.insert(1, "grape")    # インデックス1に挿入
print(fruits)                # ['apple', 'grape', 'banana', 'cherry', 'mango']

# 削除
fruits.remove("banana")      # 値を指定して削除
print(fruits)

popped = fruits.pop()        # 末尾を削除して返す
print(popped)                # 出力: mango

# ソート
fruits.sort()                # 昇順（元のリストを変更）
print(fruits)

# 検索
print(fruits.index("apple")) # インデックスを返す: 0
print("grape" in fruits)     # 含まれるか確認: True
