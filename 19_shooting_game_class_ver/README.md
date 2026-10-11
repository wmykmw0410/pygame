```text
14_shooting_game の関数ベースのコードを、クラスを使って段階的に書き直します
```

# pygame で段階的にクラス化する（シューティングゲーム）

[14_shooting_game](../14_shooting_game/) の完成コード（関数ベース）を出発点に、  
自機・UFO・弾を順番にクラスに変換していく。

| ファイル | 追加するクラス | ポイント |
| --- | --- | --- |
| [ex01.py](example/ex01.py) | なし（関数ベースの出発点） | `myrect` / `ufos` / `bulletrect` がバラバラに存在する |
| [ex02.py](example/ex02.py) | `MyShip` | 1つのインスタンス・一番シンプル |
| [ex03.py](example/ex03.py) | `MyShip` + `UFO` | リストで複数インスタンスを管理 |
| [ex04.py](example/ex04.py) | `MyShip` + `UFO` + `Bullet` | `is_active()` で発射状態を管理 |
| [ex05.py](example/ex05.py) | `MyShip` + `UFO` + `Bullet` | UFO に `speed` 属性を追加してインスタンスごとに速さを変える完成形 |
| [ex06.py](example/ex06.py) | 変更なし（`UFO` に難易度システムを追加） | スコアに応じて速度・移動パターン・背景色が段階的に変化する発展版 |

---

# ex01 → ex02: MyShip クラスに書き直す

サンプル: [ex02.py](example/ex02.py)

`myimg` と `myrect` がバラバラに存在していた自機のデータと処理を `MyShip` クラスに集約する。

## やること

```
step1. MyShip クラスを作る
         __init__(self, img) で self.img と self.rect を持たせる
         self.rect = pg.Rect(400, 500, SHIP_SIZE, SHIP_SIZE) で初期位置を設定する

step2. update(self, mx) を追加する
         self.rect.x = mx - SHIP_SIZE // 2 でマウスの X 座標に追随する

step3. draw(self) を追加する
         screen.blit(self.img, self.rect) で描画する

step4. reset(self) を追加する
         gamereset() から呼ぶ用に初期位置に戻す処理をまとめる

step5. ゲームループと gamereset() を書き直す
         myrect.x = mx - SHIP_SIZE // 2 → myship.update(mx)
         screen.blit(myimg, myrect) → myship.draw()
         myrect.x = 400; myrect.y = 500 → myship.reset()
```

<details>
<summary>コードを見る</summary>

```python
SHIP_SIZE = 50


class MyShip():
    def __init__(self, img):
        self.img  = img
        self.rect = pg.Rect(400, 500, SHIP_SIZE, SHIP_SIZE)

    def update(self, mx):
        self.rect.x = mx - SHIP_SIZE // 2

    def draw(self):
        screen.blit(self.img, self.rect)

    def reset(self):
        self.rect.x = 400
        self.rect.y = 500


myimg  = pg.image.load(IMG_DIR / "myship.png")
myimg  = pg.transform.scale(myimg, (SHIP_SIZE, SHIP_SIZE))
myship = MyShip(myimg)
```

```python
# gamestage() 内
myship.update(mx)
myship.draw()
```

```python
# gamereset() 内
myship.reset()
```

</details>

---

# ex02 → ex03: UFO クラスに書き直す

サンプル: [ex03.py](example/ex03.py)

`ufos` リストの中が `pg.Rect` だったものを `UFO` インスタンスに変える。  
複数インスタンスをリストで管理するパターンを確認する。

## やること

```
step1. UFO クラスを作る
         __init__(self, img, x, y) で self.img と self.rect を持たせる

step2. update(self) を追加する
         self.rect.y += UFO_SPEED で下に移動する
         画面外に出たら self.rect.x / y をリセットして再登場させる

step3. draw(self) を追加する
         screen.blit(self.img, self.rect) で描画する

step4. respawn(self) を追加する
         撃墜されたときや gamereset() から呼ぶ用にランダム位置に戻す処理をまとめる

step5. ufos リストの作り方を変える
         pg.Rect(ux, uy, UFO_SIZE, UFO_SIZE) の代わりに UFO(ufoimg, x, y) を append する

step6. ゲームループと gamereset() を書き直す
         ufo.y += UFO_SPEED; screen.blit(ufoimg, ufo) → ufo.update(); ufo.draw()
         ufo.y = OFFSCREEN_Y; ufo.x = ... → ufo.respawn()
         衝突判定: ufo.colliderect(...) → ufo.rect.colliderect(...)
```

