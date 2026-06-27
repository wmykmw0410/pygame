```text
エラーの種類と例外処理の書き方、randomモジュールの使い方を学びましょう
```

# 目次
- [エラーの種類](#エラーの種類)
- [例外処理](#例外処理)
  - [try / except](#try--except)
  - [as句](#as句)
  - [else節](#else節)
  - [finally節](#finally節)
- [例外の発生 raise文](#例外の発生-raise文)
  - [例外クラスの継承階層](#例外クラスの継承階層)
- [Noneオブジェクト](#noneオブジェクト)
  - [== と is の違い](#-と-is-の違い)
- [randomモジュール](#randomモジュール)

---

# エラーの種類

| 種類 | 説明 |
| --- | --- |
| 構文エラー（SyntaxError） | Pythonの文法を守らなかった時に発生。プログラムは実行されない |
| 例外（Exception） | 実行中に予測できない問題が起きた時に発生。適切に処理しないとプログラムが終了する |

主な例外の種類

| 例外 | 発生タイミング |
| --- | --- |
| `ZeroDivisionError` | 何かを0で割った時 |
| `NameError` | 定義されていない変数名が使われた時 |
| `TypeError` | 型が一致していない時 |
| `ValueError` | 型は正しいが想定外の値が使われた時 |
| `ImportError` | モジュールやオブジェクトが読み込めない時 |
| `IndexError` | 存在しないインデックスでアクセスした時 |
| `KeyError` | 存在しないキーで辞書にアクセスした時 |
| `FileNotFoundError` | ファイルが見つからない時 |

サンプル: [example/ex01.py](example/ex01.py)

---

# 例外処理

## try / except

```python
try:
    # 例外の発生が想定される処理
except 例外の種類:
    # 例外が発生したときの処理
```

| 節 | 説明 |
| --- | --- |
| `try` 節 | 例外が発生するかもしれない処理を書く。発生した例外は `except` でキャッチされる |
| `except` 節 | 指定した例外と一致したら実行される。複数書いて複数の例外をキャッチすることも可能 |

try節で例外が発生すると、それ以降のtry節のコードはスキップされてexcept節へ移る

サンプル: [example/ex02.py](example/ex02.py)

> 練習: [problem/pr01.py](problem/pr01.py) / 解答: [problem/answer/pr01_ans.py](problem/answer/pr01_ans.py)

## as句

```python
try:
    # 例外の発生が想定される処理
except 例外の種類 as e:
    print(e)        # エラーの詳細メッセージ
    print(type(e))  # エラーの型
```

`as` の後に変数名を書くと、発生した例外オブジェクトが格納される

サンプル: [example/ex03.py](example/ex03.py)

## else節

```python
try:
    # 例外の発生が想定される処理
except 例外の種類:
    # 例外が発生したときの処理
else:
    # 例外が発生しなかった時の処理
```

サンプル: [example/ex04.py](example/ex04.py)

> 練習: [problem/pr02.py](problem/pr02.py) / 解答: [problem/answer/pr02_ans.py](problem/answer/pr02_ans.py)

## finally節

```python
try:
    # 例外の発生が想定される処理
finally:
    # 例外の発生に関わらず最後に必ず実行される処理
```

---

# 例外の発生 raise文

`raise` 文を使って任意のタイミングで例外を発生させることができる

```python
raise エラーの種類("エラーメッセージ")
```

サンプル: [example/ex05.py](example/ex05.py)

関数の中で条件チェックに使うのが一般的な使い方

```python
def calc_speed(dist, time):
    if time <= 0:
        raise ValueError("時間は0より大きい値を入力してください。")
    return dist / time
```

サンプル: [example/ex06.py](example/ex06.py) / [example/ex07.py](example/ex07.py)

## 例外クラスの継承階層

```
BaseException（全ての例外の親クラス）
 ├─ SystemExit
 ├─ KeyboardInterrupt
 ├─ GeneratorExit
 └─ Exception（独自例外の親クラス）
     ├─ ArithmeticError（算術エラーの基底クラス）
     │   ├─ OverflowError
     │   └─ ZeroDivisionError
     ├─ AttributeError
     ├─ LookupError（インデックス・キーエラーの基底クラス）
     │   ├─ IndexError
     │   └─ KeyError
     ├─ OSError
     │   └─ FileNotFoundError
     ├─ SyntaxError
     │   └─ IndentationError
     ├─ TypeError
     └─ ValueError
```

`Exception` はほとんどの例外の基底クラスで、独自例外を作る際も `Exception` を継承する

---

# Noneオブジェクト

`None` は「データが存在しない」ことを表す特殊なオブジェクト

| 状態 | 例 | 説明 |
| --- | --- | --- |
| `0` や `""` | `x = 0` | 値はあるが、ゼロや空の状態 |
| `None` | `x = None` | 定義はされているが中身が全くない |
| 未定義 | （変数を定義していない） | 変数そのものが存在しない |

```python
# None の代入
x = None

# None かどうかの比較（== ではなく is を使う）
if x is None:
    print("Noneです")
```

サンプル: [example/ex08.py](example/ex08.py) / [example/ex09.py](example/ex09.py) / [example/ex11.py](example/ex11.py)

## == と is の違い

| 演算子 | 比較内容 | 例 |
| --- | --- | --- |
| `==` | 値が等しいか | `[1,2] == [1,2]` → `True` |
| `is` | 同じオブジェクト（メモリ上の場所）か | `[1,2] is [1,2]` → `False` |

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True（値が同じ）
print(a is b)  # False（別のオブジェクト）

c = a
print(a is c)  # True（同じオブジェクトを指している）
```

`None` との比較には `==` より `is` を使うのが慣例

サンプル: [example/ex10.py](example/ex10.py)

---

# randomモジュール

| 関数 | 説明 | 戻り値 |
| --- | --- | --- |
| `random()` | ランダムな浮動小数点数 | `0.0 <= N < 1.0` |
| `randint(a, b)` | ランダムな整数 | `a <= N <= b` |
| `shuffle(list)` | リストの要素をランダムに並び替える（元のリストを変更） | なし |
| `choice(list)` | リストからランダムに1つ選ぶ | 選ばれた要素 |

```python
from random import random, randint, shuffle, choice
```

サンプル: [example/ex12.py](example/ex12.py) / [example/ex13.py](example/ex13.py) / [example/ex14.py](example/ex14.py) / [example/ex15.py](example/ex15.py)

> 練習: [problem/pr03.py](problem/pr03.py) / 解答: [problem/answer/pr03_ans.py](problem/answer/pr03_ans.py)

> 練習: [problem/pr04.py](problem/pr04.py) / 解答: [problem/answer/pr04_ans.py](problem/answer/pr04_ans.py)

> 練習: [problem/pr05.py](problem/pr05.py) / 解答: [problem/answer/pr05_ans.py](problem/answer/pr05_ans.py)

> 練習: [problem/pr06.py](problem/pr06.py) / 解答: [problem/answer/pr06_ans.py](problem/answer/pr06_ans.py)
