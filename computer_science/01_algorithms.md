# アルゴリズム

## 目次
- [アルゴリズムとは](#アルゴリズムとは)
- [探索](#探索)
  - [線形探索](#線形探索)
  - [二分探索](#二分探索)
- [ソート](#ソート)
  - [選択ソート](#選択ソート)
  - [Python の sort・sorted](#python-の-sort・sorted)
- [再帰](#再帰)

---

## アルゴリズムとは

「問題を解くための手順」のこと。同じ問題でも、手順（アルゴリズム）が違えば速さやメモリの使い方が変わる。

このリポジトリでは `27_bou_taoshi` の「棒倒し法」が、迷路を作るためのアルゴリズムの実例になっている（格子状に立てた棒を1本ずつランダムな向きに倒して壁を作る、という具体的な手順）。同じ迷路でも「穴掘り法」「壁伸ばし法」という別のアルゴリズムで作ることもできる。**同じ結果を得る方法は1つではない**、という視点が重要。

## 探索

リストの中から目的の値を探す方法。

### 線形探索

先頭から順番に1つずつ確認していく、もっとも単純な探索方法。

```python
def linear_search(items, target):
    for i, item in enumerate(items):
        if item == target:
            return i
    return -1   # 見つからなかった

enemies = ["スライム", "ゴブリン", "ドラゴン"]
linear_search(enemies, "ドラゴン")   # → 2
```

Python の `in` や `list.index()` は、内部的にこれと同じ考え方で探している。

### 二分探索

**あらかじめ並べ替えられているリスト**に対して、真ん中の値と比較しながら範囲を半分ずつ絞り込んでいく方法。線形探索よりずっと速い。

```python
def binary_search(items, target):
    low, high = 0, len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

scores = [10, 30, 50, 70, 90]   # 昇順に並んでいる必要がある
binary_search(scores, 70)       # → 3
```

> 要素数が多いリストほど効果を実感しやすい。1,000個のデータから探す場合、線形探索は最悪1,000回の比較が必要だが、二分探索なら最大でも10回程度で見つかる（[計算量](03_computational_complexity.md)を参照）。

## ソート

### 選択ソート

「残りの中から一番小さい値を選んで、先頭から順に並べていく」という素朴なソート方法。

```python
def selection_sort(items):
    result = items.copy()
    for i in range(len(result)):
        min_i = i
        for j in range(i + 1, len(result)):
            if result[j] < result[min_i]:
                min_i = j
        result[i], result[min_i] = result[min_i], result[i]   # 多重代入で入れ替え
    return result

selection_sort([50, 10, 40, 20])   # → [10, 20, 40, 50]
```

`result[i], result[min_i] = result[min_i], result[i]` の入れ替えは、[多重代入](../docs/python_grammar/01_basic.md#多重代入)の応用。仕組みを理解するための一例であり、実際のコードでこれを自分で書く必要はほとんど無い。

### Python の sort・sorted

普段のコードでは、自分でソートアルゴリズムを書く代わりに、組み込みの `sort()`/`sorted()`（[基礎編](../docs/python_grammar/01_basic.md#リストの主なメソッド)・[中級編](../docs/python_grammar/02_intermediate.md#組み込み関数)を参照）を使う。Python の `sorted()` は内部的に「Timsort」という高速なアルゴリズムで実装されており、自作の選択ソートよりずっと効率的に動く。

> 「仕組みを理解すること」と「実際に使うときは標準機能に任せること」は両立する。車輪の再発明はせず、標準機能を信頼してよい。

## 再帰

関数が**自分自身を呼び出す**書き方。

```python
def countdown(n):
    if n <= 0:
        print("発射！")
        return
    print(n)
    countdown(n - 1)   # 自分自身を呼び出す

countdown(3)
# 3
# 2
# 1
# 発射！
```

再帰には必ず「終わりの条件」（`if n <= 0:` の部分）が必要。無いと `RecursionError` になるまで呼び出しが続いてしまう。

```python
# 階乗（n! = n × (n-1) × ... × 1）を再帰で書く例
def factorial(n):
    if n == 0:
        return 1              # 終わりの条件
    return n * factorial(n - 1)

factorial(5)   # → 120
```

> 同じ処理は `for`/`while` ループでも書けることが多い。再帰はデータが木構造のように入れ子になっている場合に、特に自然に書けることが多い（[木構造](02_data_structures.md#木構造)を参照）。
