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

サンプル: [example/ex01.py](example/ex01.py)（ex01〜ex04 は終わらないループなので、止めるときは `Ctrl + C` を押す。リポジトリのルートで `python 10_exception/example/ex01.py` のように実行する。実行のしかたは [03_linux_command](../03_linux_command/README.md)）

練習: [practice/practice01.py](practice/practice01.py)（「# ★」の部分が空欄になっているので、サンプルを見ながら自分の手でコードを打ち込んで完成させよう）

動いたら、書き換えてもう一度動かし、変化を確認する。実行する前に、結果を予想してみるとよい。

| 試すこと | 確認すること |
| --- | --- |
| `abc` を入力 | `ValueError: invalid literal for int() with base 10: 'abc'` が表示されて、プログラムが終了する（最後の行が「例外の種類: メッセージ」になっている） |
| 何も入力せずに Enter | `ValueError`（メッセージの最後が `''`）。空の文字列は、整数に変換できない |
| `3.5` / `1e3` | どちらも `ValueError`。`int()` は、整数の文字列しか変換できない |
| ` 5 `（前後に空白）/ `５`（全角）/ `-3` | どれもエラーにならず、`5` / `5` / `-3` と表示される（前後の空白は無視され、全角の数字も整数として読める） |
| 例外が発生したあと | プログラムが終了するので、ループは続かない（例外を処理していないため） |

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

練習: [practice/practice02.py](practice/practice02.py)

| 試すこと | 確認すること |
| --- | --- |
| `abc` を入力 | メッセージが表示され、そのあとも続けて入力できる（例外を `except` で処理したので、プログラムが終了しない） |
| `except ValueError` → `except TypeError` | `abc` を入力すると `ValueError` でプログラムが終了する。`except` に書いた種類と、実際に発生した例外の種類が違うと、キャッチされない |
| `10 / int(input(...))` に変えて `0` を入力 | `ZeroDivisionError: division by zero` でプログラムが終了する。`except ValueError` では、`ZeroDivisionError` はキャッチされない |
| `except ZeroDivisionError:` を足す | `0` を入力するとメッセージが表示され、続けて入力できる。`except` は複数並べて書ける |
| `print` を `try` の外に出す | `abc` のとき、メッセージのあとに `UnboundLocalError`（`num` に値が入っていない）で終了する。例外が発生すると `try` の中の残りの処理は飛ばされるので、その値を使う処理も `try` の中に書く |

> 問題: [question/question1.py](question/question1.py) / 解答: [question/answer/answer1.py](question/answer/answer1.py)

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

練習: [practice/practice03.py](practice/practice03.py)

| 試すこと | 確認すること |
| --- | --- |
| `abc` を入力 | `エラーが発生しました：invalid literal for int() with base 10: 'abc'` と `エラーの型：<class 'ValueError'>` が表示される |
| 何も入力せずに Enter | メッセージの `'abc'` の部分が `''` に変わる |
| `type(e)` → `type(e).__name__` | `<class 'ValueError'>` ではなく、`ValueError` だけが表示される |
| `except ValueError as e` → `except Exception as e` | 同じように処理される（`ValueError` は `Exception` の仲間のため。→ 下の「例外クラスの継承階層」） |

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

練習: [practice/practice04.py](practice/practice04.py)

| 試すこと | 確認すること |
| --- | --- |
| 整数（例: `5`）と `abc` を順番に入力 | 整数のときだけ「正常に整数が入力されました。」が表示される（`else` は、例外が発生しなかったときだけ実行される） |
| `else:` を `finally:` に書き換える | 整数でも `abc` でも「正常に〜」が表示される（`finally` は、例外の有無に関係なく実行される） |
| `else:` の下に `finally: print("おわり")` を足す | 整数のときも `abc` のときも、最後に必ず「おわり」が表示される |

> 問題: [question/question2.py](question/question2.py) / 解答: [question/answer/answer2.py](question/answer/answer2.py)

## finally節

```python
try:
    # 例外の発生が想定される処理
except 例外の種類:
    # 例外が発生したときの処理
finally:
    # 例外の発生に関わらず最後に必ず実行される処理
```

例外が発生してもしなくても、最後に必ず実行される。ファイルのクローズや後片付けに使う