<details>
<summary>コードを見る</summary>

```python
UFO_SIZE  = 50
UFO_COUNT = 10
UFO_SPEED = 10
OFFSCREEN_Y = -100


class UFO():
    def __init__(self, img, x, y):
        self.img  = img
        self.rect = pg.Rect(x, y, UFO_SIZE, UFO_SIZE)

    def update(self):
        self.rect.y += UFO_SPEED
        if self.rect.y > HEIGHT:
            self.rect.x = random.randint(0, WIDTH)
            self.rect.y = OFFSCREEN_Y

    def draw(self):
        screen.blit(self.img, self.rect)

    def respawn(self):
        self.rect.x = random.randint(0, WIDTH)
        self.rect.y = OFFSCREEN_Y


ufoimg = pg.image.load(IMG_DIR / "UFO.png")
ufoimg = pg.transform.scale(ufoimg, (UFO_SIZE, UFO_SIZE))
ufos   = []
for i in range(UFO_COUNT):
    ufos.append(UFO(ufoimg, random.randint(0, WIDTH), OFFSCREEN_Y * i))
```

```python
# gamestage() 内
for ufo in ufos:
    ufo.update()
    ufo.draw()
    if ufo.rect.colliderect(myship.rect):
        page = 2
        pg.mixer.Sound(SOUND_DIR / "down.wav").play()
    if ufo.rect.colliderect(bulletrect):
        ufo.respawn()
        bulletrect.y = OFFSCREEN_Y
        pg.mixer.Sound(SOUND_DIR / "piko.wav").play()
```

```python
# gamereset() 内
for i in range(UFO_COUNT):
    ufos[i].respawn()
```

</details>

---

# ex03 → ex04: Bullet クラスに書き直す

サンプル: [ex04.py](example/ex04.py)

`bulletrect` と発射ロジックをバラバラに書いていたものを `Bullet` クラスに集約する。  
`is_active()` で「発射中かどうか」の状態を管理するのがポイント。

## やること

```
step1. Bullet クラスを作る
         __init__(self, img) で self.img と self.rect を持たせる
         初期位置は self.rect = pg.Rect(0, OFFSCREEN_Y, BULLET_SIZE, BULLET_SIZE)（画面外＝待機状態）

step2. is_active(self) を追加する
         self.rect.y >= 0 のとき True（発射中）を返す

step3. shoot(self, x, y) を追加する
         is_active() が False のときだけ発射位置をセットして効果音を鳴らす
         すでに発射中は何もしない（2連射できない）

step4. update(self) を追加する
         is_active() のときだけ self.rect.y -= BULLET_SPEED で上に移動する

step5. draw(self) を追加する
         is_active() のときだけ描画する

step6. deactivate(self) と reset(self) を追加する
         deactivate: 撃墜したとき → self.rect.y = OFFSCREEN_Y で待機状態に戻す
         reset: gamereset() から呼ぶ用

step7. ゲームループと gamereset() を書き直す
         発射判定: if mdown[0] and bulletrect.y < 0: ... → bullet.shoot(...)
         移動・描画: バラバラな処理 → bullet.update(); bullet.draw()
         待機に戻す: bulletrect.y = OFFSCREEN_Y → bullet.deactivate()
```

<details>
<summary>コードを見る</summary>

```python
BULLET_SIZE  = 16
BULLET_SPEED = 15


class Bullet():
    def __init__(self, img):
        self.img  = img
        self.rect = pg.Rect(0, OFFSCREEN_Y, BULLET_SIZE, BULLET_SIZE)

    def shoot(self, x, y):
        if not self.is_active():
            self.rect.x = x
            self.rect.y = y
            pg.mixer.Sound(SOUND_DIR / "pi.wav").play()

    def update(self):
        if self.is_active():
            self.rect.y -= BULLET_SPEED

    def draw(self):
        if self.is_active():
            screen.blit(self.img, self.rect)

    def is_active(self):
        return self.rect.y >= 0

    def deactivate(self):
        self.rect.y = OFFSCREEN_Y

    def reset(self):
        self.rect.y = OFFSCREEN_Y
```

```python
# gamestage() 内
if mdown[0]:
    bullet.shoot(myship.rect.x + SHIP_SIZE // 2 - BULLET_SIZE // 2, myship.rect.y)
bullet.update()
bullet.draw()

for ufo in ufos:
    ...
    if ufo.rect.colliderect(bullet.rect) and bullet.is_active():
        ufo.respawn()
        bullet.deactivate()
        pg.mixer.Sound(SOUND_DIR / "piko.wav").play()
```

