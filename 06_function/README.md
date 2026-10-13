```text
Pythonの関数の定義・呼び出し・スコープについて学びましょう
```


# 目次
- [組み込み関数（built-in functions）](#組み込み関数built-in-functions)
- [ユーザー定義関数](#ユーザー定義関数)
  - [関数の定義](#関数の定義)
  - [命名のスタイル](#命名のスタイル)
  - [関数の呼び出し方](#関数の呼び出し方)
  - [引数の種類](#引数の種類)
    - [補足: キーワード専用引数・位置専用引数](#補足-キーワード専用引数位置専用引数)
  - [戻り値の詳細](#戻り値の詳細)
    - [複数の値を返す](#複数の値を返す)
    - [早期 return](#早期-return)
    - [None が返る条件](#none-が返る条件)
  - [None とは](#none-とは)
  - [None と空リスト `[]` の違い](#none-と空リスト--の違い)
    - [関数の使い方がわからない時](#関数の使い方がわからない時)
- [変数のスコープ](#変数のスコープ)
  - [ローカル変数（local variable）](#ローカル変数local-variable)
  - [グローバル変数（global variable）](#グローバル変数global-variable)
    - [グローバル変数を避けるべき理由](#グローバル変数を避けるべき理由)

---

# 組み込み関数（built-in functions）
Pythonインタプリタが最初から用意している関数で、importせずにそのまま使える関数

| 関数名 | 概要 | 使用例 |
| --- | --- | --- |
| `print()` | 画面に出力する | `print("Hello")` |
| `len()` | 要素数を返す | `len("abc")` → 3 |
| `type()` | データ型を返す | `type(123)` → `<class 'int'>` |
| `int()` | 整数に変換 | `int("10")` → 10 |
| `str()` | 文字列に変換 | `str(100)` → `"100"` |
| `list()` | リストに変換 | `list("abc")` → `['a','b','c']` |
| `range()` | 整数の範囲を生成（for文でよく使用） | `range(3)` → 0,1,2 |
| `sum()` | 合計を計算 | `sum([1, 2, 3])` → 6 |
| `max()` | 最大値を返す | `max([1, 5, 3])` → 5 |
| `min()` | 最小値を返す | `min([1, 5, 3])` → 1 |
| `abs()` | 絶対値を返す | `abs(-5)` → 5 |
| `input()` | 入力を受け取る（文字列） | `input("名前は？")` |

全部で70個以上ある

```python
# 一覧の確認方法
import builtins
print(dir(builtins))
```

---

# ユーザー定義関数

## 関数の定義
```python
def func_name(arg1, arg2, ...):
    # process
    return return_value
```

| キーワード | 意味 |
| --- | --- |
| `def` | define(定義する) |
| `func_name` | スネークケースで記載する |
| `(arg1, arg2, ...)` | 引数(省略可) |
| `return return_value` | 戻り値(省略可。省略時は `None` が返される) |

## 命名のスタイル

| 用途 | 命名スタイル | 例 |
| --- | --- | --- |
| 変数名 | スネークケース(小文字+アンダースコア) | `user_name` |
| 関数名 | スネークケース | `calc_sum()` |
| クラス名 | キャメルケース(単語の先頭が大文字) | `MyClass` |
| 定数 | アッパーケース+`_` | `MAX_SPEED`, `PI` |
| 特殊メソッド | ダブルアンダースコア(ダンダー) | `__init__` |

## 関数の呼び出し方
```python
func_name(arg1, arg2, ...)
```

## 引数の種類

| 種類 | 書き方 | 説明 | 例 |
| --- | --- | --- | --- |
| 位置引数 | `def func(a, b)` | 順番で渡す | `func(1, 2)` |
| デフォルト引数 | `def func(a=10)` | 省略可能。右側から指定する | `func()` → a=10 |
| キーワード引数 | `def func(a, b)` | 名前を指定して渡す(順番不問) | `func(b=2, a=1)` |
| 可変長位置引数 | `def func(*args)` | 複数の位置引数をタプルで受け取る | `func(1, 2, 3)` |
| 可変長キーワード引数 | `def func(**kwargs)` | 複数のキーワード引数を辞書で受け取る | `func(x=1, y=2)` |
| キーワード専用引数 | `def func(*, a)` | `*` より後はキーワード指定のみ | `func(a=1)` |
| 位置専用引数 | `def func(a, /)` | `/` より前は位置引数のみ | `func(1)` |

サンプル: [example/ex01.py](example/ex01.py)（位置引数・キーワード引数）

このレッスンのサンプルは、ウィンドウを開かず、結果をターミナルに表示する。リポジトリのルートで `python 06_function/example/ex01.py` のように実行する（実行のしかたは [03_linux_command](../03_linux_command/README.md)）。

練習: [practice/practice01.py](practice/practice01.py)（「# ★」の部分が空欄になっているので、サンプルを見ながら自分の手でコードを打ち込んで完成させよう）

動いたら、書き換えてもう一度動かし、変化を確認する。実行する前に、結果を予想してみるとよい。

| 試すこと | 確認すること |
| --- | --- |
| `add(10, 5)` / `add("a", "b")` | `15` / `ab`（文字列の `+` は、つなげる） |
| `add(1)` | `TypeError`（`missing 1 required positional argument: 'b'`）。引数が足りない |
| `add(1, 2, 3)` | `TypeError`（`takes 2 positional arguments but 3 were given`）。引数が多すぎる |
| `a - b` にして `add(10, 3)` / `add(b=3, a=10)` / `add(3, 10)` | `7` / `7` / `-7`。キーワード指定なら順番を変えても同じ結果、位置指定は順番で結果が変わる |
| `add(1, a=1)` | `TypeError`（`got multiple values for argument 'a'`）。同じ引数を位置とキーワードの両方で渡している |

サンプル: [example/ex02.py](example/ex02.py)（デフォルト引数）

練習: [practice/practice02.py](practice/practice02.py)

| 試すこと | 確認すること |
| --- | --- |
| `add1(5)` / `add1(b=5)` | `7` / `6`。位置引数は左の `a` から順に入り、キーワード指定なら指定した引数に入る |
| `add2` のデフォルト値 `2` → `10`、`add2(3)` | `13`。デフォルト値を変えると、省略したときの値が変わる |
| `add2()` | `TypeError`（`missing 1 required positional argument: 'a'`）。デフォルト値のない引数は省略できない |
| `def add(a=1, b):` | `SyntaxError`（`non-default argument follows default argument`）。デフォルト値のない引数を、右側に置けない。この1行があるとファイル全体が実行できない |

> 問題: デフォルト引数 → [question/question1.py](question/question1.py) / 解答: [question/answer/answer1.py](question/answer/answer1.py)

> 問題: 位置引数・キーワード引数 → [question/question2.py](question/question2.py) / 解答: [question/answer/answer2.py](question/answer/answer2.py)

> 問題: 可変長位置引数(`*args`) → [question/question3.py](question/question3.py) / 解答: [question/answer/answer3.py](question/answer/answer3.py)

> 問題: 可変長キーワード引数(`**kwargs`) → [question/question4.py](question/question4.py) / 解答: [question/answer/answer4.py](question/answer/answer4.py)

### 補足: キーワード専用引数・位置専用引数

`*`・`/` を使うと、引数の渡し方を制限してAPIを分かりやすくできる。

```python
def func(a, b, *, c):
    print(a, b, c)

func(1, 2, c=3)      # OK
# func(1, 2, 3)      # TypeError: c はキーワードでしか渡せない


def greet(name, /, greeting="Hello"):
    print(f"{greeting}, {name}")

greet("Alice")             # OK
# greet(name="Alice")      # TypeError: name はキーワードでは渡せない
```

`*` より後の引数はキーワード指定必須、`/` より前の引数は位置指定必須になる。組み込み関数にも位置専用引数を使うものがある（例: `len(obj, /)`）。

## 戻り値の詳細

### 複数の値を返す
```python
def min_max(numbers):
    return min(numbers), max(numbers)  # タプルとして返される

lo, hi = min_max([3, 1, 4, 1, 5])
print(lo, hi)  # 出力: 1 5
```

> 問題: 複数の値を返す → [question/question6.py](question/question6.py) / 解答: [question/answer/answer6.py](question/answer/answer6.py)

### 早期 return
条件を満たさない場合に関数を早く抜ける

```python
def divide(a, b):
    if b == 0:
        return None  # 早期 return でゼロ除算を防ぐ
    return a / b
```

> 問題: 早期return → [question/question5.py](question/question5.py) / 解答: [question/answer/answer5.py](question/answer/answer5.py)

### None が返る条件
`return` を書かない、または `return` だけ書いた場合は `None` が返る

```python
def greet(name):
    print(f"Hello, {name}")  # return なし

result = greet("Alice")
print(result)  # 出力: None
```

## None とは

`None` はPythonの特殊な値で「何もない」「値が存在しない」ことを表す

```python
x = None
print(x)        # 出力: None
print(type(x))  # 出力: <class 'NoneType'>
```

| 項目 | 内容 |
| --- | --- |
| 型 | `NoneType` |
| 真偽値 | `False` として扱われる |
| 比較 | `== None` より `is None` を使うのが慣例 |

```python
result = None

# None かどうかの確認
if result is None:
    print("値がありません")

# None でないことの確認
if result is not None:
    print("値があります")
```

```python
# いずれも if で False として扱われる
if not None:  print("None は False")
if not []:    print("空リストは False")
if not "":    print("空文字は False")
```

## None と空リスト `[]` の違い

どちらも「何もない」ように見えるが意味が異なる

| | `None` | `[]` |
| --- | --- | --- |
| 意味 | 値そのものが存在しない | リストは存在するが中身が空 |
| 型 | `NoneType` | `list` |
| 要素追加 | できない（エラー） | `append()` で追加できる |
| よく使う場面 | 関数が値を返せなかった時 | これから要素を追加する予定のリスト |

```python
result_none = None
result_empty = []

# None にはappendできない
# result_none.append(1)  # AttributeError

# 空リストには追加できる
result_empty.append(1)
print(result_empty)  # 出力: [1]
```

### 関数の使い方がわからない時
```python
help(関数名)          # 例: help(print)
print(関数名.__doc__) # 例: print(len.__doc__)
```

---

# 変数のスコープ

## ローカル変数（local variable）
```python
def greet():
    name = "Alice"  # ローカル変数: 関数の中でのみ有効
    print("Hello,", name)

greet()
# print(name)  # エラー！関数の外からはアクセスできない
```

サンプル: [example/ex03.py](example/ex03.py)

練習: [practice/practice03.py](practice/practice03.py)

| 試すこと | 確認すること |
| --- | --- |
| 関数の外で `print(name)` | `NameError`（`name 'name' is not defined`）。関数の中の `name` は、外からは見えない |
| 関数の外に `name = "Bob"` を作り、最後に `print(name)` | 関数の中は `Alice`、外は `Bob`。同じ名前でも、別の変数として扱われる |
| 関数の中の `"Alice"` を別の名前に変える | 関数の外の `name`（`Bob`）は変わらない |

## グローバル変数（global variable）
```python
message = "こんにちは"  # グローバル変数: プログラム全体で有効

def greet():
    print(message)  # 関数の中から参照できる

greet()  # 出力: こんにちは
```

サンプル: [example/ex04.py](example/ex04.py)

練習: [practice/practice04.py](practice/practice04.py)

| 試すこと | 確認すること |
| --- | --- |
| 関数の定義のあと、呼び出す前に `message = "こんばんは"` | `こんばんは` が表示される。関数が呼ばれた時点の値を使う |
| 関数の中に `message = "やあ"` を足して、外でも `print(message)` | 関数の中は `やあ`、外は `こんにちは`。関数の中の代入は、新しいローカル変数を作る |

関数の中でグローバル変数を **変更** するには `global` 宣言が必要

```python
count = 0

def increment():
    global count   # global をつけないと UnboundLocalError
    count += 1

increment()
print(count)  # 出力: 1
```

サンプル: [example/ex05.py](example/ex05.py)

練習: [practice/practice05.py](practice/practice05.py)

| 試すこと | 確認すること |
| --- | --- |
| `increment()` を3回呼ぶ | `count` は `3` になる |
| `global count` の行を消して呼ぶ | `UnboundLocalError` になる（外の `count` ではなく、ローカル変数として扱われるため） |
| 関数の中で `print(count)` だけにする | `global` なしで、外の `count` の値を表示できる（参照するだけなら `global` は不要） |

> 問題: global宣言 → [question/question7.py](question/question7.py) / 解答: [question/answer/answer7.py](question/answer/answer7.py)

### グローバル変数を避けるべき理由

| 理由 | 説明 |
| --- | --- |
| 予測しにくい | どこからでも変更できるため、バグの原因になりやすい |
| テストがしづらい | 特定の値に依存した関数は再利用性が下がる |
| 可読性が低くなる | 外部の変数が関数に影響することで、理解しにくいコードになる |