```python
try:
    num = int(input("数字を入力してください："))
    print(f"入力された数字は{num}です")
except ValueError:
    print("入力は無効です。")
finally:
    print("プログラムを終了します。")  # 例外の有無にかかわらず実行される
```

---

# 例外の発生 raise文

`raise` 文を使って任意のタイミングで例外を発生させることができる

```python
raise エラーの種類("エラーメッセージ")
```

サンプル: [example/ex05.py](example/ex05.py)（このサンプルは、わざと例外を発生させて終了する）

練習: [practice/practice05.py](practice/practice05.py)

| 試すこと | 確認すること |
| --- | --- |
| `NameError` → `ValueError` / `ZeroDivisionError` | 最後の行の、例外の種類が変わる（`ValueError: エラーテスト`） |
| メッセージ（`"エラーテスト"`）を変える | 最後の行の `:` のあとに表示される |
| `raise` の下に `print(...)` を足す | 表示されない（`raise` で例外が発生した時点でプログラムが終了し、以降の行は実行されない） |
| `try:` の中で `raise` して、`except NameError as e:` で `print(e)` | `エラーテスト` と表示され、プログラムは終了しない（自分で発生させた例外も、`except` でキャッチできる） |

関数の中で条件チェックに使うのが一般的な使い方

```python
def calc_speed(dist, time):
    if time <= 0:
        raise ValueError("時間は0より大きい値を入力してください。")
    return dist / time
```

サンプル: [example/ex06.py](example/ex06.py)

練習: [practice/practice06.py](practice/practice06.py)

| 試すこと | 確認すること |
| --- | --- |
| `calc_speed(10, 0)` → `calc_speed(10, 2)` | `時速は5.0km/hです。` が表示される |
| `calc_speed(10, -1)` | 0 以下なので、`時間は0より大きい値を入力してください。` が表示される |
| `except ValueError as e` → `except ZeroDivisionError as e` | `ValueError` でプログラムが終了する（`raise` した例外の種類と、`except` の種類が合わない） |
| 関数の中の `if〜raise` の2行を消す | `ZeroDivisionError: division by zero` で終了する。`ZeroDivisionError` は `ValueError` ではないので、`except ValueError` ではキャッチされない |

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

サンプル: [example/ex07.py](example/ex07.py)（このサンプルは、わざと例外を発生させて終了する）

練習: [practice/practice07.py](practice/practice07.py)

| 試すこと | 確認すること |
| --- | --- |
| `Exception` → `ValueError` | 最後の行が `ValueError: エラーメッセージ` になる |
| `raise ValueError("x")` を `except Exception as e:` でキャッチ | キャッチされる（`ValueError` は `Exception` の子クラスなので、親の `except` でキャッチできる） |
| `raise Exception("x")` を `except ValueError as e:` でキャッチ | キャッチされず、プログラムが終了する（親の例外は、子の `except` ではキャッチできない） |
| `1 / 0` を `except ArithmeticError as e:` でキャッチ | キャッチされる（`ZeroDivisionError` は `ArithmeticError` の仲間） |
| `[][0]` を `except LookupError as e:` でキャッチ | キャッチされる（`IndexError` は `LookupError` の仲間） |

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

サンプル: [example/ex08.py](example/ex08.py)

練習: [practice/practice08.py](practice/practice08.py)

| 試すこと | 確認すること |
| --- | --- |
| `value = None` → `value = 0` / `value = ""` | `Noneではない`（`0` や空文字は、値があるので `None` ではない） |
| `value = None` の行を消す | `NameError`（変数が未定義）。`None` を代入した状態とは違う |
| `value is None` → `value == None` | 同じ結果になる。ただし `None` との比較には `is` を使うのが慣例 |
| `value = "None"`（文字列） | `Noneではない`（文字列であって、`None` ではない） |

サンプル: [example/ex09.py](example/ex09.py)（`return` を書かない関数は `None` を返す → [06_function](../06_function/README.md) の「None が返る条件」）

練習: [practice/practice09.py](practice/practice09.py)

