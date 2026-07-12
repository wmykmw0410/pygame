```text
モジュール・パッケージ・ライブラリの仕組みを学び、コードを分割して再利用できるようにしましょう
```

# 目次
- [モジュール / パッケージ / ライブラリ](#モジュール--パッケージ--ライブラリ)
- [モジュールのインポート](#モジュールのインポート)
- [標準ライブラリ](#標準ライブラリ)
- [ユーザー定義モジュール](#ユーザー定義モジュール)
  - [インポート時の挙動](#インポート時の挙動)
  - [モジュール分割](#モジュール分割)
- [__name__ == "__main__"](#__name__--__main__)
- [パッケージの作り方](#パッケージの作り方)
  - [相対インポート（`.`）](#相対インポート（）)
- [補足](#補足)
  - [モジュールの属性を調べる](#モジュールの属性を調べる)
  - [ゲームのパッケージ化](#ゲームのパッケージ化)

---

# モジュール / パッケージ / ライブラリ

| 用語 | 意味 | 例 |
| --- | --- | --- |
| モジュール | 関数・クラスをまとめた `.py` ファイル | `random.py`, `mycalc.py` |
| パッケージ | 複数のモジュールをまとめたフォルダ | `calculation/` |
| ライブラリ | 他から呼び出されるもの全般（モジュール〜パッケージまとめ） | `pygame`, `pandas` |

ライブラリは大きく2種類ある

| 種類 | 特徴 | 例 |
| --- | --- | --- |
| 標準ライブラリ | Python に同梱。`import` 文だけで使える | `random`, `time`, `sys`, `datetime` |
| サードパーティライブラリ | 別途インストールが必要 | `pygame`, `numpy`, `pandas` |

インストールコマンド

```
pip install <パッケージ名>   # インストール
pip list                    # インストール済み一覧
pip uninstall <パッケージ名> # アンインストール
```

---

# モジュールのインポート

3つのインポート方法がある

| 書き方 | 呼び出し方 | 特徴 |
| --- | --- | --- |
| `import モジュール名` | `モジュール名.関数()` | 名前の衝突を防ぎやすい |
| `from モジュール名 import 関数名` | `関数()` | 記述が短くなる |
| `import モジュール名 as 別名` | `別名.関数()` | 名前が長いモジュールに便利 |

```python
import random
random.randint(1, 6)

from random import randint
randint(1, 6)

import random as rd
rd.randint(1, 6)
```

### `from モジュール名 import *`（非推奨）

`*` を使うとモジュール内のすべての関数を一度にインポートできるが、**名前の衝突が起きやすい**ため通常は避ける

```python
from random import *

randint(1, 6)   # どのモジュールの関数か分からなくなる
```

---

# 標準ライブラリ

リファレンス: https://docs.python.org/ja/3.13/py-modindex.html

## random

サンプル: [example/ex_module/ex_random.py](example/ex_module/ex_random.py)

```python
import random

random.random()           # 0.0 <= N < 1.0 の浮動小数点乱数
random.randint(1, 6)      # 1 以上 6 以下の整数乱数
random.choice(["a", "b"]) # リストからランダムに1つ選ぶ
```

## time

サンプル: [example/ex_module/ex_time.py](example/ex_module/ex_time.py)

```python
import time

time.sleep(5)  # 5秒間スリープ

# 応用: 1秒ずつスリープしてカウントする
print(1)
time.sleep(1)
print(2)
time.sleep(1)
print(3)
```

## datetime

サンプル: [example/ex_module/ex_datetime.py](example/ex_module/ex_datetime.py)

```python
import datetime

today = datetime.date.today()       # 今日の日付
now   = datetime.datetime.now()     # 現在の日時
print(now.hour, now.minute, now.second)
```

## Q1. ジャンケンゲーム

> 問題: [question/question1.py](question/question1.py) / 解答: [question/answer/answer1.py](question/answer/answer1.py)

## Q2. 誕生日計算

> 問題: [question/question2.py](question/question2.py) / 解答: [question/answer/answer2.py](question/answer/answer2.py)

---

# ユーザー定義モジュール

## インポート時の挙動

Python はモジュールを `import` した時点で、そのファイルを**上から順に実行する**。  
関数の定義だけでなく、トップレベルに書かれた処理もすべて走る。

### 組み込み関数が即実行される

サンプル: [example/ex01/greeting1.py](example/ex01/greeting1.py) / [example/ex01/result1.py](example/ex01/result1.py)

<details>
<summary>コードを見る</summary>

```python
# greeting1.py
print("Hello")

# result1.py
import greeting1  # → "Hello" がすぐ出力される
```

</details>

### ユーザー定義関数も即実行される

サンプル: [example/ex02/greeting2.py](example/ex02/greeting2.py) / [example/ex02/result2.py](example/ex02/result2.py)

<details>
<summary>コードを見る</summary>

```python
# greeting2.py
def greeting():
    print("hello")

greeting()  # ← 定義のあとすぐ呼び出している

# result2.py
import greeting2  # → "hello" がすぐ出力される
print("A")
```

</details>

### インポートしていない関数は呼び出せない

`from モジュール名 import 関数名` でインポートした場合、指定した関数**だけ**が使える

サンプル: [example/ex03/greeting3.py](example/ex03/greeting3.py) / [example/ex03/result3.py](example/ex03/result3.py)

<details>
<summary>コードを見る</summary>

```python
# greeting3.py
def greetingA():
    print("hello")

def greetingB():
    print("good morning")

# result3.py
from greeting3 import greetingA  # greetingA だけインポート

print("A")
greetingA()                       # OK
# greetingB()                     # NameError: インポートしていない関数は呼び出せない
print("B")
```

</details>

## モジュール分割

大きくなったファイルから関数を切り出して別ファイルにする

**メリット**
- **再利用**：別のプロジェクトでも `import` するだけで同じ関数が使える
- **可読性**：役割ごとにファイルが分かれるので全体が把握しやすくなる
- **分担**：チーム開発でファイル単位に担当を分けやすくなる

サンプル: [example/ex04/ex04.py](example/ex04/ex04.py) / [example/ex04/mycalc.py](example/ex04/mycalc.py) / [example/ex04/testlist.py](example/ex04/testlist.py)

<details>
<summary>コードを見る</summary>

```python
# mycalc.py（切り出したモジュール）
def gap(score):
    if score >= 90: return "S"
    elif score >= 80: return "A"
    elif score >= 70: return "B"
    elif score >= 60: return "C"
    else: return "F"

# testlist.py（利用側）
import mycalc

scorelist = [95, 75, 30, 85]
for score in scorelist:
    print(score, "点は、", mycalc.gap(score))
```

</details>

## Q3. 単位変換モジュール

> 問題: [question/question3.py](question/question3.py) / 解答: [question/answer/answer3/](question/answer/answer3/)

---

# __name__ == "__main__"

ファイルが**直接実行されたとき**だけコードを動かしたい場合に使う

サンプル: [example/ex06/hello.py](example/ex06/hello.py) / [example/ex06/import_hello.py](example/ex06/import_hello.py)

| 実行方法 | `__name__` の値 |
| --- | --- |
| 直接実行（`python hello.py`） | `"__main__"` |
| インポートされた（`import hello`） | `"hello"` |

<details>
<summary>コードを見る</summary>

```python
# hello.py
def say_hello():
    print("Hello!")

if __name__ == "__main__":
    say_hello()   # 直接実行したときだけ呼ばれる

# import_hello.py
import hello  # say_hello() は呼ばれない（インポートしただけ）
```

</details>

---

# パッケージの作り方

パッケージにしたいフォルダ内に `__init__.py` を作成する

```
calculation/
├── __init__.py    ← これがあるとパッケージとして認識される
├── addition.py
└── subtraction.py
```

## `__init__.py` の役割

1. **パッケージの目印**：空でもよい
2. **まとめてエクスポート**：よく使うものをまとめて書いておくと呼び出しが簡単になる

サンプル: [example/ex05/](example/ex05/)

### 相対インポート（`.`）

`__init__.py` 内では**相対インポート**を使ってパッケージ内のモジュールを参照する

| 書き方 | 意味 |
| --- | --- |
| `from .module import func` | 同じパッケージ内の `module.py` から `func` をインポート |
| `from ..module import func` | 1つ上の階層のパッケージから |

先頭の `.` が「このフォルダ（パッケージ）の中を見る」という指示になる

<details>
<summary>コードを見る</summary>

```python
# calculation/__init__.py
from .addition    import add   # ← 同じ calculation/ 内の addition.py
from .subtraction import sub   # ← 同じ calculation/ 内の subtraction.py

# addition.py
def add(x, y):
    return x + y

# subtraction.py
def sub(x, y):
    return x - y
```

</details>

呼び出し方の違い

```python
# パターン1: モジュールをインポートして関数を呼ぶ
from calculation import addition
addition.add(1, 2)

# パターン2: 関数を直接インポート（__init__.py でエクスポート済みの場合）
from calculation import add, sub
add(1, 2)

# パターン3: モジュール内の関数を直接インポート
from calculation.subtraction import sub
sub(2, 1)
```

## Q4. 図形パッケージ

> 問題: [question/question4.py](question/question4.py) / 解答: [question/answer/answer4/](question/answer/answer4/)

---

# 補足

## モジュールの属性を調べる

`dir()` でモジュールに定義されている変数・関数の一覧を確認できる

```python
import random
print(dir(random))   # randomモジュールの属性一覧を表示
```

引数なしの場合は、現在のスコープで定義されている名前を一覧表示する

```python
x = 10
def greet(): pass

print(dir())   # ['greet', 'x', ...] のように表示される
```

## ゲームのパッケージ化

このコースで作るゲームも、ここまで学んだモジュール分割・パッケージの考え方で構成されている

例: [021_Tetris/Tetris/](../021_Tetris/Tetris/)

```
Tetris/
├── main.py       ← エントリーポイント（ゲームの起動）
├── config.py     ← 定数（画面サイズ・色など）
└── game/         ← ゲームロジックをまとめたパッケージ
    ├── __init__.py         ← TetrisGame・Renderer をまとめてエクスポート
    ├── tetris_game.py
    ├── tetris_renderer.py
    └── tetrimino.py
```

`__init__.py` で、外部から使うクラスをまとめてエクスポートしておく（`calculation/__init__.py` と同じ考え方）

```python
# game/__init__.py
from .tetris_game     import TetrisGame
from .tetris_renderer import Renderer
```

`main.py`（エントリーポイント）は `game/` パッケージの**外**にあるので、`game` から直接インポートできる

```python
# main.py
from config import WIDTH, HEIGHT, FPS
from game   import TetrisGame, Renderer
```

`game/` パッケージ内のモジュール同士（`tetris_game.py` から `tetrimino.py` を使うときなど）を参照するときは、パッケージ名からのインポートを使う

```python
# game/tetris_game.py
from game.tetrimino import Tetrimino, Grid
```

> 実行するときは `python Tetris/main.py` のように、`main.py` のあるフォルダを基準に `game/` パッケージを認識できる状態で実行する
