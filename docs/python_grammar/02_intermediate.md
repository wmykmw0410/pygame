# Python 文法（中級）

関数・クラス・例外処理・モジュールなど、プログラムを「部品」として整理するための文法。[基礎](01_basic.md)を一通り終えてから読むことを想定している。

## 目次
- [関数](#関数)
  - [戻り値](#戻り値)
  - [デフォルト引数](#デフォルト引数)
  - [キーワード引数](#キーワード引数)
  - [`*args` と `**kwargs`](#args-と-kwargs)
  - [スコープ](#スコープ)
- [組み込み関数](#組み込み関数)
- [クラス](#クラス)
  - [クラス変数とインスタンス変数](#クラス変数とインスタンス変数)
  - [継承](#継承)
  - [多重継承](#多重継承)
- [例外処理](#例外処理)
- [モジュール](#モジュール)

---

## 関数

```python
def greet(name):
    print(f"こんにちは、{name}!")

greet("勇者")   # → こんにちは、勇者!
```

### docstring（関数の説明を書く）

関数の中身の先頭に文字列（`"""..."""`）だけを書くと、その関数の説明として扱われる。

```python
def take_damage(hp, amount):
    """HP から amount を引いた値を返す（0未満にはならない）"""
    return max(0, hp - amount)

print(take_damage.__doc__)   # → HP から amount を引いた値を返す（0未満にはならない）
```

> IDEの補完やヘルプ表示で読める「関数の説明書」のようなもの。コメント（`#`）と違い、`__doc__` として実行時にも読み出せる。

### 戻り値

```python
def add(a, b):
    return a + b

result = add(3, 4)   # 7
```

### デフォルト引数

```python
def take_damage(hp, amount=10):
    return max(0, hp - amount)

take_damage(80)        # amount=10 として計算 → 70
take_damage(80, 30)    # amount=30 として計算 → 50
```

### キーワード引数

```python
def create_player(name, hp=100, attack=20):
    return {"name": name, "hp": hp, "attack": attack}

create_player("勇者", attack=30)   # hp はデフォルト値
```

### `*args` と `**kwargs`

呼び出し側が渡す引数の**数が決まっていない**ときに使う書き方。

```python
def total_damage(*hits):        # 好きな数の位置引数をタプルとして受け取る
    return sum(hits)

total_damage(10, 20, 30)        # → 60
total_damage(5)                 # → 5
```

```python
def create_status(**params):    # 好きな数のキーワード引数を辞書として受け取る
    return params

create_status(hp=100, mp=30, attack=15)
# → {'hp': 100, 'mp': 30, 'attack': 15}
```

`*args` は「名前を付けていない追加の位置引数」、`**kwargs` は「名前を付けていない追加のキーワード引数」をまとめて受け取る。2つを同時に使うこともできる。

```python
def spawn_enemy(name, *skills, **stats):
    print(name, skills, stats)

spawn_enemy("ドラゴン", "火炎", "咆哮", hp=300, attack=50)
# → ドラゴン ('火炎', '咆哮') {'hp': 300, 'attack': 50}
```

### 呼び出し時のアンパック

`*`/`**` は、関数を定義するときだけでなく、**呼び出すとき**にも使える。リストや辞書の中身を展開して、複数の引数として渡せる。

```python
def create_status(name, hp, attack):
    return f"{name} HP:{hp} 攻撃:{attack}"

params = ["勇者", 100, 20]
create_status(*params)   # リストを展開して渡す → create_status("勇者", 100, 20) と同じ

params = {"name": "勇者", "hp": 100, "attack": 20}
create_status(**params)  # 辞書を展開してキーワード引数として渡す
```

> 敵の初期値をまとめた辞書から `Enemy(**enemy_data)` のように直接インスタンスを作る、といった場面で使える。

### キーワード専用引数・位置専用引数

引数の並びに `*` や `/` を入れることで、渡し方を制限できる。

```python
def create_enemy(name, *, hp=100):   # * の後ろはキーワード引数でしか渡せない
    ...

create_enemy("スライム", hp=50)   # OK
create_enemy("スライム", 50)      # → TypeError（位置引数では渡せない）
```

```python
def move(x, y, /):   # / の前は位置引数でしか渡せない
    ...

move(1, 2)         # OK
move(x=1, y=2)      # → TypeError（キーワード引数では渡せない）
```

> 普段のコードでは省略してよい。「意図しない渡し方をされたくない」ときに使う仕組み、という理解で十分。

### スコープ

変数が「どこから使えるか」の範囲のこと。

```python
hp = 100   # グローバル変数（どこからでも読める）

def show_hp():
    print(hp)   # 外の変数を読むことはできる

show_hp()   # → 100
```

**関数の中で作った変数は外から使えない**

```python
def calc():
    result = 42   # ローカル変数（この関数の中だけ有効）

calc()
print(result)   # → NameError: name 'result' is not defined
```

**関数の中から外の変数を書き換えるには `global` を使う**

```python
score = 0

def add_score(n):
    global score      # 外の score を使うと宣言する
    score += n

add_score(10)
print(score)   # → 10
```

> `global` を多用するとバグが起きやすくなる。
> 関数には引数で値を渡し、戻り値で返すのが基本。

---

## 組み込み関数

import なしで最初から使える関数。

| 関数 | 説明 | 例 |
| --- | --- | --- |
| `len(x)` | 要素数・文字数を返す | `len([1,2,3])` → `3` |
| `max(x)` | 最大値を返す | `max([3,1,2])` → `3` |
| `min(x)` | 最小値を返す | `min([3,1,2])` → `1` |
| `sum(x)` | 合計を返す | `sum([1,2,3])` → `6` |
| `abs(x)` | 絶対値を返す | `abs(-5)` → `5` |
| `round(x, n)` | 小数を四捨五入 | `round(3.14, 1)` → `3.1` |
| `range(n)` | 連番を生成する | `range(3)` → `0, 1, 2` |
| `print(x)` | 値を表示する | `print("hello")` |
| `input(s)` | キーボード入力を受け取る | `input("名前: ")` |
| `type(x)` | 型を返す | `type(42)` → `<class 'int'>` |
| `int(x)` | 整数に変換する | `int("42")` → `42` |
| `str(x)` | 文字列に変換する | `str(42)` → `"42"` |
| `float(x)` | 小数に変換する | `float("3.14")` → `3.14` |
| `bool(x)` | 真偽値に変換する | `bool(0)` → `False` |
| `sorted(x)` | 並べ替えた**新しいリスト**を返す（元は変えない） | `sorted([3,1,2])` → `[1,2,3]` |
| `reversed(x)` | 逆順に並べ替えたイテレータを返す | `list(reversed([1,2,3]))` → `[3,2,1]` |

```python
# pygame でよく使う組み合わせ
hp_list = [100, 70, 130]

total    = sum(hp_list)            # 合計 HP: 300
strongest = max(hp_list)           # 最大 HP: 130
distance  = abs(enemy_x - my_x)   # 距離（負にならない）
```

**`sort()` と `sorted()` の違い**

```python
nums = [3, 1, 2]

nums.sort()          # 元のリストを直接書き換える（戻り値は None）
new_nums = sorted(nums)   # 新しいリストを返す（元は変わらない）
```

---

## クラス

データ（属性）と処理（メソッド）をひとまとめにしたもの。

```python
class Player:
    def __init__(self, name, hp):   # コンストラクタ（インスタンス生成時に呼ばれる）
        self.name = name
        self.hp   = hp

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0

    def __str__(self):              # print() で表示される文字列
        return f"{self.name} HP:{self.hp}"


p = Player("勇者", 100)
p.take_damage(30)
print(p.is_alive())   # True
print(p)              # 勇者 HP:70
```

### クラス変数とインスタンス変数

```python
class Enemy:
    count = 0   # クラス変数: すべてのインスタンスで共有される

    def __init__(self, name, hp):
        self.name = name   # インスタンス変数: インスタンスごとに別の値を持つ
        self.hp   = hp
        Enemy.count += 1   # クラス変数はクラス名経由で書き換える


e1 = Enemy("スライム", 50)
e2 = Enemy("ゴブリン", 40)
print(Enemy.count)   # → 2（e1, e2 で共有されている）
print(e1.hp, e2.hp)  # → 50 40（それぞれ別の値）
```

> クラス変数は「そのクラスから作られた全インスタンスで共通の値」（例: 出現した敵の総数）、インスタンス変数は「インスタンスごとに違う値」（例: 個々のHP）を持たせたいときに使い分ける。

### 非公開っぽい変数（参考）

Python には「本当に外から見えなくする」仕組みは無いが、慣習として先頭に `_` を付けることで「内部でしか使わない想定」を伝えられる。

```python
class Enemy:
    def __init__(self, hp):
        self._hp = hp   # 「外から直接いじらないでほしい」という意図を示す
```

> このリポジトリのコードでは、学習のシンプルさを優先してこの慣習をあえて使わず `self.hp` のようにプレーンな属性名で統一している（詳しくは `CLAUDE.md` のコーディング規約を参照）。「`_` 接頭辞にはこういう意味がある」と知っておけば十分。

### 継承

既存クラスの機能を引き継いで新しいクラスを作る。

```python
class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp   = hp

    def is_alive(self):
        return self.hp > 0


class Enemy(Character):             # Character を継承
    def __init__(self, name, hp, attack):
        super().__init__(name, hp)  # 親クラスの __init__ を呼ぶ
        self.attack = attack

    def describe(self):
        print(f"{self.name} HP:{self.hp} 攻撃:{self.attack}")


slime = Enemy("スライム", 50, 10)
slime.describe()          # スライム HP:50 攻撃:10
print(slime.is_alive())   # True（継承した is_alive を使える）
```

### 多重継承

Python は、複数のクラスを同時に継承できる。

```python
class Swimmer:
    def swim(self):
        print("泳ぐ")


class Flyer:
    def fly(self):
        print("飛ぶ")


class Dragon(Swimmer, Flyer):   # 2つのクラスを同時に継承
    pass


d = Dragon()
d.swim()   # → 泳ぐ（Swimmer から）
d.fly()    # → 飛ぶ（Flyer から）
```

同じ名前のメソッドが複数の親クラスにある場合、**先に書いたクラスの方が優先される**（`class Dragon(Swimmer, Flyer):` なら `Swimmer` が優先）。

> 継承元が増えるほど「どのメソッドがどこから来たか」が分かりにくくなる。「複数の役割を持たせたい」ときは、多重継承ではなく別クラスのインスタンスを属性として持たせる方法（コンポジション）で解決できないか、先に検討するとよい。

---

## 例外処理

エラーが起きても処理を続けるための仕組み。

```python
try:
    n = int(input("数を入力: "))
    print(10 / n)
except ValueError:
    print("数値を入力してください")
except ZeroDivisionError:
    print("0 では割れません")
finally:
    print("処理終了")   # 例外の有無に関わらず実行される
```

### else 節: 例外が起きなかったときだけ実行する

`try` には `else` も付けられる。**例外が起きなかったときだけ**実行したい処理を書ける。

```python
try:
    n = int(input("数を入力: "))
except ValueError:
    print("数値を入力してください")
else:
    print(f"{n} を受け取りました")   # 例外が起きなかったときだけ実行される
finally:
    print("処理終了")                # 例外の有無に関わらず実行される
```

「エラーになり得る処理（`try`）」と「成功したときだけやりたい処理（`else`）」を分けて書けるため、どこで例外が起きたのかが分かりやすくなる。

### よくある例外

| 例外 | 発生する状況 |
| --- | --- |
| `ValueError` | 型変換に失敗（`int("abc")` など） |
| `IndexError` | リストの範囲外アクセス（`list[99]` など） |
| `KeyError` | 辞書に存在しないキー |
| `ZeroDivisionError` | 0 で割る |
| `FileNotFoundError` | ファイルが見つからない |
| `TypeError` | 型が合わない演算 |

### 自分で例外を発生させる（raise）

```python
def set_hp(hp):
    if hp < 0:
        raise ValueError("HPは0以上にしてください")
    return hp

set_hp(-10)   # → ValueError: HPは0以上にしてください
```

`raise` は「ここでエラーとして処理を止めたい」ときに使う。呼び出し側は通常の例外と同じように `try/except` で受け止められる。

### 自分で例外クラスを作る

`Exception` を継承したクラスを作ると、そのゲーム独自の例外として使える。

```python
class GameOverError(Exception):
    pass


def take_damage(hp, amount):
    hp -= amount
    if hp <= 0:
        raise GameOverError("HPが0になった")
    return hp


try:
    take_damage(10, 20)
except GameOverError as e:
    print(f"ゲームオーバー: {e}")   # → ゲームオーバー: HPが0になった
```

> `except GameOverError as e:` の `e` には、`raise` したときに渡したメッセージを持つ例外オブジェクトが入る。

---

## モジュール

### import の書き方

```python
import pygame                # pygame をそのまま使う
import pygame as pg          # pg という名前で使う（よく使う略記）
import sys                   # sys モジュール

from pathlib import Path     # pathlib から Path だけ取り込む
from random import randint   # random から randint だけ取り込む
```

### よく使う標準モジュール

| モジュール | 用途 | よく使う機能 |
| --- | --- | --- |
| `random` | 乱数 | `random.randint(a, b)`, `random.choice(list)` |
| `sys` | プログラム制御 | `sys.exit()` |
| `pathlib` | ファイルパス | `Path(__file__).parent / "images"` |
| `math` | 数学関数 | `math.sqrt()`, `math.pi` |
| `time` | 時間 | `time.sleep(sec)` |

標準モジュールをもっと広く知りたい場合は[発展編の「標準ライブラリの概観」](03_advanced.md#標準ライブラリの概観)を参照。

### `if __name__ == "__main__":`

スクリプトが「直接実行されたとき」と「他のファイルから import されたとき」で動作を分けるための定番の書き方。

```python
def greet(name):
    print(f"こんにちは、{name}!")

if __name__ == "__main__":
    greet("勇者")   # このファイルを直接実行したときだけ動く
```

このファイルを `python3 xxx.py` のように直接実行すると `__name__` は `"__main__"` になり、`if` の中身が実行される。一方、他のファイルから `import xxx` された場合は `__name__` が `"xxx"`（モジュール名）になるため、`if` の中身は実行されない。

> `greet()` のような関数だけを別ファイルから使い回したいが、このファイル単体でも動作確認したい、というときに使う。