</details>

---

# ex04 → ex05: UFO の速さをインスタンスごとに変える（完成）

サンプル: [ex05.py](example/ex05.py)

UFO クラスに `speed` 属性を追加して、インスタンスによって落下速度が違うようにする。

## やること

```
step1. UFO.__init__ に speed 引数を追加する
         __init__(self, img, x, y, speed) にする
         self.speed = speed で保持する

step2. update() の移動量を speed に変える
         self.rect.y += UFO_SPEED → self.rect.y += self.speed にする

step3. UFO を生成するときに速さを渡す
         random.randint(*UFO_SPEED_RANGE) などを speed に渡すと UFO ごとに速さが変わる
```

<details>
<summary>コードを見る</summary>

```python
UFO_SPEED_RANGE = (5, 15)


class UFO():
    def __init__(self, img, x, y, speed):
        self.img   = img
        self.rect  = pg.Rect(x, y, UFO_SIZE, UFO_SIZE)
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.rect.x = random.randint(0, WIDTH)
            self.rect.y = OFFSCREEN_Y
```

```python
ufos = []
for i in range(UFO_COUNT):
    ufos.append(UFO(ufoimg, random.randint(0, WIDTH), OFFSCREEN_Y * i, random.randint(*UFO_SPEED_RANGE)))
```

</details>

---

# ex05 → ex06: 難易度システムを追加する（発展）

サンプル: [ex06.py](example/ex06.py)

得点に応じて UFO の速度と移動パターンが4段階に変化する、発展版のサンプル。`python example/ex06.py` で起動できる。

| スコア | レベル | 速度 | 移動パターン | 背景色 |
| --- | --- | --- | --- | --- |
| 0〜99 | NORMAL | 4 | 真下に落下 | 紺 |
| 100〜199 | FAST | 7 | 速度アップ | 紫 |
| 200〜299 | ZIGZAG | 7 | サイン波で左右に揺れながら落下 | 暗緑 |
| 300〜 | CHASE | 10 | 自機を追尾しながら落下 | 暗赤 |

## 発展1 — 難易度テーブルと get_level()

スコアを受け取ってその時点の難易度設定を返す関数を作る。
設定をコードに直接書かずにテーブルとしてまとめることで、調整しやすくなる。

### やること

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

## 発展2 — UFO.set_difficulty()

`get_level()` を使って UFO の速度と移動パターンを更新するメソッドを追加する。
ゲームループから毎フレーム呼ぶことで、スコアが上がった瞬間に UFO が変化する。

### やること

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
        self.rect      = pg.Rect(x, y, UFO_SIZE, UFO_SIZE)
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

## 発展3 — 移動パターンの実装

`update()` の中で `move_type` を見て3種類の動きを分岐する。

```
normal / fast   → 真下に落下するだけ（speed の大きさだけ違う）
zigzag          → サイン波で X 座標を左右に動かしながら落下する
chase           → 毎フレーム自機の X 座標に近づきながら落下する
```

### やること — zigzag

```
step1. UFO.__init__ に self.phase = random.randint(0, 360) を追加する
         各 UFO の初期位相をずらすことで、一斉に同じ方向へ動くのを防ぐ

step2. update() で move_type == "zigzag" のとき
         self.phase += ZIGZAG_STEP  で位相を毎フレーム進める
         dx = int(math.sin(math.radians(self.phase)) * ZIGZAG_RANGE)  で左右の移動量を計算する
         self.rect.x += dx  で X 座標を更新する
         X 座標が画面外に出たら 0 または UFO_X_MAX（= WIDTH - UFO_SIZE、750）に戻す

step3. respawn() でも self.phase をランダムにリセットする
         復活するたびに位相が変わり、動きにバリエーションが生まれる
```

### やること — chase

