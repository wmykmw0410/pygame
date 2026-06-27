```text
基本版（../example/ex05.py）に難易度変化を追加した発展版です
python advanced/main.py で起動できます
```

# 追加した機能

得点に応じて UFO の速度と移動パターンが4段階に変化する。

| スコア | レベル | 速度 | 移動パターン | 背景色 |
| --- | --- | --- | --- | --- |
| 0〜99 | NORMAL | 4 | 真下に落下 | 紺 |
| 100〜199 | FAST | 7 | 速度アップ | 紫 |
| 200〜299 | ZIGZAG | 7 | サイン波で左右に揺れながら落下 | 暗緑 |
| 300〜 | CHASE | 10 | 自機を追尾しながら落下 | 暗赤 |

---

# 発展1 — 難易度テーブルと get_level()

サンプル: [main.py](main.py)

スコアを受け取ってその時点の難易度設定を返す関数を作る。
設定をコードに直接書かずにテーブルとしてまとめることで、調整しやすくなる。

## やること

```
step1. 難易度テーブル LEVELS をリストで作る
         各要素は辞書で「スコア閾値 / レベル名 / 速度 / 移動パターン / 背景色」を持つ
         スコアが高い順（CHASE → NORMAL）に並べる

step2. get_level(score) 関数を作る
         LEVELS を先頭から順に見ていく
         score >= lv["min_score"] になった最初の要素を返す
         スコアが高い順に並んでいるので、最初にマッチしたものが正しいレベルになる
```

<details>
<summary>コードを見る</summary>

```python
LEVELS = [
    {"min_score": 300, "name": "CHASE",  "speed": 10, "move": "chase",  "bg": (60,  0,   0)},
    {"min_score": 200, "name": "ZIGZAG", "speed":  7, "move": "zigzag", "bg": (0,   50,  0)},
    {"min_score": 100, "name": "FAST",   "speed":  7, "move": "fast",   "bg": (50,  0,  80)},
    {"min_score":   0, "name": "NORMAL", "speed":  4, "move": "normal", "bg": (0,   0, 128)},
]

def get_level(score):
    for lv in LEVELS:
        if score >= lv["min_score"]:
            return lv
    return LEVELS[-1]
```

</details>

---

# 発展2 — UFO.set_difficulty()

サンプル: [main.py](main.py)

`get_level()` を使って UFO の速度と移動パターンを更新するメソッドを追加する。
ゲームループから毎フレーム呼ぶことで、スコアが上がった瞬間に UFO が変化する。

## やること

```
step1. UFO クラスに speed と move_type の属性を追加する
         __init__ で self.speed = 4, self.move_type = "normal" として初期化する

step2. set_difficulty(self, score) メソッドを追加する
         get_level(score) を呼んで lv を取得する
         self.speed     = lv["speed"] で速度を更新する
         self.move_type = lv["move"]  で移動パターンを更新する

step3. ゲームループの UFO 処理で ufo.set_difficulty(score) を呼ぶ
         update() の前に呼ぶことで、その時点のスコアが反映される
```

<details>
<summary>コードを見る</summary>

```python
class UFO:
    def __init__(self, img, x, y):
        self.img       = img
        self.rect      = pg.Rect(x, y, 50, 50)
        self.speed     = 4
        self.move_type = "normal"
        self.phase     = random.randint(0, 360)

    def set_difficulty(self, score):
        lv             = get_level(score)
        self.speed     = lv["speed"]
        self.move_type = lv["move"]
```

```python
# ゲームループ内
for ufo in ufos:
    ufo.set_difficulty(score)   # ← 毎フレーム更新
    ufo.update(myship.rect.x)
    ufo.draw()
```

</details>

---

# 発展3 — 移動パターンの実装

サンプル: [main.py](main.py)

`update()` の中で `move_type` を見て3種類の動きを分岐する。

```
normal / fast   → 真下に落下するだけ（speed の大きさだけ違う）
zigzag          → サイン波で X 座標を左右に動かしながら落下する
chase           → 毎フレーム自機の X 座標に近づきながら落下する
```

