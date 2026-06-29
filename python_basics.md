# Python 基本文法

## 目次
- [変数と型](#変数と型)
- [演算子](#演算子)
- [文字列](#文字列)
- [プログラムの三大構造](#プログラムの三大構造)
- [制御構文](#制御構文)
  - [if / elif / else](#if--elif--else)
  - [三項演算子](#三項演算子)
  - [for と while の使い分け](#for-と-while-の使い分け)
  - [iterable](#iterableイテラブル)
  - [for ループ](#for-ループ)
  - [while ループ](#while-ループ)
- [リスト](#リスト)
  - [リスト内包表記](#リスト内包表記)
- [タプル](#タプル)
- [辞書](#辞書)
- [関数](#関数)
  - [スコープ](#スコープ)
- [組み込み関数](#組み込み関数)
- [クラス](#クラス)
- [例外処理](#例外処理)
- [モジュール](#モジュール)

---

## 変数と型

変数に値を入れるとき、型の宣言は不要（代入するだけでよい）

```python
name  = "勇者"      # str  （文字列）
hp    = 100         # int  （整数）
speed = 1.5         # float（小数）
alive = True        # bool （真偽値: True / False）
```

### 型を確認する

```python
print(type(hp))     # → <class 'int'>
```

### 型を変換する

```python
n = int("42")       # 文字列 → 整数
s = str(42)         # 整数   → 文字列
f = float("3.14")   # 文字列 → 小数
```

### None

「値がない」「まだ決まっていない」を表す特別な値。

```python
result = None       # まだ値がない状態

def greet(name):
    print(f"こんにちは、{name}!")
    # return がないと None が返る

x = greet("勇者")   # → こんにちは、勇者!
print(x)            # → None
```

**`None` の比較には `is` を使う**

```python
result = None

# 推奨
if result is None:
    print("まだ値がない")

if result is not None:
    print("値がある")

# 非推奨（動くが意図が伝わりにくい）
if result == None:
    ...
```

よく使う場面：

```python
# デフォルト引数に None を使い、呼び出し時に省略できるようにする
def create_enemy(name, color=None):
    if color is None:
        color = pg.Color("RED")   # 省略時のデフォルト
    ...
```

---

## 演算子

### 算術演算子

| 演算子 | 意味 | 例 | 結果 |
| --- | --- | --- | --- |
| `+` | 足し算 | `3 + 2` | `5` |
| `-` | 引き算 | `3 - 2` | `1` |
| `*` | 掛け算 | `3 * 2` | `6` |
| `/` | 割り算（小数） | `7 / 2` | `3.5` |
| `//` | 割り算（整数） | `7 // 2` | `3` |
| `%` | 余り | `7 % 2` | `1` |
| `**` | べき乗 | `2 ** 3` | `8` |

### 比較演算子

```python
10 == 10   # True  （等しい）
10 != 5    # True  （等しくない）
10 > 5     # True  （より大きい）
10 >= 10   # True  （以上）
10 < 5     # False （より小さい）
10 <= 9    # False （以下）
```

### 論理演算子

```python
True and False  # False（両方 True のとき True）
True or  False  # True （どちらかが True のとき True）
not True        # False（True/False を逆にする）
```

### 代入演算子

```python
x = 10
x += 3   # x = x + 3  → 13
x -= 2   # x = x - 2  → 11
x *= 2   # x = x * 2  → 22
x //= 3  # x = x // 3 → 7
```

---

## 文字列

```python
s = "Hello, World!"

len(s)           # 文字数: 13
s[0]             # 先頭の文字: 'H'
s[-1]            # 末尾の文字: '!'
s[0:5]           # スライス: 'Hello'
s.upper()        # 大文字: 'HELLO, WORLD!'
s.lower()        # 小文字: 'hello, world!'
s.replace("World", "Python")  # 'Hello, Python!'
"Hello" in s     # True（含まれているか）
```

### f 文字列（変数を埋め込む）

```python
name = "勇者"
hp   = 80
print(f"{name} の HP は {hp} です")  # → 勇者 の HP は 80 です
print(f"HP: {hp:3d}")                # → HP:  80  （3桁右寄せ）
```

---

## プログラムの三大構造

すべてのプログラムは、次の3つの組み合わせで成り立っている。

| 構造 | 意味 | Python での書き方 |
| --- | --- | --- |
| 順次処理 | 上から順に1行ずつ実行する | （普通に並べて書くだけ） |
| 条件分岐 | 条件によって実行する処理を変える | `if` / `elif` / `else` |
| 繰り返し | 同じ処理を何度も実行する | `for` / `while` |

```python
# ① 順次処理：上から順に実行される
name = "勇者"
hp   = 100
print(f"{name} が現れた！")   # 1行目が終わってから次へ進む

# ② 条件分岐：hp の値によって表示が変わる
if hp <= 0:
    print("戦闘不能")
else:
    print("元気")

# ③ 繰り返し：同じ処理を 3 回くり返す
for i in range(3):
    print(f"{i + 1} 回目の攻撃！")
```

> この3つを組み合わせるだけで、どんな複雑なプログラムも作れる。

---

## 制御構文

### if / elif / else

```python
hp = 30

if hp <= 0:
    print("戦闘不能")
elif hp <= 50:
    print("ピンチ！")
else:
    print("元気")
```

### 三項演算子

`if / else` を1行で書く省略記法。

```python
# 通常の if / else
if hp > 0:
    status = "生存"
else:
    status = "戦闘不能"

# 三項演算子（1行で書ける）
status = "生存" if hp > 0 else "戦闘不能"
```

書式：

```
値A if 条件 else 値B
```

条件が `True` なら `値A`、`False` なら `値B` が返る。

> 読みやすさ優先なら通常の if / else で書いてよい。  
> 条件と値がシンプルなときだけ使うのがおすすめ。

### for と while の使い分け

| ループ | 使うとき | 例 |
| --- | --- | --- |
| `for` | **回数・対象が決まっている**とき | リストを全部処理する、3回繰り返す |
| `while` | **条件が満たされる間**繰り返すとき | HP が 0 になるまで、ボタンが押されるまで |

### iterable（イテラブル）

`for` ループで順番に取り出せるオブジェクトを **iterable（反復可能なオブジェクト）** と呼ぶ。

| iterable の例 | 説明 |
| --- | --- |
| `[1, 2, 3]` | リスト |
| `(1, 2, 3)` | タプル |
| `"abc"` | 文字列（1文字ずつ取り出せる） |
| `{"a": 1}` | 辞書（キーを順番に取り出せる） |
| `range(5)` | 連番を生成するオブジェクト |

```python
for ch in "abc":
    print(ch)   # a → b → c

for key in {"name": "勇者", "hp": 100}:
    print(key)  # name → hp
```

### for ループ

```python
# リストを順番に取り出す
for name in ["勇者", "魔法使い", "戦士"]:
    print(name)

# 0〜4 の数を繰り返す
for i in range(5):
    print(i)           # 0, 1, 2, 3, 4

# 開始・終了・ステップを指定
for i in range(1, 10, 2):
    print(i)           # 1, 3, 5, 7, 9

# インデックスと値を同時に取り出す
for i, name in enumerate(["勇者", "魔法使い"]):
    print(i, name)     # 0 勇者 / 1 魔法使い
```

### while ループ

```python
hp = 100
while hp > 0:
    hp -= 10
    print(f"HP: {hp}")

# break: ループを抜ける
# continue: 次の繰り返しへスキップ
while True:
    key = input("コマンド: ")
    if key == "q":
        break      # ループを抜ける
    if key == "":
        continue   # 入力が空なら次へ
    print(f"コマンド: {key}")
```

---

## リスト

順番のある値の集まり。値を後から変更できる。

```python
party = ["勇者", "魔法使い", "戦士"]

party[0]          # "勇者"（インデックスは 0 始まり）
party[-1]         # "戦士"（末尾）
len(party)        # 3

party.append("僧侶")    # 末尾に追加
party.insert(1, "盗賊") # 指定位置に挿入
party.remove("魔法使い") # 値で削除
party.pop()             # 末尾を取り出して削除
party.pop(0)            # 先頭を取り出して削除

"勇者" in party   # True（含まれているか）
party.sort()      # 昇順にソート
```

### スライス

```python
nums = [10, 20, 30, 40, 50]
nums[1:3]    # [20, 30]（インデックス 1〜2）
nums[:3]     # [10, 20, 30]（先頭から 3 つ）
nums[2:]     # [30, 40, 50]（インデックス 2 以降）
nums[::-1]   # [50, 40, 30, 20, 10]（逆順）
```

### 二次元リスト

```python
grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0],
]
grid[1][1]   # 1（行・列の順）
```

### リスト内包表記

`for` ループでリストを作る処理を1行で書く省略記法。

```python
# 通常の for ループ
result = []
for x in range(5):
    result.append(x * 2)
# result → [0, 2, 4, 6, 8]

# リスト内包表記（1行で書ける）
result = [x * 2 for x in range(5)]
```

書式：

```
[式 for 変数 in iterable]
```

条件フィルタ付き：

```python
# 通常の for ループ（偶数だけ集める）
evens = []
for x in range(10):
    if x % 2 == 0:
        evens.append(x)

# リスト内包表記
evens = [x for x in range(10) if x % 2 == 0]
# evens → [0, 2, 4, 6, 8]
```

書式：

```
[式 for 変数 in iterable if 条件]
```

> 処理が複雑になる場合は通常の for ループで書いた方が読みやすい。

---

## タプル

リストと似ているが、値を後から変更できない。

```python
point = (100, 200)   # (x, y)
point[0]             # 100
x, y = point         # アンパック（変数に展開）
```

> pygame では座標・サイズなどの引数にタプルを多用する  
> 例: `pg.draw.rect(screen, color, (x, y, w, h))`

### immutable（イミュータブル）と mutable（ミュータブル）

作成後に値を**変更できない**オブジェクトを **immutable（不変）**、変更できるものを **mutable（可変）** と呼ぶ。

| 種類 | 型 | 例 |
| --- | --- | --- |
| immutable（変更不可） | `int` `float` `bool` `str` `tuple` | `(1, 2)` の中身は変えられない |
| mutable（変更可） | `list` `dict` | `[1, 2]` の要素はあとから変えられる |

```python
# タプルは変更しようとするとエラーになる
point = (100, 200)
point[0] = 50        # → TypeError: 'tuple' object does not support item assignment

# リストは変更できる
coords = [100, 200]
coords[0] = 50       # OK → [50, 200]
```

> immutable なオブジェクトは「絶対に変わらない値」として使うのに向いている。  
> 座標・サイズなど「変えるつもりのない値」にはタプルを使うと意図が明確になる。

---

## 辞書

キーと値のペアで管理する。

```python
player = {
    "name":   "勇者",
    "hp":     100,
    "attack": 25,
}

player["name"]          # "勇者"（キーでアクセス）
player["hp"] = 80       # 値を変更
player["level"] = 5     # 新しいキーを追加
del player["level"]     # キーを削除

"hp" in player          # True（キーが存在するか）
player.keys()           # キーの一覧
player.values()         # 値の一覧
player.items()          # (キー, 値) のペアの一覧
```

---

## 関数

```python
def greet(name):
    print(f"こんにちは、{name}!")

greet("勇者")   # → こんにちは、勇者!
```

### 戻り値

```python
def add(a, b):
    return a + b

result = add(3, 4)   # 7
```

### デフォルト引数

```python
def take_damage(hp, amount=10):
    return max(0, hp - amount)

take_damage(80)        # amount=10 として計算 → 70
take_damage(80, 30)    # amount=30 として計算 → 50
```

### キーワード引数

```python
def create_player(name, hp=100, attack=20):
    return {"name": name, "hp": hp, "attack": attack}

create_player("勇者", attack=30)   # hp はデフォルト値
```

### スコープ

変数が「どこから使えるか」の範囲のこと。

```python
hp = 100   # グローバル変数（どこからでも読める）

def show_hp():
    print(hp)   # 外の変数を読むことはできる

show_hp()   # → 100
```

**関数の中で作った変数は外から使えない**

```python
def calc():
    result = 42   # ローカル変数（この関数の中だけ有効）

calc()
print(result)   # → NameError: name 'result' is not defined
```

**関数の中から外の変数を書き換えるには `global` を使う**

```python
score = 0

def add_score(n):
    global score      # 外の score を使うと宣言する
    score += n

add_score(10)
print(score)   # → 10
```

> `global` を多用するとバグが起きやすくなる。  
> 関数には引数で値を渡し、戻り値で返すのが基本。

---

## 組み込み関数

import なしで最初から使える関数。

| 関数 | 説明 | 例 |
| --- | --- | --- |
| `len(x)` | 要素数・文字数を返す | `len([1,2,3])` → `3` |
| `max(x)` | 最大値を返す | `max([3,1,2])` → `3` |
| `min(x)` | 最小値を返す | `min([3,1,2])` → `1` |
| `sum(x)` | 合計を返す | `sum([1,2,3])` → `6` |
| `abs(x)` | 絶対値を返す | `abs(-5)` → `5` |
| `round(x, n)` | 小数を四捨五入 | `round(3.14, 1)` → `3.1` |
| `range(n)` | 連番を生成する | `range(3)` → `0, 1, 2` |
| `print(x)` | 値を表示する | `print("hello")` |
| `input(s)` | キーボード入力を受け取る | `input("名前: ")` |
| `type(x)` | 型を返す | `type(42)` → `<class 'int'>` |
| `int(x)` | 整数に変換する | `int("42")` → `42` |
| `str(x)` | 文字列に変換する | `str(42)` → `"42"` |
| `float(x)` | 小数に変換する | `float("3.14")` → `3.14` |
| `bool(x)` | 真偽値に変換する | `bool(0)` → `False` |

```python
# pygame でよく使う組み合わせ
hp_list = [100, 70, 130]

total    = sum(hp_list)            # 合計 HP: 300
strongest = max(hp_list)           # 最大 HP: 130
distance  = abs(enemy_x - my_x)   # 距離（負にならない）
```

---

## クラス

データ（属性）と処理（メソッド）をひとまとめにしたもの。

```python
class Player:
    def __init__(self, name, hp):   # コンストラクタ（インスタンス生成時に呼ばれる）
        self.name = name
        self.hp   = hp

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0

    def __str__(self):              # print() で表示される文字列
        return f"{self.name} HP:{self.hp}"


p = Player("勇者", 100)
p.take_damage(30)
print(p.is_alive())   # True
print(p)              # 勇者 HP:70
```

### 継承

既存クラスの機能を引き継いで新しいクラスを作る。

```python
class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp   = hp

    def is_alive(self):
        return self.hp > 0


class Enemy(Character):             # Character を継承
    def __init__(self, name, hp, attack):
        super().__init__(name, hp)  # 親クラスの __init__ を呼ぶ
        self.attack = attack

    def describe(self):
        print(f"{self.name} HP:{self.hp} 攻撃:{self.attack}")


slime = Enemy("スライム", 50, 10)
slime.describe()          # スライム HP:50 攻撃:10
print(slime.is_alive())   # True（継承した is_alive を使える）
```

---

## 例外処理

エラーが起きても処理を続けるための仕組み。

```python
try:
    n = int(input("数を入力: "))
    print(10 / n)
except ValueError:
    print("数値を入力してください")
except ZeroDivisionError:
    print("0 では割れません")
finally:
    print("処理終了")   # 例外の有無に関わらず実行される
```

### よくある例外

| 例外 | 発生する状況 |
| --- | --- |
| `ValueError` | 型変換に失敗（`int("abc")` など） |
| `IndexError` | リストの範囲外アクセス（`list[99]` など） |
| `KeyError` | 辞書に存在しないキー |
| `ZeroDivisionError` | 0 で割る |
| `FileNotFoundError` | ファイルが見つからない |
| `TypeError` | 型が合わない演算 |

---

## モジュール

### import の書き方

```python
import pygame                # pygame をそのまま使う
import pygame as pg          # pg という名前で使う（よく使う略記）
import sys                   # sys モジュール

from pathlib import Path     # pathlib から Path だけ取り込む
from random import randint   # random から randint だけ取り込む
```

### よく使う標準モジュール

| モジュール | 用途 | よく使う機能 |
| --- | --- | --- |
| `random` | 乱数 | `random.randint(a, b)`, `random.choice(list)` |
| `sys` | プログラム制御 | `sys.exit()` |
| `pathlib` | ファイルパス | `Path(__file__).parent / "images"` |
| `math` | 数学関数 | `math.sqrt()`, `math.pi` |
| `time` | 時間 | `time.sleep(sec)` |
