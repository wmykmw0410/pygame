```text
Pythonの関数の定義・呼び出し・スコープについて学びましょう
```


# 目次
- [目次](#目次)
- [組み込み関数（built-in functions）](#組み込み関数built-in-functions)
- [ユーザー定義関数](#ユーザー定義関数)
  - [関数の定義](#関数の定義)
  - [命名のスタイル](#命名のスタイル)
  - [関数の呼び出し方](#関数の呼び出し方)
  - [引数の種類](#引数の種類)
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

> サンプル: [example/ex01.py](example/ex01.py)

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

> サンプル: [example/ex02.py](example/ex02.py)

> 練習: デフォルト引数 → [problem/pr01.py](problem/pr01.py) / 解答: [answer/pr01_ans.py](answer/pr01_ans.py)

> 練習: 位置引数・キーワード引数 → [problem/pr02.py](problem/pr02.py) / 解答: [answer/pr02_ans.py](answer/pr02_ans.py)

> 練習: 可変長位置引数(`*args`) → [problem/pr03.py](problem/pr03.py) / 解答: [answer/pr03_ans.py](answer/pr03_ans.py)

> 練習: 可変長キーワード引数(`**kwargs`) → [problem/pr04.py](problem/pr04.py) / 解答: [answer/pr04_ans.py](answer/pr04_ans.py)

## 戻り値の詳細

### 複数の値を返す
```python
def min_max(numbers):
    return min(numbers), max(numbers)  # タプルとして返される

lo, hi = min_max([3, 1, 4, 1, 5])
print(lo, hi)  # 出力: 1 5
```

### 早期 return
条件を満たさない場合に関数を早く抜ける

```python
def divide(a, b):
    if b == 0:
        return None  # 早期 return でゼロ除算を防ぐ
    return a / b
```

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

> サンプル: [example/ex03.py](example/ex03.py)

## グローバル変数（global variable）
```python
message = "こんにちは"  # グローバル変数: プログラム全体で有効

def greet():
    print(message)  # 関数の中から参照できる

greet()  # 出力: こんにちは
```

> サンプル: [example/ex04.py](example/ex04.py)

関数の中でグローバル変数を **変更** するには `global` 宣言が必要

```python
count = 0

def increment():
    global count   # global をつけないと UnboundLocalError
    count += 1

increment()
print(count)  # 出力: 1
```

> サンプル: [example/ex05.py](example/ex05.py)

### グローバル変数を避けるべき理由

| 理由 | 説明 |
| --- | --- |
| 予測しにくい | どこからでも変更できるため、バグの原因になりやすい |
| テストがしづらい | 特定の値に依存した関数は再利用性が下がる |
| 可読性が低くなる | 外部の変数が関数に影響することで、理解しにくいコードになる |