## やること — zigzag

```
step1. UFO.__init__ に self.phase = random.randint(0, 360) を追加する
         各 UFO の初期位相をずらすことで、一斉に同じ方向へ動くのを防ぐ

step2. update() で move_type == "zigzag" のとき
         self.phase += 3  で位相を毎フレーム進める
         dx = int(math.sin(math.radians(self.phase)) * 6)  で左右の移動量を計算する
         self.rect.x += dx  で X 座標を更新する
         X 座標が画面外に出たら 0 または 750 に戻す

step3. respawn() でも self.phase をランダムにリセットする
         復活するたびに位相が変わり、動きにバリエーションが生まれる
```

## やること — chase

```
step1. update(self, ship_x) の引数に ship_x を追加する
         ゲームループから myship.rect.x を渡す

step2. move_type == "chase" のとき
         target_x = ship_x - 25  で自機の中心 X に合わせた目標座標を計算する
         self.rect.x が target_x より小さければ +3 する
         self.rect.x が target_x より大きければ -3 する
```

<details>
<summary>コードを見る</summary>

```python
import math

class UFO:
    def __init__(self, img, x, y):
        ...
        self.phase = random.randint(0, 360)   # 追加

    def update(self, ship_x):
        self.rect.y += self.speed

        if self.move_type == "zigzag":
            self.phase += 3
            dx = int(math.sin(math.radians(self.phase)) * 6)
            self.rect.x += dx
            if self.rect.x < 0:
                self.rect.x = 0
            if self.rect.x > 750:
                self.rect.x = 750

        elif self.move_type == "chase":
            target_x = ship_x - 25
            if self.rect.x < target_x:
                self.rect.x += 3
            elif self.rect.x > target_x:
                self.rect.x -= 3

        if self.rect.y > 600:
            self.respawn()

    def respawn(self):
        self.rect.x = random.randint(0, 750)
        self.rect.y = -100
        self.phase  = random.randint(0, 360)   # 追加
```

```python
# ゲームループ内（ship_x を渡す）
ufo.update(myship.rect.x)
```

</details>

---

# 発展4 — HUD 表示

サンプル: [main.py](main.py)

現在のレベル名と「次のレベルまでの残りスコア」を画面に表示する。
背景色をレベルごとに変えることで、難易度が上がったことを視覚的に伝える。

## やること

```
step1. 背景色を lv["bg"] から取得する
         get_level(score) の戻り値から bg を取り出して screen.fill() に渡す

step2. レベル名を画面左上に表示する
         font.render("LEVEL: " + lv["name"], ...) で文字を作り screen.blit() で描画する

step3. 次のレベルまでの残りスコアを表示する
         LEVELS を reversed() でスコアが低い順に走査する
         score < lv_data["min_score"] が成り立つ最初の要素が次のレベルになる
         残り = next_score - score を計算して表示する
         最高レベル（CHASE）に達したときは表示しない
```

<details>
<summary>コードを見る</summary>

```python
def gamestage():
    global page, score
    lv = get_level(score)
    screen.fill(lv["bg"])          # レベルに応じた背景色

    ...

    font  = pg.font.Font(None, 40)
    small = pg.font.Font(None, 28)

    score_text = font.render("SCORE: " + str(score), True, pg.Color("WHITE"))
    screen.blit(score_text, (20, 20))

    lv_text = font.render("LEVEL: " + lv["name"], True, pg.Color("YELLOW"))
    screen.blit(lv_text, (20, 58))

    # 次のレベルまでの残りスコアを表示
    next_score = 0
    for lv_data in reversed(LEVELS):
        if lv_data["min_score"] > score:
            next_score = lv_data["min_score"]
            break
    if next_score > 0:
        remain = next_score - score
        hint = small.render("NEXT LV: " + str(remain) + " pts", True, pg.Color("LIGHTGRAY"))
        screen.blit(hint, (20, 90))
```

</details>
