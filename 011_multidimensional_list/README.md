```text
リストの基本操作と、二次元リストの使い方を学びましょう
```

# 目次
- [目次](#目次)
- [データ構造の比較](#データ構造の比較)
  - [ミュータブル / イミュータブル](#ミュータブル--イミュータブル)
  - [イテラブル（iterable）](#イテラブルiterable)
- [配列（リスト）の基本](#配列リストの基本)
  - [要素へのアクセス](#要素へのアクセス)
  - [スライス](#スライス)
  - [よく使うメソッド](#よく使うメソッド)
  - [for文との組み合わせ](#for文との組み合わせ)
- [タプル](#タプル)
- [辞書](#辞書)
  - [よく使うメソッド（辞書）](#よく使うメソッド辞書)
- [リストの次元](#リストの次元)
- [二次元リストの使い方](#二次元リストの使い方)
  - [要素の参照・置き換え](#要素の参照置き換え)
  - [clear](#clear)
  - [sort](#sort)
  - [reverse](#reverse)
- [二次元リストとfor文](#二次元リストとfor文)

---

# データ構造の比較

| | リスト | タプル | 辞書 |
| --- | --- | --- | --- |
| 記法 | `[1, 2, 3]` | `(1, 2, 3)` | `{"key": value}` |
| アクセス | `list[0]` | `tuple[0]` | `dict["key"]` |
| ミュータブル | ○（変更できる） | ✕（変更できない） | ○（変更できる） |
| イテラブル | ○ | ○ | ○（デフォルトはキー） |
| 順序 | ある | ある | ある |
| 重複 | 許可 | 許可 | キーは不可・値は許可 |
| 用途 | 順番のあるデータ | 座標・RGB など固定値 | 名前付きデータ |

## ミュータブル / イミュータブル

| 用語 | 意味 | 例 |
| --- | --- | --- |
| ミュータブル（mutable） | 作成後に中身を変更できる | `list`, `dict` |
| イミュータブル（immutable） | 作成後に中身を変更できない | `tuple`, `str`, `int` |

```python
fruits = ["apple", "banana"]
fruits[0] = "mango"   # OK（リストはミュータブル）

point = (10, 20)
point[0] = 99         # TypeError（タプルはイミュータブル）
```

## イテラブル（iterable）

`for` 文で1つずつ要素を取り出せるオブジェクトのこと

```python
for x in [1, 2, 3]:            print(x)        # リスト
for x in (1, 2, 3):            print(x)        # タプル
for key in {"a": 1}:           print(key)      # 辞書（キー）
for key, val in {"a": 1}.items(): print(key, val)  # 辞書（キーと値）
```

文字列 `str` や `range` もイテラブル

---

# 配列（リスト）の基本

複数の値をまとめて扱うデータ構造

```python
fruits  = ["apple", "banana", "cherry"]  # 文字列のリスト
numbers = [1, 2, 3, 4, 5]               # 数値のリスト
mixed   = [1, "hello", True, None]       # 異なる型も混在できる
empty   = []                             # 空リスト

print(len(fruits))  # 出力: 3 (要素数)
```

サンプル: [example/ex01.py](example/ex01.py)

> 問題: [question/question1.py](question/question1.py) / 解答: [question/answer/answer1.py](question/answer/answer1.py)

## 要素へのアクセス

インデックスは **0始まり**。負のインデックスで末尾からアクセスできる

```python
fruits = ["apple", "banana", "cherry"]
```

| インデックス | 0 | 1 | 2 |
| --- | --- | --- | --- |
| **値** | `fruits[0]` = "apple" | `fruits[1]` = "banana" | `fruits[2]` = "cherry" |
| **負のインデックス** | `fruits[-3]` | `fruits[-2]` | `fruits[-1]` |

```python
print(fruits[0])   # 出力: apple  (先頭)
print(fruits[1])   # 出力: banana
print(fruits[-1])  # 出力: cherry (末尾)
print(fruits[-2])  # 出力: banana (末尾から2番目)
```

サンプル: [example/ex02.py](example/ex02.py)

> 問題: [question/question2.py](question/question2.py) / 解答: [question/answer/answer2.py](question/answer/answer2.py)

## スライス

`リスト[開始:終了]` で部分リストを取得する（終了インデックスは含まない）

```python
numbers = [0, 1, 2, 3, 4]

print(numbers[1:3])   # 出力: [1, 2]
print(numbers[:3])    # 出力: [0, 1, 2]  (先頭から3つ)
print(numbers[2:])    # 出力: [2, 3, 4]  (2番目以降)
print(numbers[::-1])  # 出力: [4, 3, 2, 1, 0]  (逆順)
```

サンプル: [example/ex03.py](example/ex03.py)

> 問題: [question/question3.py](question/question3.py) / 解答: [question/answer/answer3.py](question/answer/answer3.py)

## よく使うメソッド

```python
fruits = ["apple", "banana"]

fruits.append("cherry")     # 末尾に追加
fruits.insert(1, "mango")   # 指定位置に追加
fruits.remove("banana")     # 値を指定して削除
fruits.pop()                # 末尾を削除して返す
fruits.pop(0)               # インデックスを指定して削除して返す
fruits.sort()               # 昇順にソート（元のリストを変更）
fruits.reverse()            # 逆順にする
fruits.index("apple")       # 値のインデックスを返す
"apple" in fruits           # 値が含まれるか確認 → True / False
```

サンプル: [example/ex04.py](example/ex04.py)

> 問題: [question/question4.py](question/question4.py) / 解答: [question/answer/answer4.py](question/answer/answer4.py)

## for文との組み合わせ

```python
fruits = ["apple", "banana", "cherry"]

# 要素を順番に取り出す
for fruit in fruits:
    print(fruit)

# インデックスと要素を同時に取得する
for i, fruit in enumerate(fruits):
    print(i, fruit)  # 出力: 0 apple / 1 banana / 2 cherry
```

サンプル: [example/ex05.py](example/ex05.py)

> 問題: [question/question5.py](question/question5.py) / 解答: [question/answer/answer5.py](question/answer/answer5.py)

---

# タプル

リストと似ているが**変更不可（イミュータブル）**なデータ構造

```python
point = (10, 20)        # 丸括弧で作成
rgb   = (255, 128, 0)
empty = ()              # 空タプル
one   = (1,)            # 要素が1つの場合はカンマが必要
```

| | リスト | タプル |
| --- | --- | --- |
| 記法 | `[1, 2, 3]` | `(1, 2, 3)` |
| 変更 | できる | できない |
| 用途 | 変化するデータ | 座標・RGB など固定値 |

```python
point = (10, 20)
```

| インデックス | 0 | 1 |
| --- | --- | --- |
| **値** | `point[0]` = 10 | `point[1]` = 20 |

```python
print(point[0])   # 出力: 10
x, y = point      # アンパック
print(x, y)       # 出力: 10 20
```

---

# 辞書

**キーと値のペア**でデータを管理するデータ構造

```python
player = {
    "name": "太郎",
    "hp": 100,
    "level": 5,
}
```

| キー | `"name"` | `"hp"` | `"level"` |
| --- | --- | --- | --- |
| **値** | `player["name"]` = "太郎" | `player["hp"]` = 100 | `player["level"]` = 5 |

```python
print(player["name"])   # 出力: 太郎
print(player["hp"])     # 出力: 100
```

要素の追加・変更・削除

```python
player["mp"] = 50          # 追加
player["hp"] = 80          # 変更
del player["level"]        # 削除
```

for文で全要素を取り出す

```python
for key, value in player.items():
    print(key, value)
```

> 問題: [question/question6.py](question/question6.py) / 解答: [question/answer/answer6.py](question/answer/answer6.py)

## よく使うメソッド（辞書）

| メソッド | 説明 | 例 |
| --- | --- | --- |
| `.keys()` | キーの一覧 | `player.keys()` |
| `.values()` | 値の一覧 | `player.values()` |
| `.items()` | キーと値のペアの一覧 | `player.items()` |
| `.get(key, default)` | キーがなくてもエラーにならない | `player.get("mp", 0)` |
| `key in dict` | キーが存在するか確認 | `"name" in player` |

```python
# get はキーが存在しない時にデフォルト値を返す
print(player.get("mp", 0))   # キー "mp" がなければ 0 を返す
```

> 問題: [question/question7.py](question/question7.py) / 解答: [question/answer/answer7.py](question/answer/answer7.py)

---

# リストの次元

| 次元 | イメージ | 例 |
| --- | --- | --- |
| 一次元 | 1列のデータ | `[1, 2, 3]` |
| 二次元 | 表・グリッド | `[[1,2], [3,4]]` |
| 三次元 | 立体・RGB画像など | `[[[R,G,B], ...], ...]` |

```python
# 一次元リスト
numbers = [1, 2, 3]

# 二次元リスト（行 × 列）
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
```

二次元リストはマトリクス（表）として表現できる

|  | 列 0 | 列 1 | 列 2 |
| --- | --- | --- | --- |
| **行 0** | `matrix[0][0]` = 1 | `matrix[0][1]` = 2 | `matrix[0][2]` = 3 |
| **行 1** | `matrix[1][0]` = 4 | `matrix[1][1]` = 5 | `matrix[1][2]` = 6 |
| **行 2** | `matrix[2][0]` = 7 | `matrix[2][1]` = 8 | `matrix[2][2]` = 9 |

---

# 二次元リストの使い方

## 要素の参照・置き換え

```python
# 参照: リスト[行][列]
print(matrix[0][1])  # 出力: 2（0行目・1列目）

# 置き換え
matrix[0][1] = 99
```

サンプル: [example/ex06.py](example/ex06.py)

> 問題: [question/question8.py](question/question8.py) / 解答: [question/answer/answer8.py](question/answer/answer8.py)

## clear

リストの要素を全て削除する

```python
matrix.clear()  # [] になる
```

サンプル: [example/ex07.py](example/ex07.py)

## sort

要素を昇順・降順に並び替える（元のリストを変更する）

```python
numbers = [3, 1, 4, 1, 5]
numbers.sort()               # 昇順: [1, 1, 3, 4, 5]
numbers.sort(reverse=True)   # 降順: [5, 4, 3, 1, 1]
```

サンプル: [example/ex08.py](example/ex08.py)

> 問題: [question/question9.py](question/question9.py) / 解答: [question/answer/answer9.py](question/answer/answer9.py)

## reverse

要素を逆順に並び替える（元のリストを変更する）

```python
numbers = [1, 2, 3]
numbers.reverse()  # [3, 2, 1]
```

サンプル: [example/ex09.py](example/ex09.py)

> 問題: [question/question10.py](question/question10.py) / 解答: [question/answer/answer10.py](question/answer/answer10.py)

---

# 二次元リストとfor文

for文を1つ使うと一次元リスト（行）を1つずつ取り出す

```python
for row in matrix:
    print(row)
```

サンプル: [example/ex10.py](example/ex10.py)

for文を2つネストすると全要素を1つずつ取り出す

```python
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"matrix[{i}][{j}] = {matrix[i][j]}")
```

サンプル: [example/ex11.py](example/ex11.py) / [example/ex12.py](example/ex12.py)

> 問題: [question/question11.py](question/question11.py) / 解答: [question/answer/answer11.py](question/answer/answer11.py)

> 問題: [question/question12.py](question/question12.py) / 解答: [question/answer/answer12.py](question/answer/answer12.py)

> 問題: [question/question13.py](question/question13.py) / 解答: [question/answer/answer13.py](question/answer/answer13.py)

> 問題（応用）: [012_TicTocToe/example/TicTocToe.py](../012_TicTocToe/example/TicTocToe.py)