```
step1. update(self, ship_x) の引数に ship_x を追加する
         ゲームループから myship.rect.x を渡す

step2. move_type == "chase" のとき
         target_x = ship_x - SHIP_SIZE // 2  で自機の中心 X に合わせた目標座標を計算する
         self.rect.x が target_x より小さければ +CHASE_STEP する
         self.rect.x が target_x より大きければ -CHASE_STEP する
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
            self.phase += ZIGZAG_STEP
            dx = int(math.sin(math.radians(self.phase)) * ZIGZAG_RANGE)
            self.rect.x += dx
            if self.rect.x < 0:
                self.rect.x = 0
            if self.rect.x > UFO_X_MAX:
                self.rect.x = UFO_X_MAX

        elif self.move_type == "chase":
            target_x = ship_x - SHIP_SIZE // 2
            if self.rect.x < target_x:
                self.rect.x += CHASE_STEP
            elif self.rect.x > target_x:
                self.rect.x -= CHASE_STEP

        if self.rect.y > HEIGHT:
            self.respawn()

    def respawn(self):
        self.rect.x = random.randint(0, UFO_X_MAX)
        self.rect.y = OFFSCREEN_Y
        self.phase  = random.randint(0, 360)   # 追加
```

```python
# ゲームループ内（ship_x を渡す）
ufo.update(myship.rect.x)
```

</details>

## 発展4 — HUD 表示

現在のレベル名と「次のレベルまでの残りスコア」を画面に表示する。
背景色をレベルごとに変えることで、難易度が上がったことを視覚的に伝える。

### やること

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

    font  = pg.font.Font(None, SCORE_FONT_SIZE)
    small = pg.font.Font(None, 28)

    score_text = font.render("SCORE: " + str(score), True, pg.Color("WHITE"))
    screen.blit(score_text, SCORE_POS)

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

---

# ex06 → package: クラスごとにファイル分割する

サンプル: [package/main.py](package/main.py) / [package/game/](package/game/)

ここまでの `example/ex06.py` は、`LEVELS` テーブル・`MyShip`/`UFO`/`Bullet` の3クラス・画面制御用の関数がすべて1つのファイルに入っている。クラスが増えるほど「どこに何が書いてあるか」を探しにくくなる。[18_module](../18_module/README.md) で学んだパッケージ・相対インポートの知識を使って、クラスごとに別ファイルへ分割する。

## やること

```
step1. game/ フォルダを作り、__init__.py を置く（パッケージにする）

step2. LEVELS と get_level() を game/level.py に移す
         他のクラスから使われる「難易度の定義」なので、クラスとは別ファイルにする

step3. MyShip クラスを game/myship.py に移す
         draw() が main.py の screen をそのまま参照していた部分は、
         ファイルを分けると main.py の screen が見えなくなるため、
         draw(self, screen) のように引数で受け取る形に変更する

step4. UFO クラスを game/ufo.py に移す
         get_level() は from .level import get_level で読み込む（相対インポート）
         HEIGHT のように main.py 側にあった定数も、このファイルの先頭に書き直す

step5. Bullet クラスを game/bullet.py に移す
         SOUND_DIR も同様に、このファイルの先頭で定義し直す

step6. game/__init__.py で各クラス・関数をまとめて公開する
         main.py 側は from game import MyShip, UFO, Bullet, LEVELS, get_level だけで済むようにする

step7. main.py を整理する
         クラスの中身が無くなった分、main.py は「準備」と「ゲームループ」だけになる
         draw() の呼び出しは myship.draw(screen) のように screen を渡す形に変える
         UFO の中でしか使わなくなった math の import は main.py から削除する
```

## ディレクトリ構成

```
19_shooting_game_class_ver/
├── example/
│   └── ex06.py          # 分割前（このステップの「Before」）
└── package/
    ├── main.py          # 分割後の「準備」と「ゲームループ」だけが残る
    └── game/
        ├── __init__.py  # 各クラス・関数をまとめて公開する
        ├── level.py     # LEVELS・get_level()
        ├── myship.py    # MyShip クラス
        ├── ufo.py       # UFO クラス
        └── bullet.py    # Bullet クラス
```

<details>
<summary>コードを見る（game/level.py）</summary>

```python
# 難易度テーブル（スコアが高い順に並べる）
LEVELS = [
    {"min_score": 300, "name": "CHASE",  "speed": 10, "move": "chase",  "bg": (60,  0,   0)},
    {"min_score": 200, "name": "ZIGZAG", "speed":  7, "move": "zigzag", "bg": (0,   50,  0)},
    {"min_score": 100, "name": "FAST",   "speed":  7, "move": "fast",   "bg": (50,  0,   80)},
    {"min_score":   0, "name": "NORMAL", "speed":  4, "move": "normal", "bg": (0,   0,   128)},
]


def get_level(score):
    for lv in LEVELS:
        if score >= lv["min_score"]:
            return lv
    return LEVELS[-1]
```

