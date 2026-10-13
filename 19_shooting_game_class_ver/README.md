```text
14_shooting_game の関数ベースのコードを、クラスを使って段階的に書き直します
```

# 目次
- [概要](#概要)
- [ex01 — 出発点：関数ベースのコード](#ex01--出発点関数ベースのコード)
  - [ステップ1. 出発点のコードを用意する](#ステップ1-出発点のコードを用意する)
- [ex02 — MyShip クラスにまとめる](#ex02--myship-クラスにまとめる)
  - [ステップ2. MyShip クラスの枠と __init__ を書く](#ステップ2-myship-クラスの枠と-__init__-を書く)
  - [ステップ3. update() と draw() を書く](#ステップ3-update-と-draw-を書く)
  - [ステップ4. reset() を書く](#ステップ4-reset-を書く)
  - [ステップ5. myrect を myship に置き換える](#ステップ5-myrect-を-myship-に置き換える)
  - [ステップ6. gamestage() の自機の処理を書き換える](#ステップ6-gamestage-の自機の処理を書き換える)
  - [ステップ7. gamereset() で myship.reset() を呼ぶ](#ステップ7-gamereset-で-myshipreset-を呼ぶ)
- [ex03 — UFO クラスを作る](#ex03--ufo-クラスを作る)
  - [ステップ8. UFO の定数を、UFO クラスの上に置く](#ステップ8-ufo-の定数をufo-クラスの上に置く)
  - [ステップ9. UFO クラスの枠と __init__ を書く](#ステップ9-ufo-クラスの枠と-__init__-を書く)
  - [ステップ10. update() を書く](#ステップ10-update-を書く)
  - [ステップ11. draw() と respawn() を書く](#ステップ11-draw-と-respawn-を書く)
  - [ステップ12. UFO のインスタンスを作る](#ステップ12-ufo-のインスタンスを作る)
  - [ステップ13. gamestage() の UFO の処理を書き換える](#ステップ13-gamestage-の-ufo-の処理を書き換える)
  - [ステップ14. gamereset() で UFO を respawn() する](#ステップ14-gamereset-で-ufo-を-respawn-する)
- [ex04 — Bullet クラスを作る](#ex04--bullet-クラスを作る)
  - [ステップ15. Bullet クラスの枠と __init__ を書く](#ステップ15-bullet-クラスの枠と-__init__-を書く)
  - [ステップ16. shoot() を書く](#ステップ16-shoot-を書く)
  - [ステップ17. update() と draw() を書く](#ステップ17-update-と-draw-を書く)
  - [ステップ18. is_active()・deactivate()・reset() を書く](#ステップ18-is_activedeactivatereset-を書く)
  - [ステップ19. bulletrect を bullet に置き換える](#ステップ19-bulletrect-を-bullet-に置き換える)
  - [ステップ20. gamestage() の弾の処理を書き換える](#ステップ20-gamestage-の弾の処理を書き換える)
  - [ステップ21. gamereset() で bullet.reset() を呼ぶ](#ステップ21-gamereset-で-bulletreset-を呼ぶ)
- [ex05 — UFO の速さをインスタンスごとに変える](#ex05--ufo-の速さをインスタンスごとに変える)
  - [ステップ22. UFO に speed を持たせる](#ステップ22-ufo-に-speed-を持たせる)
  - [ステップ23. UFO を作るとき、速さをランダムに決める](#ステップ23-ufo-を作るとき速さをランダムに決める)
- [ex06 — 難易度システムを追加する（発展）](#ex06--難易度システムを追加する発展)
  - [ステップ24. 難易度のテーブルを作る](#ステップ24-難易度のテーブルを作る)
  - [ステップ25. get_level() を書く](#ステップ25-get_level-を書く)
  - [ステップ26. UFO の定数を足す](#ステップ26-ufo-の定数を足す)
  - [ステップ27. UFO の __init__ を書き換える](#ステップ27-ufo-の-__init__-を書き換える)
  - [ステップ28. set_difficulty() を書く](#ステップ28-set_difficulty-を書く)
  - [ステップ29. update() を書き換える：下に動かして、画面外で戻す](#ステップ29-update-を書き換える下に動かして画面外で戻す)
  - [ステップ30. ジグザグに動かす](#ステップ30-ジグザグに動かす)
  - [ステップ31. 自機を追いかける](#ステップ31-自機を追いかける)
  - [ステップ32. respawn() を書き換える](#ステップ32-respawn-を書き換える)
  - [ステップ33. UFO を作るとき、X座標の範囲を変える](#ステップ33-ufo-を作るときx座標の範囲を変える)
  - [ステップ34. gamestage() の背景を難易度の色にする](#ステップ34-gamestage-の背景を難易度の色にする)
  - [ステップ35. UFO に難易度を伝える](#ステップ35-ufo-に難易度を伝える)
  - [ステップ36. スコアと難易度を表示する](#ステップ36-スコアと難易度を表示する)
  - [ステップ37. 次のレベルまでの残りを表示する](#ステップ37-次のレベルまでの残りを表示する)
  - [ステップ38. ゲームオーバー画面のスコアの文字をそろえる](#ステップ38-ゲームオーバー画面のスコアの文字をそろえる)
- [package — クラスごとにファイルを分割する](#package--クラスごとにファイルを分割する)
  - [ステップ39. game/ フォルダと __init__.py を作る](#ステップ39-game-フォルダと-__init__py-を作る)
  - [ステップ40. level.py：難易度のテーブルを移す](#ステップ40-levelpy難易度のテーブルを移す)
  - [ステップ41. myship.py：MyShip クラスを移す](#ステップ41-myshippymyship-クラスを移す)
  - [ステップ42. ufo.py：定数とインポート](#ステップ42-ufopy定数とインポート)
  - [ステップ43. ufo.py：UFO クラス](#ステップ43-ufopyufo-クラス)
  - [ステップ44. bullet.py：Bullet クラスを移す](#ステップ44-bulletpybullet-クラスを移す)
  - [ステップ45. __init__.py：各クラスをまとめて公開する](#ステップ45-__init__py各クラスをまとめて公開する)
  - [ステップ46. main.py：インポートと準備](#ステップ46-mainpyインポートと準備)
  - [ステップ47. main.py：button_to_jump()](#ステップ47-mainpybutton_to_jump)
  - [ステップ48. main.py：gamestage()](#ステップ48-mainpygamestage)
  - [ステップ49. main.py：gamereset()・gameover()・ゲームループ](#ステップ49-mainpygameresetgameoverゲームループ)

---

# 概要

[14_shooting_game](../14_shooting_game/README.md) の完成コード（関数ベース）を出発点に、自機・UFO・弾を、順番にクラスに変換していく。

| 章 | 追加するクラス | ポイント |
| --- | --- | --- |
| ex01 | なし（関数ベースの出発点） | `myrect` / `ufos` / `bulletrect` がバラバラに存在する |
| ex02 | `MyShip` | 1つのインスタンス・一番シンプル |
| ex03 | `MyShip` + `UFO` | リストで複数インスタンスを管理 |
| ex04 | `MyShip` + `UFO` + `Bullet` | `is_active()` で発射状態を管理 |
| ex05 | `MyShip` + `UFO` + `Bullet` | `UFO` に `speed` 属性を追加して、インスタンスごとに速さを変える完成形 |
| ex06 | 変更なし（`UFO` に難易度システムを追加） | スコアに応じて速度・移動パターン・背景色が段階的に変化する発展版 |
| package | 同上 | クラスごとにファイルを分割する |

---

# ex01 — 出発点：関数ベースのコード

14_shooting_game の完成コードを、ここからクラスに書き直していく（コードは [example/ex01.py](example/ex01.py)）。

## ステップ1. 出発点のコードを用意する

[14_shooting_game](../14_shooting_game/README.md) の完成コード（`14_shooting_game/example/ex05.py`）を、新しい `.py` ファイルにコピーする。これが、クラス化していく出発点になる（ここでは何も書き足さない）。

- 作りは、関数ベース。自機は `myrect`、弾は `bulletrect`、UFO は `ufos`（`pg.Rect` のリスト）で、バラバラに持っている
- `gamestage()` の中で、これらの変数を直接書き換えている（`myrect.x = ...`、`ufo.y += UFO_SPEED` など）
- 次のステップから、自機・UFO・弾を順番にクラスにまとめていく
- `example/ex01.py` は、同じ内容で、定数の並べ方だけが少し違う（動きは同じ）。コードは、答え合わせ用に載せておく

<details>
<summary>コードを見る</summary>

```python
from pathlib import Path
import pygame as pg
import sys
import random

pg.init()
BASE_DIR  = Path(__file__).resolve().parent.parent
IMG_DIR   = BASE_DIR / "images"
SOUND_DIR = BASE_DIR / "sounds"

WIDTH, HEIGHT = 800, 600

FPS = 60

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("シューティングゲーム")
clock = pg.time.Clock()

SHIP_SIZE = 50
BULLET_SIZE  = 16
BULLET_SPEED = 15
OFFSCREEN_Y  = -100
UFO_SIZE  = 50
UFO_COUNT = 10
UFO_SPEED = 10
REPLAY_BTN_POS   = (320, 480)
RESULT_FONT_SIZE = 150
SCORE_FONT_SIZE  = 40
SCORE_POS        = (20, 20)
SCORE_PER_HIT    = 10

myimg  = pg.image.load(IMG_DIR / "myship.png")
myimg  = pg.transform.scale(myimg, (SHIP_SIZE, SHIP_SIZE))
myrect = pg.Rect(400, 500, SHIP_SIZE, SHIP_SIZE)

bulletimg  = pg.image.load(IMG_DIR / "bullet.png")
bulletimg  = pg.transform.scale(bulletimg, (BULLET_SIZE, BULLET_SIZE))
bulletrect = pg.Rect(400, OFFSCREEN_Y, BULLET_SIZE, BULLET_SIZE)

ufoimg = pg.image.load(IMG_DIR / "UFO.png")
ufoimg = pg.transform.scale(ufoimg, (UFO_SIZE, UFO_SIZE))
ufos   = []
for i in range(UFO_COUNT):
    ux = random.randint(0, WIDTH)
    uy = OFFSCREEN_Y * i
    ufos.append(pg.Rect(ux, uy, UFO_SIZE, UFO_SIZE))

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
    screen.fill(pg.Color("NAVY"))
    (mx, my) = pg.mouse.get_pos()
    mdown = pg.mouse.get_pressed()

    myrect.x = mx - SHIP_SIZE // 2
    screen.blit(myimg, myrect)

    if mdown[0] and bulletrect.y < 0:
        bulletrect.x = myrect.x + SHIP_SIZE // 2 - BULLET_SIZE // 2
        bulletrect.y = myrect.y
        pg.mixer.Sound(SOUND_DIR / "pi.wav").play()
    if bulletrect.y >= 0:
        bulletrect.y -= BULLET_SPEED
        screen.blit(bulletimg, bulletrect)

    for ufo in ufos:
        ufo.y += UFO_SPEED
        screen.blit(ufoimg, ufo)
        if ufo.y > HEIGHT:
            ufo.x = random.randint(0, WIDTH)
            ufo.y = OFFSCREEN_Y
        if ufo.colliderect(myrect):
            page = 2
            pg.mixer.Sound(SOUND_DIR / "down.wav").play()
        if ufo.colliderect(bulletrect):
            score += SCORE_PER_HIT
            ufo.y = OFFSCREEN_Y
            ufo.x = random.randint(0, WIDTH)
            bulletrect.y = OFFSCREEN_Y
            pg.mixer.Sound(SOUND_DIR / "piko.wav").play()

    font = pg.font.Font(None, SCORE_FONT_SIZE)
    text = font.render("SCORE:" + str(score), True, pg.Color("WHITE"))
    screen.blit(text, SCORE_POS)


def gamereset():
    global score
    score      = 0
    myrect.x   = 400
    myrect.y   = 500
    bulletrect.y = OFFSCREEN_Y
    for i in range(UFO_COUNT):
        ufos[i] = pg.Rect(random.randint(0, WIDTH), OFFSCREEN_Y * i, UFO_SIZE, UFO_SIZE)


def gameover():
    screen.fill(pg.Color("NAVY"))
    font = pg.font.Font(None, RESULT_FONT_SIZE)
    text = font.render("GAMEOVER", True, pg.Color("RED"))
    screen.blit(text, (100, 200))
    btn1 = screen.blit(replay_img, REPLAY_BTN_POS)
    font = pg.font.Font(None, SCORE_FONT_SIZE)
    text = font.render("SCORE:" + str(score), True, pg.Color("WHITE"))
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

ここまでで、`example/ex01.py` と同じ動きになる。マウスで自機を動かし、クリックで弾を撃って、UFO を倒す。

### 実行する

ターミナルで、リポジトリのルートから実行する（自分のファイルなら、ファイル名を置き換える）。

```bash
python 19_shooting_game_class_ver/example/ex01.py
```

---

# ex02 — MyShip クラスにまとめる

`myimg` と `myrect` がバラバラに存在していた自機のデータと処理を、`MyShip` クラスに集約する（完成形は [example/ex02.py](example/ex02.py)）。

## ステップ2. MyShip クラスの枠と __init__ を書く

ここから、自機をクラスにまとめる。`ex01` をコピーして `ex02.py` にして、書き換えてもよい。

定数の下に、書く。

- `SHIP_SIZE = 50` を、`MyShip` の上に書く（元の `SHIP_SIZE` の行は、消す）
- 2行空けて、`class MyShip():` を定義する
- `def __init__(self, img):` で、画像を受け取る
- `self.img = img` で、画像を持つ
- `self.rect = pg.Rect(400, 500, SHIP_SIZE, SHIP_SIZE)` で、位置と大きさ（`myrect` だったもの）を持つ

<details>
<summary>コードを見る</summary>

```python
SHIP_SIZE = 50


class MyShip():
    def __init__(self, img):
        self.img  = img
        self.rect = pg.Rect(400, 500, SHIP_SIZE, SHIP_SIZE)
```

</details>

## ステップ3. update() と draw() を書く

`__init__` の下に、1行空けて、2つのメソッドを書く。

- `def update(self, mx):` で、`self.rect.x = mx - SHIP_SIZE // 2` と、マウスのX座標に自機の中心を合わせる
- `def draw(self):` で、`screen.blit(self.img, self.rect)` と、描く

<details>
<summary>コードを見る</summary>

```python
    def update(self, mx):
        self.rect.x = mx - SHIP_SIZE // 2

    def draw(self):
        screen.blit(self.img, self.rect)
```

</details>

## ステップ4. reset() を書く

`draw()` の下に、1行空けて書く。ゲームをやり直すときに使う。

- `def reset(self):` で、`self.rect.x = 400` と `self.rect.y = 500` と、最初の位置に戻す

<details>
<summary>コードを見る</summary>

```python
    def reset(self):
        self.rect.x = 400
        self.rect.y = 500
```

</details>

## ステップ5. myrect を myship に置き換える

データの部分を書き換える。

- `myrect = pg.Rect(...)` の行を消す
- `myimg` を読み込む2行はそのまま残す
- その下に、`myship = MyShip(myimg)` を足して、自機のインスタンスを作る

<details>
<summary>コードを見る</summary>

```python
myimg  = pg.image.load(IMG_DIR / "myship.png")
myimg  = pg.transform.scale(myimg, (SHIP_SIZE, SHIP_SIZE))
myship = MyShip(myimg)
```

</details>

## ステップ6. gamestage() の自機の処理を書き換える

`gamestage()` の、`myrect` を使っている部分を、書き換える。

- `myrect.x = mx - SHIP_SIZE // 2` と `screen.blit(myimg, myrect)` を消して、`myship.update(mx)` と `myship.draw()` にする
- 弾を撃つ位置の `myrect.x`・`myrect.y` を、`myship.rect.x`・`myship.rect.y` に変える
- UFO との当たり判定の `ufo.colliderect(myrect)` を、`ufo.colliderect(myship.rect)` に変える

自機の処理:

<details>
<summary>コードを見る</summary>

```python
    myship.update(mx)
    myship.draw()
```

</details>

弾を撃つ位置:

<details>
<summary>コードを見る</summary>

```python
        bulletrect.x = myship.rect.x + SHIP_SIZE // 2 - BULLET_SIZE // 2
        bulletrect.y = myship.rect.y
```

</details>

UFO との当たり判定:

<details>
<summary>コードを見る</summary>

```python
        if ufo.colliderect(myship.rect):
```

</details>

## ステップ7. gamereset() で myship.reset() を呼ぶ

`gamereset()` を変更する。

- `myrect.x = 400` と `myrect.y = 500` の2行を消して、`myship.reset()` の1行にする

<details>
<summary>コードを見る</summary>

```python
def gamereset():
    global score
    score = 0
    myship.reset()
```

</details>

ここまでで、`example/ex02.py` と同じ動きになる。動きは ex01 と同じで、自機の持ち物と処理が `MyShip` にまとまった。

### 実行する

ターミナルで、リポジトリのルートから実行する（自分のファイルなら、ファイル名を置き換える）。

```bash
python 19_shooting_game_class_ver/example/ex02.py
```

---

# ex03 — UFO クラスを作る

UFO を `UFO` クラスにして、リストで複数のインスタンスを管理する（完成形は [example/ex03.py](example/ex03.py)）。

## ステップ8. UFO の定数を、UFO クラスの上に置く

ここから、UFO をクラスにまとめる。

`MyShip` クラスの下に、2行空けて書く。UFO の定数をここにまとめる（元の定数の行は、消す）。

- `UFO_SIZE`、`UFO_COUNT`、`UFO_SPEED`、`OFFSCREEN_Y` の4つを書く

<details>
<summary>コードを見る</summary>

```python
UFO_SIZE  = 50
UFO_COUNT = 10
UFO_SPEED = 10
OFFSCREEN_Y = -100
```

</details>

## ステップ9. UFO クラスの枠と __init__ を書く

定数の下に、2行空けて書く。

- `class UFO():` を定義する
- `def __init__(self, img, x, y):` で、画像と位置を受け取る
- `self.img = img`、`self.rect = pg.Rect(x, y, UFO_SIZE, UFO_SIZE)` で、画像と `Rect` を持つ

<details>
<summary>コードを見る</summary>

```python
class UFO():
    def __init__(self, img, x, y):
        self.img  = img
        self.rect = pg.Rect(x, y, UFO_SIZE, UFO_SIZE)
```

</details>

## ステップ10. update() を書く

`__init__` の下に、1行空けて書く。`gamestage()` にあった UFO を動かす処理を、メソッドに移す。`ufo.y` は `self.rect.y` に変わる。

- `def update(self):` で、`self.rect.y += UFO_SPEED` と、下に動かす
- `if self.rect.y > HEIGHT:`（画面の下に出た）なら、`self.rect.x` をランダムに決め直し、`self.rect.y = OFFSCREEN_Y` と、上に戻す

<details>
<summary>コードを見る</summary>

```python
    def update(self):
        self.rect.y += UFO_SPEED
        if self.rect.y > HEIGHT:
            self.rect.x = random.randint(0, WIDTH)
            self.rect.y = OFFSCREEN_Y
```

</details>

## ステップ11. draw() と respawn() を書く

`update()` の下に、1行空けて、2つのメソッドを書く。

- `def draw(self):` で、`screen.blit(self.img, self.rect)` と、描く
- `def respawn(self):` で、`self.rect.x` をランダムに決め、`self.rect.y = OFFSCREEN_Y` と、上に戻す（弾に当たったときや、リプレイのときに使う）

<details>
<summary>コードを見る</summary>

```python
    def draw(self):
        screen.blit(self.img, self.rect)

    def respawn(self):
        self.rect.x = random.randint(0, WIDTH)
        self.rect.y = OFFSCREEN_Y
```

</details>

## ステップ12. UFO のインスタンスを作る

UFO のデータを作る部分を書き換える。

- `ufoimg` を読み込む2行と、`ufos = []` は、そのまま
- `for i in range(UFO_COUNT):` の中の、`ux`・`uy` を求める2行と、`pg.Rect` を足す行を消して、1行にする
- `ufos.append(UFO(ufoimg, random.randint(0, WIDTH), OFFSCREEN_Y * i))` で、`UFO` のインスタンスをリストに足す

<details>
<summary>コードを見る</summary>

```python
ufoimg = pg.image.load(IMG_DIR / "UFO.png")
ufoimg = pg.transform.scale(ufoimg, (UFO_SIZE, UFO_SIZE))
ufos   = []
for i in range(UFO_COUNT):
    ufos.append(UFO(ufoimg, random.randint(0, WIDTH), OFFSCREEN_Y * i))
```

</details>

## ステップ13. gamestage() の UFO の処理を書き換える

`gamestage()` の、`for ufo in ufos:` の中を書き換える。

- UFO を動かして描く部分（`ufo.y += UFO_SPEED` から、画面の下に出たときの処理まで）を消して、`ufo.update()` と `ufo.draw()` にする
- 自機との当たり判定を、`ufo.rect.colliderect(myship.rect)` に変える
- 弾との当たり判定を、`ufo.rect.colliderect(bulletrect)` に変える
- 弾に当たったときの、`ufo.y`・`ufo.x` を戻す2行を消して、`ufo.respawn()` にする

<details>
<summary>コードを見る</summary>

```python
    for ufo in ufos:
        ufo.update()
        ufo.draw()
        if ufo.rect.colliderect(myship.rect):
            page = 2
            pg.mixer.Sound(SOUND_DIR / "down.wav").play()
        if ufo.rect.colliderect(bulletrect):
            score += SCORE_PER_HIT
            ufo.respawn()
            bulletrect.y = OFFSCREEN_Y
            pg.mixer.Sound(SOUND_DIR / "piko.wav").play()
```

</details>

## ステップ14. gamereset() で UFO を respawn() する

`gamereset()` を変更する。

- UFO を作り直していた行（`ufos[i] = pg.Rect(...)`）を、`ufos[i].respawn()` にする

<details>
<summary>コードを見る</summary>

```python
def gamereset():
    global score
    score = 0
    myship.reset()
    bulletrect.y = OFFSCREEN_Y
    for i in range(UFO_COUNT):
        ufos[i].respawn()
```

</details>

ここまでで、`example/ex03.py` と同じ動きになる。UFO のリストを、`UFO` のインスタンスで管理するようになった。

### 実行する

ターミナルで、リポジトリのルートから実行する（自分のファイルなら、ファイル名を置き換える）。

```bash
python 19_shooting_game_class_ver/example/ex03.py
```

---

# ex04 — Bullet クラスを作る

弾の状態（発射中・待機中）と処理を、`Bullet` クラスにまとめる（完成形は [example/ex04.py](example/ex04.py)）。

## ステップ15. Bullet クラスの枠と __init__ を書く

ここから、弾をクラスにまとめる。`UFO` クラスの下に、2行空けて書く（弾の定数をここに移す）。

- `BULLET_SIZE = 16`、`BULLET_SPEED = 15` を書く（元の定数の行は、消す）
- 2行空けて、`class Bullet():` を定義する
- `def __init__(self, img):` で、画像を受け取り、`self.img` に持つ
- `self.rect = pg.Rect(0, OFFSCREEN_Y, BULLET_SIZE, BULLET_SIZE)` で、待機している弾（画面の外）の `Rect` を持つ

定数:

<details>
<summary>コードを見る</summary>

```python
BULLET_SIZE  = 16
BULLET_SPEED = 15
```

</details>

クラス:

<details>
<summary>コードを見る</summary>

```python
class Bullet():
    def __init__(self, img):
        self.img  = img
        self.rect = pg.Rect(0, OFFSCREEN_Y, BULLET_SIZE, BULLET_SIZE)
```

</details>

## ステップ16. shoot() を書く

`__init__` の下に、1行空けて書く。ex01 では `gamestage()` に書いていた、弾を発射する処理。

- `def shoot(self, x, y):` で、発射する位置を受け取る
- `if not self.is_active():`（発射中ではない）ときだけ、次の3つを行う（弾は1発だけ）
  - `self.rect.x = x`、`self.rect.y = y` で、位置を決める
  - `pg.mixer.Sound(SOUND_DIR / "pi.wav").play()` で、音を鳴らす

<details>
<summary>コードを見る</summary>

```python
    def shoot(self, x, y):
        if not self.is_active():
            self.rect.x = x
            self.rect.y = y
            pg.mixer.Sound(SOUND_DIR / "pi.wav").play()
```

</details>

## ステップ17. update() と draw() を書く

`shoot()` の下に、1行空けて、2つのメソッドを書く。発射中（`is_active()` が `True`）のときだけ、動かして描く。

- `def update(self):` で、`if self.is_active():` なら、`self.rect.y -= BULLET_SPEED` と、上に動かす
- `def draw(self):` で、`if self.is_active():` なら、`screen.blit(self.img, self.rect)` と、描く

<details>
<summary>コードを見る</summary>

```python
    def update(self):
        if self.is_active():
            self.rect.y -= BULLET_SPEED

    def draw(self):
        if self.is_active():
            screen.blit(self.img, self.rect)
```

</details>

## ステップ18. is_active()・deactivate()・reset() を書く

`draw()` の下に、1行空けて、3つのメソッドを書く。

- `def is_active(self):` で、`return self.rect.y >= 0` と、発射中かを返す（画面の外にいるときは `y` が `0` より小さい）
- `def deactivate(self):` で、`self.rect.y = OFFSCREEN_Y` と、待機状態に戻す（UFO に当たったとき）
- `def reset(self):` で、同じく `self.rect.y = OFFSCREEN_Y`（リプレイのとき）

<details>
<summary>コードを見る</summary>

```python
    def is_active(self):
        return self.rect.y >= 0

    def deactivate(self):
        self.rect.y = OFFSCREEN_Y

    def reset(self):
        self.rect.y = OFFSCREEN_Y
```

</details>

## ステップ19. bulletrect を bullet に置き換える

データの部分を書き換える。

- `bulletrect = pg.Rect(...)` の行を消す
- `bulletimg` を読み込む2行はそのまま残す
- その下に、`bullet = Bullet(bulletimg)` を足して、弾のインスタンスを作る

<details>
<summary>コードを見る</summary>

```python
bulletimg = pg.image.load(IMG_DIR / "bullet.png")
bulletimg = pg.transform.scale(bulletimg, (BULLET_SIZE, BULLET_SIZE))
bullet    = Bullet(bulletimg)
```

</details>

## ステップ20. gamestage() の弾の処理を書き換える

`gamestage()` を変更する。

- 弾を撃つ処理（`if mdown[0] and bulletrect.y < 0:` の3行）と、弾を動かして描く処理（`if bulletrect.y >= 0:` の2行）を、すべて消して、書き換える
  - `if mdown[0]:` なら、`bullet.shoot(...)` に、発射する位置（自機の中心から出す）を渡す
  - `bullet.update()` と `bullet.draw()` を呼ぶ（発射中かどうかは、`Bullet` の中で調べる）
- 弾との当たり判定を、`ufo.rect.colliderect(bullet.rect) and bullet.is_active()` に変える（待機中の弾に当たらないようにする）
- 当たったときの、`bulletrect.y = OFFSCREEN_Y` を、`bullet.deactivate()` にする

弾の処理:

<details>
<summary>コードを見る</summary>

```python
    if mdown[0]:
        bullet.shoot(myship.rect.x + SHIP_SIZE // 2 - BULLET_SIZE // 2, myship.rect.y)
    bullet.update()
    bullet.draw()
```

</details>

弾との当たり判定:

<details>
<summary>コードを見る</summary>

```python
        if ufo.rect.colliderect(bullet.rect) and bullet.is_active():
            score += SCORE_PER_HIT
            ufo.respawn()
            bullet.deactivate()
            pg.mixer.Sound(SOUND_DIR / "piko.wav").play()
```

</details>

## ステップ21. gamereset() で bullet.reset() を呼ぶ

`gamereset()` を変更する。

- `bulletrect.y = OFFSCREEN_Y` の行を、`bullet.reset()` にする

<details>
<summary>コードを見る</summary>

```python
def gamereset():
    global score
    score = 0
    myship.reset()
    bullet.reset()
    for i in range(UFO_COUNT):
        ufos[i].respawn()
```

</details>

ここまでで、`example/ex04.py` と同じ動きになる。自機・UFO・弾の3つが、クラスになった。

### 実行する

ターミナルで、リポジトリのルートから実行する（自分のファイルなら、ファイル名を置き換える）。

```bash
python 19_shooting_game_class_ver/example/ex04.py
```

---

# ex05 — UFO の速さをインスタンスごとに変える

`UFO` に `speed` 属性を足して、UFO ごとに落ちる速さを変える。クラス化の完成形（完成形は [example/ex05.py](example/ex05.py)）。

## ステップ22. UFO に speed を持たせる

ここから、UFO ごとに、落ちる速さを変える。`UFO` クラスを書き換える。

- 定数の `UFO_SPEED = 10` を、`UFO_SPEED_RANGE = (5, 15)` に変える（速さの範囲）
- `__init__` の引数を `(self, img, x, y, speed)` に変え、`self.speed = speed` を足す
- `update()` の `self.rect.y += UFO_SPEED` を、`self.rect.y += self.speed` に変える

定数:

<details>
<summary>コードを見る</summary>

```python
UFO_SIZE = 50
UFO_COUNT = 10
UFO_SPEED_RANGE = (5, 15)
OFFSCREEN_Y = -100
```

</details>

__init__:

<details>
<summary>コードを見る</summary>

```python
class UFO():
    def __init__(self, img, x, y, speed):
        self.img   = img
        self.rect  = pg.Rect(x, y, UFO_SIZE, UFO_SIZE)
        self.speed = speed
```

</details>

update():

<details>
<summary>コードを見る</summary>

```python
    def update(self):
        self.rect.y += self.speed
```

</details>

## ステップ23. UFO を作るとき、速さをランダムに決める

UFO のインスタンスを作る部分を書き換える。

- `UFO(...)` の最後の引数に、`random.randint(*UFO_SPEED_RANGE)` を足す（`*` で、範囲の2つの値を展開して渡す）

<details>
<summary>コードを見る</summary>

```python
ufoimg = pg.image.load(IMG_DIR / "UFO.png")
ufoimg = pg.transform.scale(ufoimg, (UFO_SIZE, UFO_SIZE))
ufos   = []
for i in range(UFO_COUNT):
    ufos.append(UFO(ufoimg, random.randint(0, WIDTH), OFFSCREEN_Y * i, random.randint(*UFO_SPEED_RANGE)))
```

</details>

ここまでで、`example/ex05.py` と同じ、完成版の動きになる。UFO ごとに、落ちる速さが違う。

### 実行する

ターミナルで、リポジトリのルートから実行する（自分のファイルなら、ファイル名を置き換える）。

```bash
python 19_shooting_game_class_ver/example/ex05.py
```

---

# ex06 — 難易度システムを追加する（発展）

スコアに応じて、UFO の速さ・動き方・背景の色を変える。`UFO` にジグザグと追跡の動きを足す（完成形は [example/ex06.py](example/ex06.py)）。

## ステップ24. 難易度のテーブルを作る

ここから、スコアに応じて、UFO の速さや動き、背景の色を変える（発展）。`ex05` をコピーして `ex06.py` にして、書き換えてもよい。

ウィンドウの設定（`clock = ...`）の下に、1行空けて書く。

- `LEVELS = [ ... ]` で、難易度の一覧（辞書のリスト）を作る
  - 1つの辞書が、1つの難易度。`min_score`（このスコア以上）、`name`（表示する名前）、`speed`（UFO の速さ）、`move`（動き方）、`bg`（背景の色）を持つ
  - スコアが高い順に並べる（次のステップで、先頭から調べるため）
- また、`import math` を、`import` の行に足す（あとで `sin` を使う）
- `pg.display.set_caption(...)` の文字を、`"シューティングゲーム 発展版"` に変える

import:

<details>
<summary>コードを見る</summary>

```python
import math
```

</details>

タイトル:

<details>
<summary>コードを見る</summary>

```python
pg.display.set_caption("シューティングゲーム 発展版")
```

</details>

テーブル:

<details>
<summary>コードを見る</summary>

```python
# 難易度テーブル（スコアが高い順に並べる）
LEVELS = [
    {"min_score": 300, "name": "CHASE",  "speed": 10, "move": "chase",  "bg": (60,  0,   0)},
    {"min_score": 200, "name": "ZIGZAG", "speed":  7, "move": "zigzag", "bg": (0,   50,  0)},
    {"min_score": 100, "name": "FAST",   "speed":  7, "move": "fast",   "bg": (50,  0,   80)},
    {"min_score":   0, "name": "NORMAL", "speed":  4, "move": "normal", "bg": (0,   0,   128)},
]
```

</details>

## ステップ25. get_level() を書く

`LEVELS` の下に、2行空けて書く。スコアに合った難易度を返す関数。

- `def get_level(score):` を定義する
- `for lv in LEVELS:` で、先頭から順に調べ、`if score >= lv["min_score"]:` なら、`return lv`（高い順に並べているので、最初に当てはまったものが、今の難易度）
- どれにも当てはまらなければ、`return LEVELS[-1]`（いちばん低い難易度）

<details>
<summary>コードを見る</summary>

```python
def get_level(score):
    for lv in LEVELS:
        if score >= lv["min_score"]:
            return lv
    return LEVELS[-1]
```

</details>

## ステップ26. UFO の定数を足す

UFO の定数を書き換える。

- `UFO_SPEED_RANGE` の行は、消す（速さは、難易度で決まる）
- `UFO_X_MAX = WIDTH - UFO_SIZE` を足す（UFO が横に動いても、画面から出ない、X座標の上限）
- 動き方の定数を足す: `ZIGZAG_STEP = 3`（ジグザグの角度の増え方）、`ZIGZAG_RANGE = 6`（ジグザグの横幅）、`CHASE_STEP = 3`（追いかける速さ）
- `MyShip`・`UFO`・`Bullet` の `class` の行は、`()` を付けなくてもよい（ex06 では `class UFO:` のように、省略している）

<details>
<summary>コードを見る</summary>

```python
UFO_SIZE  = 50
UFO_COUNT = 10
OFFSCREEN_Y = -100
UFO_X_MAX = WIDTH - UFO_SIZE   # ジグザグ・リスポーン時のX座標の上限(750)
ZIGZAG_STEP  = 3
ZIGZAG_RANGE = 6
CHASE_STEP   = 3
```

</details>

## ステップ27. UFO の __init__ を書き換える

`UFO.__init__` を書き換える。速さは、難易度で決まるので、引数では受け取らない。

- 引数を `(self, img, x, y)` に戻す（`speed` を、やめる）
- `self.speed = 4` で、最初の速さを決める
- `self.move_type = "normal"` で、最初の動き方を決める
- `self.phase = random.randint(0, 360)` で、ジグザグの角度の最初の値を決める（UFO ごとにずらすので、全員が同じ動きにならない）

<details>
<summary>コードを見る</summary>

```python
class UFO:
    def __init__(self, img, x, y):
        self.img       = img
        self.rect      = pg.Rect(x, y, UFO_SIZE, UFO_SIZE)
        self.speed     = 4
        self.move_type = "normal"
        self.phase     = random.randint(0, 360)   # 各 UFO の位相をずらす
```

</details>

## ステップ28. set_difficulty() を書く

`__init__` の下に、1行空けて書く。スコアに合わせて、UFO の速さと動き方を変える。

- `def set_difficulty(self, score):` を定義する
- `lv = get_level(score)` で、今の難易度を求める
- `self.speed = lv["speed"]`、`self.move_type = lv["move"]` で、難易度の値を、UFO に入れる

<details>
<summary>コードを見る</summary>

```python
    def set_difficulty(self, score):
        lv             = get_level(score)
        self.speed     = lv["speed"]
        self.move_type = lv["move"]
```

</details>

## ステップ29. update() を書き換える：下に動かして、画面外で戻す

`UFO.update()` を書き換える。

- 引数を `(self, ship_x)` に変える（追いかける動きで、自機のX座標を使う）
- 最初の行は、`self.rect.y += self.speed`（そのまま）
- 一番最後に、`if self.rect.y > HEIGHT:`（画面の下に出た）なら、`self.respawn()` と、上に戻す（今までの、`x`・`y` を直接書き換える2行を、これに置き換える）

はじめ:

<details>
<summary>コードを見る</summary>

```python
    def update(self, ship_x):
        self.rect.y += self.speed
```

</details>

おわり:

<details>
<summary>コードを見る</summary>

```python
        if self.rect.y > HEIGHT:
            self.respawn()
```

</details>

## ステップ30. ジグザグに動かす

`update()` の、`self.rect.y += self.speed` の下に、1行空けて書く。

- `if self.move_type == "zigzag":` のとき、次を行う
  - `self.phase += ZIGZAG_STEP` で、角度を進める
  - `dx = int(math.sin(math.radians(self.phase)) * ZIGZAG_RANGE)` で、`sin` を使って、左右にゆれる量を求める（`radians()` で、角度をラジアンに変える）
  - `self.rect.x += dx` で、横に動かす
  - `self.rect.x` が `0` より小さければ `0` に、`UFO_X_MAX` より大きければ `UFO_X_MAX` にして、画面の中に収める

<details>
<summary>コードを見る</summary>

```python
        if self.move_type == "zigzag":
            self.phase += ZIGZAG_STEP
            dx = int(math.sin(math.radians(self.phase)) * ZIGZAG_RANGE)
            self.rect.x += dx
            if self.rect.x < 0:
                self.rect.x = 0
            if self.rect.x > UFO_X_MAX:
                self.rect.x = UFO_X_MAX
```

</details>

## ステップ31. 自機を追いかける

ジグザグの `if` の下に、続けて書く（`elif`）。

- `elif self.move_type == "chase":` のとき、次を行う
  - `target_x = ship_x - SHIP_SIZE // 2` で、自機の左端のX座標を求める
  - `self.rect.x < target_x`（自機より左）なら `self.rect.x += CHASE_STEP`、`self.rect.x > target_x`（自機より右）なら `self.rect.x -= CHASE_STEP` と、自機に近づく向きに動かす

<details>
<summary>コードを見る</summary>

```python
        elif self.move_type == "chase":
            target_x = ship_x - SHIP_SIZE // 2
            if self.rect.x < target_x:
                self.rect.x += CHASE_STEP
            elif self.rect.x > target_x:
                self.rect.x -= CHASE_STEP
```

</details>

## ステップ32. respawn() を書き換える

`respawn()` を書き換える。

- `self.rect.x` の範囲を、`random.randint(0, UFO_X_MAX)` にする（画面から、はみ出さないように）
- 最後に、`self.phase = random.randint(0, 360)` を足して、ジグザグの角度も決め直す

<details>
<summary>コードを見る</summary>

```python
    def respawn(self):
        self.rect.x = random.randint(0, UFO_X_MAX)
        self.rect.y = OFFSCREEN_Y
        self.phase  = random.randint(0, 360)
```

</details>

## ステップ33. UFO を作るとき、X座標の範囲を変える

UFO のインスタンスを作る部分を書き換える。

- `random.randint(0, WIDTH)` を、`random.randint(0, UFO_X_MAX)` に変える
- 最後の引数の、速さ（`random.randint(*UFO_SPEED_RANGE)`）は、消す

<details>
<summary>コードを見る</summary>

```python
for i in range(UFO_COUNT):
    ufos.append(UFO(ufoimg, random.randint(0, UFO_X_MAX), OFFSCREEN_Y * i))
```

</details>

## ステップ34. gamestage() の背景を難易度の色にする

`gamestage()` の最初を書き換える。

- `screen.fill(pg.Color("NAVY"))` を消して、`lv = get_level(score)` で、今の難易度を求める
- `screen.fill(lv["bg"])` で、難易度の背景の色で塗りつぶす

<details>
<summary>コードを見る</summary>

```python
    lv = get_level(score)
    screen.fill(lv["bg"])
```

</details>

## ステップ35. UFO に難易度を伝える

UFO の処理（`for ufo in ufos:` の中）を変更する。

- `ufo.update()` の前に、`ufo.set_difficulty(score)` を足す（スコアに合った速さ・動き方にする）
- `ufo.update()` を、`ufo.update(myship.rect.x)` に変える（自機のX座標を渡す）

<details>
<summary>コードを見る</summary>

```python
    for ufo in ufos:
        ufo.set_difficulty(score)
        ufo.update(myship.rect.x)
        ufo.draw()
```

</details>

## ステップ36. スコアと難易度を表示する

`gamestage()` の一番最後の、スコアを描く部分を書き換える。

- `font = pg.font.Font(None, SCORE_FONT_SIZE)` の下に、`small = pg.font.Font(None, 28)` を足す（小さい文字用）
- `score_text = font.render("SCORE: " + str(score), True, pg.Color("WHITE"))` で、スコアの文字を作り、`screen.blit(score_text, SCORE_POS)` で描く
- `lv_text = font.render("LEVEL: " + lv["name"], True, pg.Color("YELLOW"))` で、難易度の名前の文字を作り、`screen.blit(lv_text, (20, 58))` で描く

<details>
<summary>コードを見る</summary>

```python
    font  = pg.font.Font(None, SCORE_FONT_SIZE)
    small = pg.font.Font(None, 28)

    score_text = font.render("SCORE: " + str(score), True, pg.Color("WHITE"))
    screen.blit(score_text, SCORE_POS)

    lv_text = font.render("LEVEL: " + lv["name"], True, pg.Color("YELLOW"))
    screen.blit(lv_text, (20, 58))
```

</details>

## ステップ37. 次のレベルまでの残りを表示する

難易度の表示の下に、1行空けて書く。

- `next_score = 0` で、次の難易度のスコアを、`0` にしておく
- `for lv_data in reversed(LEVELS):`（低い難易度から順に調べる）で、`if lv_data["min_score"] > score:`（今のスコアより高い）最初のものを見つけたら、`next_score` に入れて、`break` する
- `if next_score > 0:`（次の難易度がある）なら、`remain = next_score - score` で、残りの点数を求める
- `hint = small.render("NEXT LV: " + str(remain) + " pts", True, pg.Color("LIGHTGRAY"))` で、文字を作り、`screen.blit(hint, (20, 90))` で描く

<details>
<summary>コードを見る</summary>

```python
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

## ステップ38. ゲームオーバー画面のスコアの文字をそろえる

`gameover()` の中のスコアの文字を、`"SCORE: "` と、コロンの後ろに空白を入れた形にそろえる（`gamestage()` と同じ形）。

- `text = font.render("SCORE: " + str(score), True, pg.Color("WHITE"))` に変える

<details>
<summary>コードを見る</summary>

```python
    text = font.render("SCORE: " + str(score), True, pg.Color("WHITE"))
```

</details>

ここまでで、`example/ex06.py` と同じ動きになる。スコアが上がると、UFO が速くなったり、ジグザグに動いたり、自機を追いかけたりする。

### 実行する

ターミナルで、リポジトリのルートから実行する（自分のファイルなら、ファイル名を置き換える）。

```bash
python 19_shooting_game_class_ver/example/ex06.py
```

---

# package — クラスごとにファイルを分割する

`ex06.py` は、`LEVELS`・3つのクラス・画面制御の関数が1つのファイルに入っていて、どこに何があるか探しにくい。[18_module](../18_module/README.md) で学んだパッケージ・相対インポートを使って、クラスごとに別ファイルに分ける（完成形は [package/main.py](package/main.py) と [package/game/](package/game/)）。

## ステップ39. game/ フォルダと __init__.py を作る

ここから、`ex06.py` を、クラスごとにファイル分割する。`example/` とは別の場所（`package/`）に、新しく作る。

- `package/` フォルダを作り、その中に `game/` フォルダを作る
- `game/` の中に、空の `__init__.py` を作る（フォルダを、パッケージとして認識させる目印。中身は、最後のステップで書く）
- `package/` の中に、`main.py` を作る（のちほど書く）

```
package/
├── main.py
└── game/
    ├── __init__.py
    ├── level.py
    ├── myship.py
    ├── ufo.py
    └── bullet.py
```

## ステップ40. level.py：難易度のテーブルを移す

`game/level.py` を新しく作る。`ex06.py` の `LEVELS` と `get_level()` を、そのまま移す。他のクラスから使う「難易度の定義」なので、クラスとは別のファイルにする。

- `LEVELS` と `get_level()` を、`ex06.py` からコピーする（`pygame` は使わないので、`import` は不要）

<details>
<summary>コードを見る</summary>

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

## ステップ41. myship.py：MyShip クラスを移す

`game/myship.py` を新しく作る。`MyShip` クラスを、`ex06.py` から移す。

- 先頭に、`import pygame as pg` を書く
- `SHIP_SIZE = 50` を書く（`main.py` にある定数は、このファイルからは見えないので、使う定数は、このファイルの先頭に書き直す）
- `MyShip` クラスをコピーして、`draw()` を `draw(self, screen)` に変える。`screen` は `main.py` にあるので、引数で受け取る

<details>
<summary>コードを見る</summary>

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

## ステップ42. ufo.py：定数とインポート

`game/ufo.py` を新しく作る。まず、先頭の部分。

- `import math`、`import random`、`import pygame as pg` を書く
- `from .level import get_level` を書く（先頭の `.` は、同じパッケージ `game/` の中の `level.py` を指す相対インポート。→ [18_module](../18_module/README.md)）
- `UFO` が使う定数を、このファイルの先頭に書き直す: `HEIGHT`、`SHIP_SIZE`、`UFO_SIZE`、`OFFSCREEN_Y`、`UFO_X_MAX`、`ZIGZAG_STEP`、`ZIGZAG_RANGE`、`CHASE_STEP`
  - `WIDTH` は、このファイルでは使わないので、`UFO_X_MAX` は `800 - UFO_SIZE` と、直接書く

<details>
<summary>コードを見る</summary>

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
```

</details>

## ステップ43. ufo.py：UFO クラス

定数の下に、2行空けて、`UFO` クラスを書く。`ex06.py` からコピーして、`draw()` を `draw(self, screen)` に変える。それ以外は、同じ。

- `HEIGHT` は、このファイルの先頭の定数を使う

<details>
<summary>コードを見る</summary>

```python
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

## ステップ44. bullet.py：Bullet クラスを移す

`game/bullet.py` を新しく作る。`Bullet` クラスを、`ex06.py` から移す。

- `Path` と `pygame` を読み込み、`BASE_DIR` と `SOUND_DIR` を、このファイルの先頭に書き直す。このファイルは `package/game/` の中なので、`.parent` が3つ必要（`bullet.py` → `game/` → `package/` → `19_shooting_game_class_ver/`）
- `BULLET_SIZE`、`BULLET_SPEED`、`OFFSCREEN_Y` を書く
- `Bullet` クラスをコピーして、`draw()` を `draw(self, screen)` に変える

<details>
<summary>コードを見る</summary>

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

## ステップ45. __init__.py：各クラスをまとめて公開する

`game/__init__.py` に書く。外から、`from game import ...` だけで使えるようにする。

- `from .level import LEVELS, get_level`
- `from .myship import MyShip`
- `from .ufo import UFO`
- `from .bullet import Bullet`

<details>
<summary>コードを見る</summary>

```python
from .level import LEVELS, get_level
from .myship import MyShip
from .ufo import UFO
from .bullet import Bullet
```

</details>

## ステップ46. main.py：インポートと準備

`main.py` の、はじめの部分を書く。`ex06.py` をコピーして、クラスの定義（`LEVELS`・`get_level()`・`MyShip`・`UFO`・`Bullet`）をすべて消し、`import math` も消す（`math` は `ufo.py` でしか使わない）。

- `from game import MyShip, UFO, Bullet, LEVELS, get_level` を書く（`game/` パッケージの外にある `main.py` から、直接インポートできる）
- `pg.display.set_caption(...)` の文字を、`"シューティングゲーム 発展版（ファイル分割）"` にする
- クラスが使っていた定数のうち、`main.py` でも使うもの（`SHIP_SIZE`・`UFO_SIZE`・`BULLET_SIZE` など）は、残しておく

<details>
<summary>コードを見る</summary>

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
```

</details>

## ステップ47. main.py：button_to_jump()

準備の下に、2行空けて書く。`ex06.py` と同じ（変更なし）。

<details>
<summary>コードを見る</summary>

```python
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
```

</details>

## ステップ48. main.py：gamestage()

`button_to_jump()` の下に、2行空けて書く。`ex06.py` の `gamestage()` と同じだが、`draw()` の呼び出しに `screen` を渡す。

- `myship.draw()` を、`myship.draw(screen)` に変える
- `bullet.draw()` を、`bullet.draw(screen)` に変える
- `ufo.draw()` を、`ufo.draw(screen)` に変える

<details>
<summary>コードを見る</summary>

```python
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
```

</details>

## ステップ49. main.py：gamereset()・gameover()・ゲームループ

`gamestage()` の下に、`ex06.py` と同じものを書く（変更なし）。

<details>
<summary>コードを見る</summary>

```python
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

ここまでで、`package/main.py` が、`example/ex06.py` と同じ動きになる。クラスの中身がなくなった分、`main.py` は「準備」と「ゲームループ」だけになった。

### 実行する

ターミナルで、リポジトリのルートから実行する（自分のファイルなら、ファイル名を置き換える）。

```bash
python 19_shooting_game_class_ver/package/main.py
```
