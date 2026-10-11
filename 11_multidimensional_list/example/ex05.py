"""for文でリストの要素を取り出す"""

fruits = ["apple", "banana", "cherry"]

# 要素を順番に取り出す
for fruit in fruits:
    print(fruit)

print("---")

# インデックスと要素を同時に取得する
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