</details>

<details>
<summary>コードを見る（game/myship.py）</summary>

```python
import pygame as pg

SHIP_SIZE = 50


class MyShip:
    def __init__(self, img):
        self.img  = img
        self.rect = pg.Rect(400, 500, SHIP_SIZE, SHIP_SIZE)

    def update(self, mx):
        self.rect.x = mx - SHIP_SIZE // 2

    def draw(self, screen):
        screen.blit(self.img, self.rect)

    def reset(self):
        self.rect.x = 400
        self.rect.y = 500
```

</details>

<details>
<summary>コードを見る（game/ufo.py）</summary>

```python
import math
import random
import pygame as pg
from .level import get_level

HEIGHT       = 600
SHIP_SIZE    = 50
UFO_SIZE     = 50
OFFSCREEN_Y  = -100
UFO_X_MAX    = 800 - UFO_SIZE   # WIDTH(800) - UFO_SIZE。ジグザグ・リスポーン時のX座標の上限
ZIGZAG_STEP  = 3
ZIGZAG_RANGE = 6
CHASE_STEP   = 3


class UFO:
    def __init__(self, img, x, y):
        self.img       = img
        self.rect      = pg.Rect(x, y, UFO_SIZE, UFO_SIZE)
        self.speed     = 4
        self.move_type = "normal"
        self.phase     = random.randint(0, 360)   # 各 UFO の位相をずらす

    def set_difficulty(self, score):
        lv             = get_level(score)
        self.speed     = lv["speed"]
        self.move_type = lv["move"]

    def update(self, ship_x):
        self.rect.y += self.speed

        if self.move_type == "zigzag":
            self.phase += ZIGZAG_STEP
            dx = int(math.sin(math.radians(self.phase)) * ZIGZAG_RANGE)
            self.rect.x += dx
            if self.rect.x < 0:
                self.rect.x = 0
            if self.rect.x > UFO_X_MAX:
                self.rect.x = UFO_X_MAX

        elif self.move_type == "chase":
            target_x = ship_x - SHIP_SIZE // 2
            if self.rect.x < target_x:
                self.rect.x += CHASE_STEP
            elif self.rect.x > target_x:
                self.rect.x -= CHASE_STEP

        if self.rect.y > HEIGHT:
            self.respawn()

    def draw(self, screen):
        screen.blit(self.img, self.rect)

    def respawn(self):
        self.rect.x = random.randint(0, UFO_X_MAX)
        self.rect.y = OFFSCREEN_Y
        self.phase  = random.randint(0, 360)
```

</details>

<details>
<summary>コードを見る（game/bullet.py）</summary>

```python
from pathlib import Path
import pygame as pg

BASE_DIR  = Path(__file__).resolve().parent.parent.parent
SOUND_DIR = BASE_DIR / "sounds"

BULLET_SIZE  = 16
BULLET_SPEED = 15
OFFSCREEN_Y  = -100


class Bullet:
    def __init__(self, img):
        self.img  = img
        self.rect = pg.Rect(0, OFFSCREEN_Y, BULLET_SIZE, BULLET_SIZE)

    def shoot(self, x, y):
        if not self.is_active():
            self.rect.x = x
            self.rect.y = y
            pg.mixer.Sound(SOUND_DIR / "pi.wav").play()

    def update(self):
        if self.is_active():
            self.rect.y -= BULLET_SPEED

    def draw(self, screen):
        if self.is_active():
            screen.blit(self.img, self.rect)

    def is_active(self):
        return self.rect.y >= 0

    def deactivate(self):
        self.rect.y = OFFSCREEN_Y

    def reset(self):
        self.rect.y = OFFSCREEN_Y
```

</details>

<details>
<summary>コードを見る（game/__init__.py）</summary>

```python
from .level import LEVELS, get_level
from .myship import MyShip
from .ufo import UFO
from .bullet import Bullet
```

</details>

<details>
<summary>コードを見る（main.py）</summary>

