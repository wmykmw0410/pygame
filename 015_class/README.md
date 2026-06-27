```text
クラスを使って、データと処理を1つにまとめる方法を学びましょう
```

# 目次
- [クラスとは](#クラスとは)
- [クラスの定義](#クラスの定義)
  - [属性の種類: インスタンス変数とクラス変数](#属性の種類-インスタンス変数とクラス変数)
- [インスタンスの生成と利用](#インスタンスの生成と利用)
- [複数のインスタンス](#複数のインスタンス)
- [継承](#継承)
- [pygame で段階的に作る](#pygame-で段階的に作る)

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

`Counter` クラスを作ろう。

- 属性（インスタンス変数）: `count = 0`
- `increment()` → count を 1 増やす
- `decrement()` → count を 1 減らす（0 未満にはならない）
- `reset()` → count を 0 に戻す
- `show()` → 現在の count を表示する

以下の手順で動作を確認する。

```
1. Counter() でインスタンスを作る
2. increment() を 3 回呼んで show() → 3 が表示される
3. decrement() を 1 回呼んで show() → 2 が表示される
4. reset() を呼んで show() → 0 が表示される
```

解答: [answer/Q1_ans.py](answer/Q1_ans.py)

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

`Character` クラスを作って、2体のキャラクターを戦わせよう。

- 属性（インスタンス変数）: `name`, `hp = 100`, `attack_power`
- `attack(target)` → `target.hp` を `attack_power` 分減らし、結果を表示する
- `is_alive()` → `hp > 0` なら `True` を返す

```
戦闘の流れ:
1. hero = Character("勇者", attack_power=30) を作る
2. demon = Character("魔王", attack_power=20) を作る
3. どちらかの is_alive() が False になるまで交互に attack() を呼ぶ
4. 倒したほうを表示する
```

解答: [answer/Q2_ans.py](answer/Q2_ans.py)

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

Q2 で作った `Character` を親クラスとして、`Enemy` クラスを作ろう。

```
step1. Enemy(Character) を定義する
         __init__(self, name, attack_power) で super() を呼ぶ
         Enemy 専用のプロパティとして hp = 150 を設定する

step2. attack() をオーバーライドする
         攻撃力を 1.5 倍にして target.hp を減らす（int に変換する）
         攻撃結果を表示する

step3. 以下で戦わせる
         hero = Character("勇者", attack_power=30)
         boss = Enemy("ラスボス", attack_power=15)
```

> 次の `016_BreakoutClone_class_ver` `017_shooting_game_class_ver` では、既存ゲームを段階的にクラス化する練習をする。  
> `019_frog_blaster` では、クラスの考え方を活かしてゼロからゲームを設計する。

解答: [answer/Q3_ans.py](answer/Q3_ans.py)

---

# pygame で段階的に作る

ここまで学んだクラスの知識を使って、バトルゲームを **4ステップ** で作っていく。  
各ファイルを順番に動かしながら、どこが変わったかを確認しよう。

| ファイル | 内容 |
| --- | --- |
| [ex01.py](example/ex01.py) | Player クラスの基本（純Python） |
| [ex02.py](example/ex02.py) | 複数インスタンスとリスト（純Python） |
| [ex03.py](example/ex03.py) | 継承 Animal / Dog / Cat（純Python） |
| [ex04.py](example/ex04.py) | pygame で関数だけで書く |
| [ex05.py](example/ex05.py) | pygame で Player クラスに変換 |
| [ex06.py](example/ex06.py) | pygame で Enemy クラスを追加 |
| [ex07.py](example/ex07.py) | pygame で攻撃ターンを実装（完成） |

---

## ex04 — 関数だけで書いてみる

サンプル: [example/ex04.py](example/ex04.py)

プレイヤー3人分のデータを**変数と関数**で管理する。  
→ 変数名がどんどん増えて管理しにくいことを確認する。

```python
name1, hp1, color1 = "勇者",    100, pg.Color("ROYALBLUE")
name2, hp2, color2 = "魔法使い",  70, pg.Color("PURPLE")
name3, hp3, color3 = "戦士",    130, pg.Color("FIREBRICK")

def draw_player(name, cx, color, hp):
    ...

draw_player(name1, 100, color1, hp1)
draw_player(name2, 300, color2, hp2)
draw_player(name3, 500, color3, hp3)
```

---

## ex05 — Player クラスにまとめる

サンプル: [example/ex05.py](example/ex05.py)

ex04 の変数と関数を `Player` クラスに集約する。  
→ リストに入れてまとめて処理できるようになることを確認する。

```python
class Player():
    def __init__(self, name, cx, color, hp):
        self.name  = name
        self.hp    = hp
        self.rect  = pg.Rect(cx - 30, 200, 60, 60)
        self.color = color

    def take_damage(self, amount): ...
    def draw(self):               ...

party = [Player("勇者", 100, ...), Player("魔法使い", 300, ...), Player("戦士", 500, ...)]

for p in party:
    p.draw()    # まとめて描画
```

---

## ex06 — Enemy クラスを追加する

サンプル: [example/ex06.py](example/ex06.py)

`Enemy` クラスを追加し、SPACE キーでパーティーが攻撃できるようにする。  
→ 複数のクラスが連携して動くことを確認する。

```python
class Enemy():
    def __init__(self, name, hp): ...
    def draw(self):               ...

enemy = Enemy("スライム", 80)

# SPACE → ランダムな1人が攻撃
alive = []
for p in party:
    if p.is_alive():
        alive.append(p)
attacker = random.choice(alive)
enemy.hp -= attacker.attack
```

---

## ex07 — 攻撃ターンを追加する（完成）

サンプル: [example/ex07.py](example/ex07.py)

ex06 に**敵の反撃**と**勝敗判定**を追加して完成。

```python
# パーティーの攻撃後、敵が反撃する
alive = []
for p in party:
    if p.is_alive():
        alive.append(p)
target = random.choice(alive)
target.take_damage(enemy.attack)

# 勝敗判定
if not enemy.is_alive():
    message = "スライムをたおした！"

party_alive = False
for p in party:
    if p.is_alive():
        party_alive = True
if not party_alive:
    message = "パーティーは全滅した…"
```
