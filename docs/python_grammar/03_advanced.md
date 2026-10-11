# Python 文法（発展）

ファイルの読み書き・標準ライブラリなど、[基礎](01_basic.md)・[中級](02_intermediate.md)より一歩進んだ文法。このリポジトリのコードには一部すでに登場しているが、概念としては未解説だったもの（`with` 文・`zip()` など）と、まだ登場していないもの（JSON・venv など）をまとめている。

## 目次
- [ファイルの読み書き](#ファイルの読み書き)
- [JSON でデータを保存する](#json-でデータを保存する)
- [lambda（無名関数）](#lambda無名関数)
- [zip() — 複数のリストを同時に処理する](#zip--複数のリストを同時に処理する)
- [イテレータとジェネレータ](#イテレータとジェネレータ)
- [標準ライブラリの概観](#標準ライブラリの概観)
- [仮想環境（venv）とパッケージ](#仮想環境venvとパッケージ)

---

## ファイルの読み書き

テキストファイルを読み込んだり、書き出したりする方法。

### ファイルを読み込む

```python
with open("stage.txt", encoding="utf-8") as f:
    for line in f:
        print(line.rstrip("\n"))   # 行末の改行を取り除いて表示
```

`with` を使うと、ブロックを抜けるときに**自動でファイルを閉じてくれる**。ファイルを開いたまま閉じ忘れる心配がない。

```python
# with を使わない場合（非推奨）
f = open("stage.txt", encoding="utf-8")
for line in f:
    print(line.rstrip("\n"))
f.close()   # 閉じ忘れるとファイルが開いたままになってしまう
```

### ファイルに書き込む

```python
with open("score.txt", "w", encoding="utf-8") as f:
    f.write("1234\n")
```

| モード | 意味 |
| --- | --- |
| `"r"` | 読み込み（省略時のデフォルト） |
| `"w"` | 書き込み（既存の内容は消えて上書きされる） |
| `"a"` | 追記（末尾に追加） |

> ステージデータの読み込みは、まさにこの `with open(...) as f:` の形。「ファイルを開いて → 使い終わったら閉じる」という一連の流れを `with` が面倒みてくれている。

---

## JSON でデータを保存する

辞書やリストのデータを、ファイルに保存したり読み込んだりできる形式。ハイスコアやセーブデータの保存によく使う。

```python
import json

data = {"name": "勇者", "score": 1200, "cleared": True}

# 保存する
with open("save.json", "w", encoding="utf-8") as f:
    json.dump(data, f)

# 読み込む
with open("save.json", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded["score"])   # → 1200
```

> JSON は Python の辞書・リストとほぼ同じ形（キーと値、配列）で書けるので相性がよい。ハイスコアランキングのように「複数のデータをまとめて保存したい」場面に向いている。

---

## lambda（無名関数）

`def` を使わずに、その場限りの小さな関数を作る書き方。

```python
# 通常の関数
def double(x):
    return x * 2

# lambda で書くと
double = lambda x: x * 2

double(5)   # → 10
```

書式：

```
lambda 引数: 式
```

### よく使う場面: `sorted()` の `key`

```python
scores = [{"name": "勇者", "score": 80}, {"name": "魔法使い", "score": 95}]

# score の大きい順に並べ替える
ranking = sorted(scores, key=lambda s: s["score"], reverse=True)
```

`sorted(リスト, key=..., reverse=True)` の `key` に「並べ替えの基準にする値を返す関数」を渡す。1回しか使わない小さな処理なので、わざわざ `def` で名前をつけずに lambda で済ませることが多い。

> 複雑な処理を書きたくなったら、素直に `def` で名前付きの関数にした方が読みやすい。

---

## zip() — 複数のリストを同時に処理する

複数の iterable を、同じ順番の要素どうしペアにして取り出す。

```python
names  = ["勇者", "魔法使い", "戦士"]
scores = [80, 95, 70]

for name, score in zip(names, scores):
    print(f"{name}: {score}点")
# 勇者: 80点
# 魔法使い: 95点
# 戦士: 70点
```

`enumerate()` が「1つのリストに番号をつけて回す」のに対し、`zip()` は**複数のリストを同時に回す**ときに使う。

> 「弾のリストと、対応する画像のリストを同時に処理したい」のような場面で使う。`for bullet, image in zip(bullets, images):` のように書ける。

---

## イテレータとジェネレータ

`for` ループで回せる値を、自分で作るための仕組み。

### イテレータ

`for` は内部的に、iterable からイテレータを取り出し、1つずつ値を取り出している。

```python
nums = [10, 20, 30]
it = iter(nums)      # イテレータを取り出す
next(it)              # → 10
next(it)              # → 20
next(it)              # → 30
next(it)              # → StopIteration（もう値が無い）
```

普段のコードでこれを直接書くことは少ないが、「`for` が裏で何をしているか」を知っておくと `StopIteration` のようなエラーメッセージを理解しやすくなる。

### ジェネレータ（yield）

`return` の代わりに `yield` を使うと、値を1つずつ返しながら途中の状態を覚えておける関数（ジェネレータ関数）になる。

```python
def countdown(n):
    while n > 0:
        yield n     # ここで一旦値を返し、次に呼ばれたら続きから再開する
        n -= 1

for i in countdown(3):
    print(i)    # 3 → 2 → 1
```

通常の関数がリストを `return` で丸ごと返すのに対し、ジェネレータは**値を1つずつ、必要になったときだけ計算する**。データ量が大きいときにメモリを節約できる。

```python
# リストで全部作る場合（すべてメモリに載る）
def all_positions(width, height):
    result = []
    for y in range(height):
        for x in range(width):
            result.append((x, y))
    return result

# ジェネレータの場合（1つずつしか作らない）
def all_positions_gen(width, height):
    for y in range(height):
        for x in range(width):
            yield (x, y)
```

### ジェネレータ式

リスト内包表記の `[]` を `()` に変えると、ジェネレータ式になる。

```python
squares = [x * x for x in range(5)]     # リスト内包表記 → リストを作る
squares_gen = (x * x for x in range(5)) # ジェネレータ式 → 1つずつ計算する
```

> このリポジトリのコードでは扱うデータ量が小さく、リストで十分間に合うことが多い。ジェネレータは「データ量が大きい・全部を一度に持ちたくない」ときの選択肢として知っておく。

---

## 標準ライブラリの概観

import するだけで使える、Python に最初から入っている便利な機能たち。

| モジュール | 用途 | よく使う機能 |
| --- | --- | --- |
| `random` | 乱数 | `random.randint(a, b)`, `random.choice(list)` |
| `sys` | プログラム制御 | `sys.exit()` |
| `pathlib` | ファイルパス | `Path(__file__).parent / "images"` |
| `math` | 数学関数 | `math.sqrt()`, `math.pi` |
| `time` | 時間 | `time.sleep(sec)` |
| `datetime` | 日付・時刻 | `datetime.datetime.now()` |
| `os` | OS 操作 | `os.listdir(".")`（フォルダの中身一覧） |
| `json` | JSON 形式の読み書き | `json.dump()`, `json.load()` |
| `re` | 正規表現 | `re.match()`, `re.findall()` |

### datetime の例

```python
import datetime

start = datetime.datetime.now()
# ...ゲームをプレイ...
end = datetime.datetime.now()
elapsed = end - start
print(f"プレイ時間: {elapsed.seconds}秒")
```

### os の例

```python
import os

files = os.listdir("images")   # フォルダの中のファイル名一覧を取得
print(files)   # → ['kaeru1.png', 'kaeru2.png', ...]
```

> すべて覚える必要はない。「こういう機能が欲しいときは標準ライブラリを探してみる」という発想を持っておくことが大事。

---

## 仮想環境（venv）とパッケージ

### なぜ仮想環境が必要か

複数のプロジェクトを扱っていると、「プロジェクト A は pygame 2.5系が必要だが、プロジェクト B は 2.6系が必要」のように、**プロジェクトごとに必要なライブラリのバージョンが異なる**ことがある。パソコン全体に1つしか Python 環境が無いと、この使い分けができない。

**仮想環境（venv）** は、プロジェクトごとに独立した Python 環境を作る仕組み。

### 作り方・使い方

```bash
# 仮想環境を作る（初回のみ）
python3 -m venv venv

# 仮想環境を有効にする（Mac/Linux）
source venv/bin/activate

# 仮想環境を有効にする（Windows）
venv\Scripts\activate

# 必要なライブラリをインストールする
pip install pygame

# 仮想環境を抜ける
deactivate
```

有効化すると、以降の `pip install` はこのプロジェクト専用の場所にインストールされ、他のプロジェクトに影響しない。

> このリポジトリでは `pip install pygame` のようにシステム全体にインストールする前提で進めてきたが、複数の Python プロジェクトを掛け持ちするようになったら venv を使う習慣をつけておくとよい。