| 試すこと | 確認すること |
| --- | --- |
| `func` の中に `return 5` を足す | `value` に `5` が入り、`5` と表示される |
| `return` だけ（値なし）を足す | `value` は `None` のまま |
| `print(value)` の下に `print(type(value))` を足す | `<class 'NoneType'>` と表示される |

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

練習: [practice/practice10.py](practice/practice10.py)

| 試すこと | 確認すること |
| --- | --- |
| `b = [1, 2, 3]` → `b = a` | `a == b` も `a is b` も `True`（同じリストを指しているため） |
| `c = a` → `c = a[:]`（コピー） | `a == c` は `True`、`a is c` は `False`（中身が同じだけの、別のリスト） |
| `c = a` のあとに `c.append(4)`、`print(a)` | `a` も `[1, 2, 3, 4]` になる（`a` と `c` は同じリストだから） |
| `id(a)` と `id(b)` を見比べる | `a is b` が `False` のときは違う数字、`a is c` のように `True` のときは同じ数字になる（数字そのものは、実行のたびに変わる） |

サンプル: [example/ex11.py](example/ex11.py)

練習: [practice/practice11.py](practice/practice11.py)

| 試すこと | 確認すること |
| --- | --- |
| `None` の位置を変える（例: `[None, "水素", None]`） | どの位置でも、`None` の要素だけが `"酸素"` に書き換わる |
| リストに `0` と `""` を入れる（例: `["水素", 0, "", None]`） | `0` や `""` は書き換わらない（`is None` は、`None` のときだけ成り立つ） |
| `if water[i] is None:` → `if not water[i]:`（上のリストで） | `None` だけでなく、`0` や `""` も `"酸素"` に書き換わる（`not` は、`0`・空文字・`None` をすべて「偽」として扱うため） |

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

サンプル: [example/ex12.py](example/ex12.py)

練習: [practice/practice12.py](practice/practice12.py)

| 試すこと | 確認すること |
| --- | --- |
| 何回か実行し直す | 毎回違う小数が表示される |
| `random()` → `random() * 10` | `0` 以上 `10` 未満の小数になる |
| 何回も実行して範囲を確かめる | `0` 以上 `1` 未満に収まる（`1` は出ない） |

サンプル: [example/ex13.py](example/ex13.py)

練習: [practice/practice13.py](practice/practice13.py)

| 試すこと | 確認すること |
| --- | --- |
| 何回か実行し直す | `1`〜`6` の整数が出る |
| `(1, 6)` → `(1, 100)` / `(10, 20)` | 指定した範囲の整数が出る（両端を含む） |
| `(1, 6)` → `(6, 1)` | `ValueError`（`empty range for randrange()`）になる。小さい方を先に書く |
| `for i in range(10):` で10回くり返す | `1` や `6`（範囲の端）も出る（`randint(a, b)` は `b` を含む） |

サンプル: [example/ex14.py](example/ex14.py)

練習: [practice/practice14.py](practice/practice14.py)

| 試すこと | 確認すること |
| --- | --- |
| 何回か実行し直す | 並び方が毎回変わる |
| `print(shuffle(my_list))` | `None` と表示される（`shuffle` は、元のリストを並び替えて、戻り値はない） |
| `shuffle` の前にも `print(my_list)` を足す | 並び替えの前後で、元のリストそのものが変わっている（新しいリストが作られるわけではない） |
| 要素を文字列（例: `["グー", "チョキ", "パー"]`）に変える | 並び替えできる（要素は、数字でも文字列でもよい） |

サンプル: [example/ex15.py](example/ex15.py)

練習: [practice/practice15.py](practice/practice15.py)

| 試すこと | 確認すること |
| --- | --- |
| 何回か実行し直す | `1`〜`5` のどれかが出る |
| 要素を文字列（例: `["グー", "チョキ", "パー"]`）に変える | 文字列が1つ選ばれる |
| リストを空（`[]`）にする | `IndexError`（`Cannot choose from an empty sequence`）になる |
| `for i in range(10):` で10回くり返す | 同じ要素が続けて出ることもある（毎回、独立に選ぶため） |

> 問題: [question/question3.py](question/question3.py) / 解答: [question/answer/answer3.py](question/answer/answer3.py)

> 問題: [question/question4.py](question/question4.py) / 解答: [question/answer/answer4.py](question/answer/answer4.py)
