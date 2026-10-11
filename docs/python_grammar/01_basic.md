# Python 文法（基礎）

変数・制御構文・リスト/タプル/辞書/集合など、Python プログラムを組み立てるための土台になる文法。

## 目次
- [変数と型](#変数と型)
- [演算子](#演算子)
  - [多重代入](#多重代入)
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
- [集合（set）](#集合set)
- [辞書](#辞書)

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

**比較を連続して書く（チェーン比較）**

```python
x = 5
1 < x < 10     # True（1 < x かつ x < 10 と同じ意味）
0 <= x < 10    # 範囲チェックによく使う書き方
```

`1 < x < 10` は `1 < x and x < 10` と同じ意味になる。「値がある範囲に収まっているか」を判定するときに読みやすい書き方。

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

### 多重代入

**同じ値**を複数の変数に一度に代入できる。

```python
x = y = z = 0
print(x, y, z)   # → 0 0 0
```

`=` を連続させて書くと、右端の値がすべての変数に代入される。3つとも独立した変数になる（1つを書き換えても他は変わらない）。

```python
x = y = 0
x += 5
print(x, y)   # → 5 0（x だけが変わる）
```

**複数の値**を、複数の変数にまとめて代入することもできる。

```python
name, hp, attack = "勇者", 100, 20
print(name, hp, attack)   # → 勇者 100 20
```

これは右辺の `("勇者", 100, 20)` というタプルを、左辺の変数にそれぞれ**アンパック**（展開）している（詳しくは[タプル](#タプル)を参照）。この仕組みを使うと、一時変数を使わずに値を入れ替えられる。

```python
a, b = 1, 2
a, b = b, a   # 一時変数を使わずに入れ替え
print(a, b)   # → 2 1
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

### 文字列を組み立てる他の方法（参考）

f文字列以外にも、次のような書き方がある。新しく書くコードは f文字列で統一してよいが、他の人のコードを読むときのために知っておく。

```python
name, hp = "勇者", 80

f"{name} の HP は {hp}"            # f文字列（推奨）
"{} の HP は {}".format(name, hp)  # str.format()
"%s の HP は %d" % (name, hp)      # % 演算子（古い書き方）
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

### pass 文

「何もしない」ことを明示する文。構文上、文が必須の場所に「とりあえず何もしない」と書きたいときに使う。

```python
def not_implemented_yet():
    pass   # あとで実装する、という仮置き

if hp <= 0:
    pass   # まだ処理を書いていない
else:
    print("元気")
```

### ループの else 節

`for`/`while` は、**途中で `break` されずに最後まで実行しきったときだけ** `else` ブロックが実行される、という少し特殊な機能を持つ。

```python
enemies = ["スライム", "ゴブリン"]

for e in enemies:
    if e == "ドラゴン":
        print("ドラゴンを発見！")
        break
else:
    print("ドラゴンはいなかった")   # break されなかったときだけ実行される
```

> 「リストの中を探して、見つかったら break、最後まで見つからなければ else」という探索処理でよく使われる書き方。

---

## リスト

順番のある値の集まり。値を後から変更できる。

```python
party = ["勇者", "魔法使い", "戦士"]

party[0]          # "勇者"（インデックスは 0 始まり）
party[-1]         # "戦士"（末尾）
len(party)        # 3

"勇者" in party   # True（含まれているか）
```

### リストの主なメソッド

| メソッド | 意味 | 例 |
| --- | --- | --- |
| `append(x)` | 末尾に1つ追加する | `party.append("僧侶")` |
| `extend(iterable)` | 別のリストなどの要素をすべて追加する | `party.extend(["盗賊", "狩人"])` |
| `insert(i, x)` | 指定位置に挿入する | `party.insert(1, "盗賊")` |
| `remove(x)` | 指定した値を先頭から探して削除する（無いと `ValueError`） | `party.remove("魔法使い")` |
| `pop(i)` | 指定位置の要素を取り出して削除する（省略時は末尾） | `party.pop()` / `party.pop(0)` |
| `clear()` | すべての要素を削除する | `party.clear()` |
| `index(x)` | 指定した値が最初に現れる位置を返す（無いと `ValueError`） | `party.index("戦士")` |
| `count(x)` | 指定した値がいくつ含まれるか数える | `party.count("勇者")` |
| `sort()` | 昇順に並べ替える（元のリストを直接書き換える） | `party.sort()` |
| `reverse()` | 並び順を逆にする（元のリストを直接書き換える） | `party.reverse()` |
| `copy()` | リストのコピーを作る | `backup = party.copy()` |

```python
party = ["勇者", "魔法使い"]
party.extend(["戦士", "僧侶"])   # → ['勇者', '魔法使い', '戦士', '僧侶']
party.index("戦士")              # → 2
party.count("勇者")              # → 1
party.reverse()                  # → ['僧侶', '戦士', '魔法使い', '勇者']
```

### del 文で要素を削除する

```python
nums = [10, 20, 30, 40]
del nums[0]      # 先頭を削除 → [20, 30, 40]
del nums[0:2]    # スライスでまとめて削除 → [40]
```

`pop()` は削除した値を受け取れるのに対し、`del` は「値は要らず、削除だけしたい」ときに使う。

### スタック・キューとして使う

```python
# スタック（後入れ先出し）: append() と pop() だけで実現できる
stack = []
stack.append("A")
stack.append("B")
stack.pop()      # → "B"（最後に入れたものが先に出る）

# キュー（先入れ先出し）には collections.deque を使うのが定石
from collections import deque
queue = deque(["A", "B"])
queue.append("C")
queue.popleft()   # → "A"（最初に入れたものが先に出る）
```

> リストの先頭に対する `pop(0)` は要素数が多いと遅くなるため、キューとして使うなら `deque` を使うのが定石。

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
| mutable（変更可） | `list` `dict` `set` | `[1, 2]` の要素はあとから変えられる |

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

## 集合（set）

**重複しない値の集まり**。順番を持たず、同じ値は1つしか持てない。

```python
defeated = {"スライム", "ゴブリン", "スライム"}   # 重複は自動でまとめられる
print(defeated)   # → {'スライム', 'ゴブリン'}（'スライム' は1つだけ残る）

defeated.add("ドラゴン")       # 要素を追加
defeated.discard("ゴブリン")   # 要素を削除（要素が無くてもエラーにならない）

"スライム" in defeated   # True（含まれているか）
len(defeated)            # 要素数
```

### 空の集合を作る

```python
seen = set()   # {} と書くと空の辞書になってしまうので、空集合には set() を使う
seen.add((3, 5))
```

> ゲームでは「すでに倒した敵」「一度でも訪れたマス」のように、**同じものが何度出てきても1回として扱いたいとき**によく使う。`dead_enemies = set()` のように、リストと同じ感覚で `add()` していける。

### 集合の演算

```python
a = {1, 2, 3}
b = {2, 3, 4}

a | b   # 和集合 → {1, 2, 3, 4}
a & b   # 積集合 → {2, 3}
a - b   # 差集合 → {1}
```

リストとの違い：**順番が無い**・**同じ値を2つ持てない**・**インデックスでのアクセスができない**（`defeated[0]` はできない）。「順番や重複が意味を持つか」で、リストと集合のどちらを使うか判断する。

---

## 辞書

キーと値のペアで管理する。順番でアクセスするリストと違い、**名前（キー）でアクセスしたいデータ**に向いている。

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
len(player)              # キーの数
```

### 辞書の主なメソッド

| メソッド | 意味 | 例 |
| --- | --- | --- |
| `keys()` | キーの一覧を返す | `player.keys()` |
| `values()` | 値の一覧を返す | `player.values()` |
| `items()` | `(キー, 値)` のペアの一覧を返す | `player.items()` |
| `get(key, default)` | キーが無くてもエラーにならずに取得する | `player.get("mp", 0)` |
| `pop(key)` | キーを取り出して削除する | `player.pop("level")` |
| `setdefault(key, default)` | キーが無ければ追加し、値を返す（あればそのまま） | `player.setdefault("mp", 0)` |
| `update(other)` | 別の辞書の内容をまとめて反映する | `player.update({"hp": 100, "mp": 30})` |

### 存在しないキーへの安全なアクセス（get）

```python
player["mp"]          # → KeyError（"mp" というキーが無い）
player.get("mp")      # → None（エラーにならない）
player.get("mp", 0)   # → 0（デフォルト値を指定できる）
```

「キーがあるとは限らない」場面では、`[]` ではなく `get()` を使うとエラーを避けられる。

### ループでキーと値を同時に取り出す

```python
for key, value in player.items():
    print(f"{key}: {value}")
# name: 勇者
# hp: 80
# attack: 25
```

`.items()` は「キーと値のペア」を返すので、`for key, value in ...` の形で2つの変数に同時に受け取れる（[zip() の説明](03_advanced.md#zip--複数のリストを同時に処理する)も参照）。

### 辞書を作る他の方法

```python
# dict() 関数とキーワード引数で作る
player = dict(name="勇者", hp=100, attack=25)

# 辞書内包表記（リスト内包表記の辞書版）
squares = {x: x * x for x in range(5)}
# → {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### キーに使える型

辞書のキーには、**immutable（変更できない）な型しか使えない**（`int`/`str`/`tuple` など）。リストのような mutable な型はキーにできない。

```python
positions = {}
positions[(3, 5)] = "宝箱"   # タプルはキーにできる
positions[[3, 5]] = "宝箱"   # → TypeError: unhashable type: 'list'
```

> immutable/mutable の違いは[タプル](#タプル)の節を参照。「座標をキーにしてマスの情報を管理したい」ときは、リストではなくタプルを使う。