```python
from pathlib import Path
import random
import sys
import pygame as pg
from game import MyShip, UFO, Bullet, LEVELS, get_level

pg.init()
BASE_DIR  = Path(__file__).resolve().parent.parent
IMG_DIR   = BASE_DIR / "images"
SOUND_DIR = BASE_DIR / "sounds"

WIDTH, HEIGHT = 800, 600
FPS = 60

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("シューティングゲーム 発展版（ファイル分割）")
clock = pg.time.Clock()

SHIP_SIZE   = 50
UFO_SIZE    = 50
UFO_COUNT   = 10
OFFSCREEN_Y = -100
UFO_X_MAX   = WIDTH - UFO_SIZE
BULLET_SIZE = 16

REPLAY_BTN_POS   = (320, 480)
RESULT_FONT_SIZE = 150
SCORE_FONT_SIZE  = 40
SCORE_POS        = (20, 20)
SCORE_PER_HIT    = 10

myimg  = pg.image.load(IMG_DIR / "myship.png")
myimg  = pg.transform.scale(myimg, (SHIP_SIZE, SHIP_SIZE))
myship = MyShip(myimg)

bulletimg = pg.image.load(IMG_DIR / "bullet.png")
bulletimg = pg.transform.scale(bulletimg, (BULLET_SIZE, BULLET_SIZE))
bullet    = Bullet(bulletimg)

ufoimg = pg.image.load(IMG_DIR / "UFO.png")
ufoimg = pg.transform.scale(ufoimg, (UFO_SIZE, UFO_SIZE))
ufos   = []
for i in range(UFO_COUNT):
    ufos.append(UFO(ufoimg, random.randint(0, UFO_X_MAX), OFFSCREEN_Y * i))

replay_img = pg.image.load(IMG_DIR / "replaybtn.png")

pushFlag = False
page     = 1
score    = 0


def button_to_jump(btn, newpage):
    global page, pushFlag
    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()
    if mdown[0]:
        if btn.collidepoint(mx, my) and not pushFlag:
            pg.mixer.Sound(SOUND_DIR / "pi.wav").play()
            page = newpage
            pushFlag = True
    else:
        pushFlag = False


def gamestage():
    global page, score
    lv = get_level(score)
    screen.fill(lv["bg"])

    (mx, my) = pg.mouse.get_pos()
    mdown = pg.mouse.get_pressed()

    myship.update(mx)
    myship.draw(screen)

    if mdown[0]:
        bullet.shoot(myship.rect.x + SHIP_SIZE // 2 - BULLET_SIZE // 2, myship.rect.y)
    bullet.update()
    bullet.draw(screen)

    for ufo in ufos:
        ufo.set_difficulty(score)
        ufo.update(myship.rect.x)
        ufo.draw(screen)
        if ufo.rect.colliderect(myship.rect):
            page = 2
            pg.mixer.Sound(SOUND_DIR / "down.wav").play()
        if ufo.rect.colliderect(bullet.rect) and bullet.is_active():
            score += SCORE_PER_HIT
            ufo.respawn()
            bullet.deactivate()
            pg.mixer.Sound(SOUND_DIR / "piko.wav").play()

    font  = pg.font.Font(None, SCORE_FONT_SIZE)
    small = pg.font.Font(None, 28)

    score_text = font.render("SCORE: " + str(score), True, pg.Color("WHITE"))
    screen.blit(score_text, SCORE_POS)

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


def gamereset():
    global score
    score = 0
    myship.reset()
    bullet.reset()
    for i in range(UFO_COUNT):
        ufos[i].respawn()


def gameover():
    screen.fill(pg.Color("NAVY"))
    font = pg.font.Font(None, RESULT_FONT_SIZE)
    text = font.render("GAMEOVER", True, pg.Color("RED"))
    screen.blit(text, (100, 200))
    btn1 = screen.blit(replay_img, REPLAY_BTN_POS)
    font = pg.font.Font(None, SCORE_FONT_SIZE)
    text = font.render("SCORE: " + str(score), True, pg.Color("WHITE"))
    screen.blit(text, SCORE_POS)
    button_to_jump(btn1, 1)
    if page == 1:
        gamereset()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    if page == 1:
        gamestage()
    elif page == 2:
        gameover()
    pg.display.update()
    clock.tick(FPS)
```

</details>

> ファイルを分けると、それまで「同じファイルの中だから見えていた」`screen` や `SOUND_DIR` のような変数が、他のファイルからは見えなくなる。分割で最初につまずきやすいのはこの点で、対処法は主に2つ。「値を引数で渡す」（`draw(self, screen)` のように、必要なときに呼び出し側から渡す）か、「その値を使うファイルの先頭に定数として書き直す」（`SOUND_DIR` や `HEIGHT` のように、値そのものは重複してもファイルごとに完結させる）。どちらを選ぶかは、[21_super_mario](../21_super_mario/README.md) 以降のレッスンでも同じ考え方が出てくる。
