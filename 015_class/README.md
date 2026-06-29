```text
クラスを使って、データと処理を1つにまとめる方法を学びましょう
```

# 目次
- [目次](#目次)
- [クラスとは](#クラスとは)
- [クラスの定義](#クラスの定義)
  - [属性の種類: インスタンス変数とクラス変数](#属性の種類-インスタンス変数とクラス変数)
- [インスタンスの生成と利用](#インスタンスの生成と利用)
  - [Q1. カウンタークラス](#q1-カウンタークラス)
- [複数のインスタンス](#複数のインスタンス)
  - [Q2. キャラクタークラス](#q2-キャラクタークラス)
- [継承](#継承)
  - [Q3. 敵クラスを継承で作る](#q3-敵クラスを継承で作る)

---

# クラスとは

「**関連するデータと処理を1つにまとめたもの**」

たとえばアドベンチャーゲームのプレイヤーは「名前・HP（データ）」と「ダメージを受ける・状態を表示する（処理）」をセットで持っている。

関数だけで書くと、データと処理が離れてしまう。

```python
player_name = "勇者"
player_hp   = 100

def take_damage(hp, amount):
    return hp - amount

def show_status(name, hp):
    print(f"{name} HP: {hp}")
```

プレイヤーが複数になると、変数がさらに増えていく。

```python
# ❌ 増やすほど管理が大変になる
player1_name = "勇者"
player1_hp   = 100
player2_name = "魔法使い"
player2_hp   = 80
```

クラスにまとめると、プレイヤー1人 = インスタンス1つで扱える。

```python
p1 = Player("勇者",   100)
p2 = Player("魔法使い", 80)

p1.take_damage(30)  # p1 だけ HP が減る
```

---

# クラスの定義

```python
class クラス名():
    def __init__(self, 引数):
        self.属性名 = 初期値

    def メソッド名(self):
        処理
```

| キーワード | 役割 |
| --- | --- |
| `class` | クラスの定義を開始する |
| `__init__` | インスタンスが作られるときに自動で呼ばれる（初期化処理） |
| `self` | そのインスタンス自身を指す。メソッドの第1引数に必ず書く |
| `self.属性名` | インスタンスごとに独立したデータを保持する（インスタンス変数） |

サンプル: [example/ex01.py](example/ex01.py)

<details>
<summary>コードを見る</summary>

```python
class Player():
    def __init__(self, name, hp):
        self.name = name    # インスタンスごとのデータ
        self.hp   = hp

    def take_damage(self, amount):
        self.hp -= amount

    def show_status(self):
        print(f"{self.name} HP: {self.hp}")
```

</details>

## 属性の種類: インスタンス変数とクラス変数

クラスが持つ**属性**には2種類ある。

| 種類 | 書く場所 | 特徴 |
| --- | --- | --- |
| インスタンス変数 | `__init__` 内に `self.変数名` | インスタンスごとに独立した値を持つ |
| クラス変数 | クラス直下（`__init__` の外）に `変数名` | 全インスタンスで共有される |

```python
class Player():
    party_count = 0           # クラス変数: パーティーの人数（全員で共有）

    def __init__(self, name, hp):
        self.name = name          # インスタンス変数: 各プレイヤー固有
        self.hp   = hp
        Player.party_count += 1  # インスタンスが作られるたびに増やす

p1 = Player("勇者",    100)
p2 = Player("魔法使い",  80)
p3 = Player("戦士",    120)

print(Player.party_count)   # 3  ← 全インスタンスで共有
print(p1.name)              # 勇者（p1 固有）
print(p2.name)              # 魔法使い（p2 固有、p1 とは独立）
```

クラス変数を変更するときは `クラス名.変数名` で行う。`self.変数名` で書き換えると、そのインスタンスだけの変数として上書きされてしまう。

```python
Player.party_count = 0    # ✅ クラス変数を変更
p1.party_count     = 0    # ❌ p1 専用のインスタンス変数が新たに作られてしまう
```

---

# インスタンスの生成と利用

```python
# 生成: クラス名() でインスタンスを作る
player = Player("勇者", 100)

# 属性へのアクセス
print(player.name)   # 勇者
print(player.hp)     # 100

# メソッドの呼び出し
player.take_damage(30)
player.show_status()  # 勇者 HP: 70

player.take_damage(20)
player.show_status()  # 勇者 HP: 50
```

## Q1. カウンタークラス

> 問題: [question/question1.py](question/question1.py) / 解答: [question/answer/answer1.py](question/answer/answer1.py)

---

# 複数のインスタンス

クラスからインスタンスをいくつでも作れる。**それぞれのデータは独立している**。

```python
p1 = Player("勇者",    100)
p2 = Player("魔法使い",  80)

p1.take_damage(30)
print(p1.hp)   # 70
print(p2.hp)   # 80  ← p2 は変わっていない
```

インスタンスをリストで管理すると、まとめて処理できる。

```python
party = [Player("勇者", 100), Player("魔法使い", 80), Player("戦士", 120)]

for p in party:
    p.take_damage(10)   # 全員まとめてダメージを与える

for p in party:
    p.show_status()
```

サンプル: [example/ex02.py](example/ex02.py)

> pygame でのクラス活用は、このページ末尾の **「pygame で段階的に作る」** を参照。

## Q2. キャラクタークラス

> 問題: [question/question2.py](question/question2.py) / 解答: [question/answer/answer2.py](question/answer/answer2.py)

---

# 継承

既存のクラスを**元にして新しいクラスを作る**方法。  
共通の処理を親クラスに書いておき、子クラスで差分だけを追加・上書きする。

```
Animal（親クラス）
  ├── Dog  ← speak() を上書き
  └── Cat  ← speak() を上書き
```

```python
class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}: ...")

class Dog(Animal):           # Animal を継承
    def speak(self):         # 親の speak を上書き（オーバーライド）
        print(f"{self.name}: ワン！")

class Cat(Animal):
    def speak(self):
        print(f"{self.name}: ニャー！")
```

子クラス独自の属性を追加したい場合は `super().__init__()` で親の初期化を呼ぶ。

```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)    # 親の __init__ を先に呼ぶ
        self.breed = breed        # Dog だけが持つ属性（インスタンス変数）
```

種類が違っても同じメソッド名で呼び出せる。

```python
animals = [Dog("シロ"), Cat("クロ"), Dog("ハチ")]
for a in animals:
    a.speak()   # Dog は「ワン！」、Cat は「ニャー！」とそれぞれ動く
```

サンプル: [example/ex03.py](example/ex03.py)

## Q3. 敵クラスを継承で作る

> 問題: [question/question3.py](question/question3.py) / 解答: [question/answer/answer3.py](question/answer/answer3.py)