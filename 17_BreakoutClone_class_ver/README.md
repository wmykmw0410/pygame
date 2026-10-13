```text
13_BreakoutClone の関数ベースのコードを、クラスを使って段階的に書き直します
```

# 目次
- [ex01 — 出発点：関数ベースのコード](#ex01--出発点関数ベースのコード)
  - [ステップ1. 出発点のコードを用意する](#ステップ1-出発点のコードを用意する)
- [ex02 — Ball クラスにまとめる](#ex02--ball-クラスにまとめる)
  - [ステップ2. Ball クラスの枠と __init__ を書く](#ステップ2-ball-クラスの枠と-__init__-を書く)
  - [ステップ3. 壁での跳ね返り bounce_wall() を書く](#ステップ3-壁での跳ね返り-bounce_wall-を書く)
  - [ステップ4. バーでの跳ね返り bounce_bar() を書く](#ステップ4-バーでの跳ね返り-bounce_bar-を書く)
  - [ステップ5. move() と draw() を書く](#ステップ5-move-と-draw-を書く)
  - [ステップ6. is_out() と reset() を書く](#ステップ6-is_out-と-reset-を書く)
  - [ステップ7. ボールの変数を Ball に置き換える](#ステップ7-ボールの変数を-ball-に置き換える)
  - [ステップ8. gamestage() のボールの処理を書き換える](#ステップ8-gamestage-のボールの処理を書き換える)
  - [ステップ9. ブロックの判定でも、ball のプロパティを使う](#ステップ9-ブロックの判定でもball-のプロパティを使う)
  - [ステップ10. gamereset() で ball.reset() を呼ぶ](#ステップ10-gamereset-で-ballreset-を呼ぶ)
- [ex03 — Block クラスを作る](#ex03--block-クラスを作る)
  - [ステップ11. Block クラスを書く](#ステップ11-block-クラスを書く)
  - [ステップ12. draw() と check_hit() を書く](#ステップ12-draw-と-check_hit-を書く)
  - [ステップ13. make_blocks() 関数を書く](#ステップ13-make_blocks-関数を書く)
  - [ステップ14. ブロックのリストを make_blocks() で作る](#ステップ14-ブロックのリストを-make_blocks-で作る)
  - [ステップ15. gamestage() のブロックの処理を書き換える](#ステップ15-gamestage-のブロックの処理を書き換える)
  - [ステップ16. gamereset() でブロックを作り直す](#ステップ16-gamereset-でブロックを作り直す)
- [ex04 — Bar クラスを作る](#ex04--bar-クラスを作る)
  - [ステップ17. Bar クラスを書く](#ステップ17-bar-クラスを書く)
  - [ステップ18. barrect を bar に置き換える](#ステップ18-barrect-を-bar-に置き換える)
  - [ステップ19. bounce_bar() が Bar を受け取るようにする](#ステップ19-bounce_bar-が-bar-を受け取るようにする)
  - [ステップ20. Block に色を持たせる](#ステップ20-block-に色を持たせる)
  - [ステップ21. make_blocks() で行ごとの色を渡す](#ステップ21-make_blocks-で行ごとの色を渡す)
- [ex05 — ボールを複数に増やす](#ex05--ボールを複数に増やす)
  - [ステップ22. Ball の開始位置を引数にする](#ステップ22-ball-の開始位置を引数にする)
  - [ステップ23. make_balls() 関数を書く](#ステップ23-make_balls-関数を書く)
  - [ステップ24. ball を balls リストに置き換える](#ステップ24-ball-を-balls-リストに置き換える)
  - [ステップ25. 全ボールを動かして、画面外のボールを除く](#ステップ25-全ボールを動かして画面外のボールを除く)
  - [ステップ26. ブロックを壊すたびに、ボールを増やす](#ステップ26-ブロックを壊すたびにボールを増やす)
  - [ステップ27. gamereset() でボールを作り直す](#ステップ27-gamereset-でボールを作り直す)

---

# ex01 — 出発点：関数ベースのコード

13_BreakoutClone の完成コードを、ここからクラスに書き直していく（コードは [example/ex01.py](example/ex01.py)）。

## ステップ1. 出発点のコードを用意する

[13_BreakoutClone](../13_BreakoutClone/README.md) の完成コード（`13_BreakoutClone/example/ex03.py`）を、新しい `.py` ファイルにコピーする。これが、クラス化していく出発点になる（ここでは何も書き足さない）。

- 作りは、関数ベース。ボールは `ballrect`・`vx`・`vy`・`ballimg` の4つの変数、バーは `barrect`、ブロックは `pg.Rect` のリストで、バラバラに持っている
- `gamestage()` の中で、これらの変数を直接書き換えている（`ballrect.x += vx` など）
- 変数が増えるほど管理が大変になる。次のステップから、クラスにまとめていく
- `example/ex01.py` は、同じ内容で、定数の並べ方だけが少し違う（動きは同じ）。コードは、答え合わせ用に載せておく

<details>
<summary>コードを見る</summary>

```python
from pathlib import Path
import pygame as pg
import sys
import random

pg.init()
BASE_DIR = Path(__file__).resolve().parent.parent
IMG_DIR  = BASE_DIR / "images"
SND_DIR  = BASE_DIR / "sounds"

WIDTH, HEIGHT = 800, 600

FPS = 60

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("BreakoutClone")
clock = pg.time.Clock()

BAR_SIZE = (100, 20)
BALL_SIZE = 30
INITIAL_VX_RANGE = (-10, 10)
INITIAL_VY = -5
BOUNCE_VY_RANGE = (-10, -5)
BLOCK_ROWS    = 4
BLOCK_COLS    = 7
BLOCK_START   = (50, 40)
BLOCK_SPACING = (100, 50)
BLOCK_SIZE    = (80, 30)
REPLAY_BTN_POS   = (320, 480)
RESULT_FONT_SIZE = 150

barrect  = pg.Rect(400, 500, *BAR_SIZE)
ballimg  = pg.image.load(IMG_DIR / "kaeru.png")
ballimg  = pg.transform.scale(ballimg, (BALL_SIZE, BALL_SIZE))
ballrect = pg.Rect(400, 450, BALL_SIZE, BALL_SIZE)
vx = random.randint(*INITIAL_VX_RANGE)
vy = INITIAL_VY

replay_img = pg.image.load(IMG_DIR / "replaybtn.png")

blocks = []
for yy in range(BLOCK_ROWS):
    for xx in range(BLOCK_COLS):
        blocks.append(pg.Rect(BLOCK_START[0] + xx * BLOCK_SPACING[0],
                               BLOCK_START[1] + yy * BLOCK_SPACING[1], *BLOCK_SIZE))

pushFlag = False
page     = 1
score    = 0


def button_to_jump(btn, newpage):
    global page, pushFlag
    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()
    if mdown[0]:
        if btn.collidepoint(mx, my) and not pushFlag:
            pg.mixer.Sound(SND_DIR / "pi.wav").play()
            page = newpage
            pushFlag = True
    else:
        pushFlag = False


def gamestage():
    global vx, vy, page, score
    screen.fill(pg.Color("NAVY"))
    (mx, my) = pg.mouse.get_pos()

    barrect.x = mx - BAR_SIZE[0] // 2
    pg.draw.rect(screen, pg.Color("CYAN"), barrect)

    if ballrect.y < 0:
        vy = -vy
    if ballrect.x < 0 or ballrect.x > WIDTH - BALL_SIZE:
        vx = -vx
    if barrect.colliderect(ballrect):
        vx = int(((ballrect.x + BALL_SIZE // 2) - (barrect.x + BAR_SIZE[0] // 2)) / 4)
        vy = random.randint(*BOUNCE_VY_RANGE)
        pg.mixer.Sound(SND_DIR / "pi.wav").play()
    if ballrect.y > HEIGHT:
        page = 2
        pg.mixer.Sound(SND_DIR / "pi.wav").play()
    ballrect.x += vx
    ballrect.y += vy
    screen.blit(ballimg, ballrect)

    for n, block in enumerate(blocks):
        pg.draw.rect(screen, pg.Color("GOLD"), block)
        if block.colliderect(ballrect):
            pg.mixer.Sound(SND_DIR / "piko.wav").play()
            vy = -vy
            blocks[n] = pg.Rect(0, 0, 0, 0)
            score += 1
            if score == BLOCK_ROWS * BLOCK_COLS:
                pg.mixer.Sound(SND_DIR / "up.wav").play()
                page = 3


def gamereset():
    global vx, vy, score, blocks
    vx = random.randint(*INITIAL_VX_RANGE)
    vy = INITIAL_VY
    ballrect.x = 400
    ballrect.y = 450
    score  = 0
    blocks = []
    for yy in range(BLOCK_ROWS):
        for xx in range(BLOCK_COLS):
            blocks.append(pg.Rect(BLOCK_START[0] + xx * BLOCK_SPACING[0],
                                   BLOCK_START[1] + yy * BLOCK_SPACING[1], *BLOCK_SIZE))


def gameover():
    gamereset()
    screen.fill(pg.Color("NAVY"))
    font = pg.font.Font(None, RESULT_FONT_SIZE)
    text = font.render("GAMEOVER", True, pg.Color("RED"))
    screen.blit(text, (100, 200))
    btn1 = screen.blit(replay_img, REPLAY_BTN_POS)
    button_to_jump(btn1, 1)


def gameclear():
    gamereset()
    screen.fill(pg.Color("GOLD"))
    font = pg.font.Font(None, RESULT_FONT_SIZE)
    text = font.render("GAMECLEAR", True, pg.Color("RED"))
    screen.blit(text, (60, 200))
    btn1 = screen.blit(replay_img, REPLAY_BTN_POS)
    button_to_jump(btn1, 1)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    if page == 1:
        gamestage()
    elif page == 2:
        gameover()
    elif page == 3:
        gameclear()
    pg.display.update()
    clock.tick(FPS)
```

</details>

ここまでで、`example/ex01.py` と同じ動きになる。マウスでバーを動かして、ボールでブロックを壊す。

### 実行する

ターミナルで、リポジトリのルートから実行する（自分のファイルなら、ファイル名を置き換える）。

```bash
python 17_BreakoutClone_class_ver/example/ex01.py
```

---

# ex02 — Ball クラスにまとめる

`ballrect` / `vx` / `vy` / `ballimg` というバラバラな変数と、ボールに関する処理を、`Ball` クラスに集める（完成形は [example/ex02.py](example/ex02.py)）。

## ステップ2. Ball クラスの枠と __init__ を書く

ここから、クラスにまとめていく。`ex01` をコピーして `ex02.py` にして、書き換えてもよい。

ボールの定数（`BALL_SIZE` など）の下に、2行空けて書く。

- `class Ball():` を定義する
- `def __init__(self, img):` で、画像を受け取る
- `self.img = img` で、画像を持つ
- `self.rect = pg.Rect(400, 450, BALL_SIZE, BALL_SIZE)` で、位置と大きさ（`ballrect` だったもの）を持つ
- `self.vx = random.randint(*INITIAL_VX_RANGE)`、`self.vy = INITIAL_VY` で、速度（`vx`・`vy` だったもの）を持つ

<details>
<summary>コードを見る</summary>

```python
class Ball():
    def __init__(self, img):
        self.img  = img
        self.rect = pg.Rect(400, 450, BALL_SIZE, BALL_SIZE)
        self.vx   = random.randint(*INITIAL_VX_RANGE)
        self.vy   = INITIAL_VY
```

</details>

## ステップ3. 壁での跳ね返り bounce_wall() を書く

`__init__` の下に、1行空けて書く。`gamestage()` にあった壁の判定を、メソッドに移す。`ballrect` は `self.rect`、`vx`・`vy` は `self.vx`・`self.vy` に変わる。

- `def bounce_wall(self):` を定義する
- `self.rect.y < 0`（上の壁）なら、`self.vy = -self.vy`
- `self.rect.x < 0 or self.rect.x > WIDTH - BALL_SIZE`（左右の壁）なら、`self.vx = -self.vx`

<details>
<summary>コードを見る</summary>

```python
    def bounce_wall(self):
        if self.rect.y < 0:
            self.vy = -self.vy
        if self.rect.x < 0 or self.rect.x > WIDTH - BALL_SIZE:
            self.vx = -self.vx
```

</details>

## ステップ4. バーでの跳ね返り bounce_bar() を書く

`bounce_wall()` の下に、1行空けて書く。

- `def bounce_bar(self, barrect):` で、バーの `Rect` を受け取る
- `if barrect.colliderect(self.rect):`（バーに当たった）のとき
  - `self.vx = int(((self.rect.x + BALL_SIZE // 2) - (barrect.x + BAR_SIZE[0] // 2)) / 4)` で、ボールの中心とバーの中心のずれから、横の速度を決める
  - `self.vy = random.randint(*BOUNCE_VY_RANGE)` で、上向きの速度をランダムに決める
  - `pg.mixer.Sound(SND_DIR / "pi.wav").play()` で、音を鳴らす

<details>
<summary>コードを見る</summary>

```python
    def bounce_bar(self, barrect):
        if barrect.colliderect(self.rect):
            self.vx = int(((self.rect.x + BALL_SIZE // 2) - (barrect.x + BAR_SIZE[0] // 2)) / 4)
            self.vy = random.randint(*BOUNCE_VY_RANGE)
            pg.mixer.Sound(SND_DIR / "pi.wav").play()
```

</details>

## ステップ5. move() と draw() を書く

`bounce_bar()` の下に、1行空けて、2つのメソッドを書く。

- `def move(self):` で、`self.rect.x += self.vx` と `self.rect.y += self.vy` と、速度の分だけ動かす
- `def draw(self):` で、`screen.blit(self.img, self.rect)` と、画像を描く

<details>
<summary>コードを見る</summary>

```python
    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

    def draw(self):
        screen.blit(self.img, self.rect)
```

</details>

## ステップ6. is_out() と reset() を書く

`draw()` の下に、1行空けて、2つのメソッドを書く。

- `def is_out(self):` で、`return self.rect.y > HEIGHT` と、画面の下に出たかを返す
- `def reset(self):` で、`self.rect.x = 400`、`self.rect.y = 450` と位置を戻し、`self.vx` と `self.vy` も、`__init__` と同じ式で初期値に戻す（リプレイのときに使う）

<details>
<summary>コードを見る</summary>

```python
    def is_out(self):
        return self.rect.y > HEIGHT

    def reset(self):
        self.rect.x = 400
        self.rect.y = 450
        self.vx = random.randint(*INITIAL_VX_RANGE)
        self.vy = INITIAL_VY
```

</details>

## ステップ7. ボールの変数を Ball に置き換える

クラスの下の、データの部分を書き換える。

- `ballrect = pg.Rect(...)`、`vx = ...`、`vy = ...` の3行は、消す（`Ball` が持つようになった）
- `ballimg` を読み込む2行は、そのまま残す
- その下に、`ball = Ball(ballimg)` を足して、ボールのインスタンスを1つ作る

<details>
<summary>コードを見る</summary>

```python
ballimg = pg.image.load(IMG_DIR / "kaeru.png")
ballimg = pg.transform.scale(ballimg, (BALL_SIZE, BALL_SIZE))
ball    = Ball(ballimg)
```

</details>

## ステップ8. gamestage() のボールの処理を書き換える

`gamestage()` を変更する。

- 関数の1行目の `global vx, vy, page, score` を、`global page, score` に変える（`vx`・`vy` はなくなったので）
- 壁の判定・バーの判定・`ballrect` の移動と描画の部分を、すべて消して、メソッドの呼び出しに書き換える
  - `ball.bounce_wall()` で、壁での跳ね返り
  - `ball.bounce_bar(barrect)` で、バーでの跳ね返り
  - `if ball.is_out():` なら、`page = 2` と、音を鳴らす（今までの `ballrect.y > HEIGHT` の判定と同じ）
  - `ball.move()` で動かし、`ball.draw()` で描く

`global` の行:

<details>
<summary>コードを見る</summary>

```python
    global page, score
```

</details>

ボールの処理:

<details>
<summary>コードを見る</summary>

```python
    ball.bounce_wall()
    ball.bounce_bar(barrect)
    if ball.is_out():
        page = 2
        pg.mixer.Sound(SND_DIR / "pi.wav").play()
    ball.move()
    ball.draw()
```

</details>

## ステップ9. ブロックの判定でも、ball のプロパティを使う

ブロックの処理（`for n, block in enumerate(blocks):`）の中を、2か所変える。

- `block.colliderect(ballrect)` を、`block.colliderect(ball.rect)` に変える
- `vy = -vy` を、`ball.vy = -ball.vy` に変える

<details>
<summary>コードを見る</summary>

```python
    for n, block in enumerate(blocks):
        pg.draw.rect(screen, pg.Color("GOLD"), block)
        if block.colliderect(ball.rect):
            pg.mixer.Sound(SND_DIR / "piko.wav").play()
            ball.vy = -ball.vy
            blocks[n] = pg.Rect(0, 0, 0, 0)
```

</details>

## ステップ10. gamereset() で ball.reset() を呼ぶ

`gamereset()` を変更する。

- `global vx, vy, score, blocks` を、`global score, blocks` に変える
- `vx`・`vy`・`ballrect` を戻していた4行を、消して、`ball.reset()` の1行にする

<details>
<summary>コードを見る</summary>

```python
def gamereset():
    global score, blocks
    ball.reset()
    score  = 0
```

</details>

ここまでで、`example/ex02.py` と同じ動きになる。動きは ex01 と同じで、ボールの持ち物（位置・速度・画像）と処理が `Ball` にまとまった。

### 実行する

ターミナルで、リポジトリのルートから実行する（自分のファイルなら、ファイル名を置き換える）。

```bash
python 17_BreakoutClone_class_ver/example/ex02.py
```

---

# ex03 — Block クラスを作る

ブロックを `pg.Rect` のリストから `Block` クラスのリストに変える。「消えているか」を `active` フラグで管理し、当たり判定を `check_hit()` に持たせる（完成形は [example/ex03.py](example/ex03.py)）。

## ステップ11. Block クラスを書く

ここから、ブロックをクラスにまとめる。`Ball` クラスの下に、2行空けて書く。

- `BLOCK_SIZE = (80, 30)` を書く（元の `BLOCK_SIZE` の行は、消す）
- 2行空けて、`class Block():` を定義する
- `def __init__(self, x, y):` で、位置を受け取る
- `self.rect = pg.Rect(x, y, *BLOCK_SIZE)` で、ブロックの `Rect` を持つ
- `self.active = True` で、まだ壊れていないかを表す印（フラグ）を持つ（今までは、壊したブロックを `pg.Rect(0, 0, 0, 0)` に置き換えて消していた）

<details>
<summary>コードを見る</summary>

```python
BLOCK_SIZE = (80, 30)


class Block():
    def __init__(self, x, y):
        self.rect   = pg.Rect(x, y, *BLOCK_SIZE)
        self.active = True
```

</details>

## ステップ12. draw() と check_hit() を書く

`__init__` の下に、1行空けて、2つのメソッドを書く。

- `def draw(self):` で、`if self.active:`（壊れていない）ときだけ、`pg.draw.rect(screen, pg.Color("GOLD"), self.rect)` と描く
- `def check_hit(self, ball):` で、ボールとの当たり判定をする
  - `if self.active and self.rect.colliderect(ball.rect):`（壊れていなくて、ボールと重なっている）なら、次の4つを行う
    - `self.active = False` で、壊れた印にする
    - `ball.vy = -ball.vy` で、ボールを跳ね返す
    - `pg.mixer.Sound(SND_DIR / "piko.wav").play()` で、音を鳴らす
    - `return True` で、当たったことを知らせる
  - 当たっていなければ、`return False`

<details>
<summary>コードを見る</summary>

```python
    def draw(self):
        if self.active:
            pg.draw.rect(screen, pg.Color("GOLD"), self.rect)

    def check_hit(self, ball):
        if self.active and self.rect.colliderect(ball.rect):
            self.active  = False
            ball.vy = -ball.vy
            pg.mixer.Sound(SND_DIR / "piko.wav").play()
            return True
        return False
```

</details>

## ステップ13. make_blocks() 関数を書く

`Block` クラスの下に、2行空けて書く。ブロックの定数（`BLOCK_ROWS`・`BLOCK_COLS`・`BLOCK_START`・`BLOCK_SPACING`）を、ここに移して、ブロックを並べる処理を関数にする。

- 定数の4行を書く（元の定義は、消す）
- 2行空けて、`def make_blocks():` を定義する
- `result = []` で、空のリストを作る
- `for yy in range(BLOCK_ROWS):` と `for xx in range(BLOCK_COLS):` の2重のくり返しで、`result.append(Block(x座標, y座標))` と足す。座標は `BLOCK_START[0] + xx * BLOCK_SPACING[0]`、`BLOCK_START[1] + yy * BLOCK_SPACING[1]` で求める
- `return result` で、リストを返す

<details>
<summary>コードを見る</summary>

```python
BLOCK_ROWS    = 4
BLOCK_COLS    = 7
BLOCK_START   = (50, 40)
BLOCK_SPACING = (100, 50)


def make_blocks():
    result = []
    for yy in range(BLOCK_ROWS):
        for xx in range(BLOCK_COLS):
            result.append(Block(BLOCK_START[0] + xx * BLOCK_SPACING[0],
                                 BLOCK_START[1] + yy * BLOCK_SPACING[1]))
    return result
```

</details>

## ステップ14. ブロックのリストを make_blocks() で作る

データの部分を書き換える。

- `blocks = []` から始まる、ブロックを並べるくり返し（5行）は、消す
- `replay_img` の下に、`blocks = make_blocks()` を足す
- `gamestage()` の1行目を、`global page, score, blocks` に変える

`blocks` の作成:

<details>
<summary>コードを見る</summary>

```python
barrect    = pg.Rect(400, 500, *BAR_SIZE)
REPLAY_BTN_POS   = (320, 480)
RESULT_FONT_SIZE = 150
replay_img = pg.image.load(IMG_DIR / "replaybtn.png")
blocks     = make_blocks()
```

</details>

`global` の行:

<details>
<summary>コードを見る</summary>

```python
    global page, score, blocks
```

</details>

## ステップ15. gamestage() のブロックの処理を書き換える

ブロックの処理を、すべて消して、書き換える。

- `for block in blocks:` で、ブロックを順番に取り出す（`enumerate` は、不要になった）
- `block.draw()` で、描く
- `if block.check_hit(ball):`（当たった）なら、`score += 1` と、今までと同じクリアの判定（`score == BLOCK_ROWS * BLOCK_COLS` なら、音を鳴らして `page = 3`）

<details>
<summary>コードを見る</summary>

```python
    for block in blocks:
        block.draw()
        if block.check_hit(ball):
            score += 1
            if score == BLOCK_ROWS * BLOCK_COLS:
                pg.mixer.Sound(SND_DIR / "up.wav").play()
                page = 3
```

</details>

## ステップ16. gamereset() でブロックを作り直す

`gamereset()` のブロックを並べ直す部分（`blocks = []` から、くり返しの最後まで）を、消して、1行にする。

- `blocks = make_blocks()`

<details>
<summary>コードを見る</summary>

```python
def gamereset():
    global score, blocks
    ball.reset()
    score  = 0
    blocks = make_blocks()
```

</details>

ここまでで、`example/ex03.py` と同じ動きになる。壊れたブロックは `active = False` になって、描かれなくなる。

### 実行する

ターミナルで、リポジトリのルートから実行する（自分のファイルなら、ファイル名を置き換える）。

```bash
python 17_BreakoutClone_class_ver/example/ex03.py
```

---

# ex04 — Bar クラスを作る

バーも `Bar` クラスにして、`Ball` / `Block` / `Bar` の3クラス構成にする。あわせて、行ごとにブロックの色を変える（完成形は [example/ex04.py](example/ex04.py)）。

## ステップ17. Bar クラスを書く

バーもクラスにまとめて、`Ball`・`Block`・`Bar` の3クラスにする。`Block` クラスの下に、2行空けて書く。

- `class Bar():` を定義する
- `def __init__(self):` で、`self.rect = pg.Rect(400, 500, *BAR_SIZE)` と、バーの `Rect` を持つ
- `def update(self, mx):` で、`self.rect.x = mx - BAR_SIZE[0] // 2` と、マウスのX座標に合わせて動かす
- `def draw(self):` で、`pg.draw.rect(screen, pg.Color("CYAN"), self.rect)` と、描く

<details>
<summary>コードを見る</summary>

```python
class Bar():
    def __init__(self):
        self.rect = pg.Rect(400, 500, *BAR_SIZE)

    def update(self, mx):
        self.rect.x = mx - BAR_SIZE[0] // 2

    def draw(self):
        pg.draw.rect(screen, pg.Color("CYAN"), self.rect)
```

</details>

## ステップ18. barrect を bar に置き換える

データと `gamestage()` を書き換える。

- `barrect = pg.Rect(...)` の行を消して、`ball = Ball(ballimg)` の下に、`bar = Bar()` を足す
- `gamestage()` の `barrect.x = mx - BAR_SIZE[0] // 2` と `pg.draw.rect(..., barrect)` を、`bar.update(mx)` と `bar.draw()` に書き換える
- `ball.bounce_bar(barrect)` を、`ball.bounce_bar(bar)` に変える

`bar` の作成:

<details>
<summary>コードを見る</summary>

```python
ballimg    = pg.image.load(IMG_DIR / "kaeru.png")
ballimg    = pg.transform.scale(ballimg, (BALL_SIZE, BALL_SIZE))
ball       = Ball(ballimg)
bar        = Bar()
```

</details>

バーの処理:

<details>
<summary>コードを見る</summary>

```python
    bar.update(mx)
    bar.draw()
```

</details>

ボールの呼び出し:

<details>
<summary>コードを見る</summary>

```python
    ball.bounce_bar(bar)
```

</details>

## ステップ19. bounce_bar() が Bar を受け取るようにする

`Ball.bounce_bar()` を書き換える。バーそのものを受け取って、`bar.rect` を使う。

- 引数を `(self, bar)` に変える
- `barrect.colliderect(self.rect)` を、`bar.rect.colliderect(self.rect)` に変える
- `barrect.x` を、`bar.rect.x` に変える

<details>
<summary>コードを見る</summary>

```python
    def bounce_bar(self, bar):
        if bar.rect.colliderect(self.rect):
            self.vx = int(((self.rect.x + BALL_SIZE // 2) - (bar.rect.x + BAR_SIZE[0] // 2)) / 4)
            self.vy = random.randint(*BOUNCE_VY_RANGE)
            pg.mixer.Sound(SND_DIR / "pi.wav").play()

```

</details>

## ステップ20. Block に色を持たせる

行ごとにブロックの色を変える。

- `Block` の `__init__` の引数を `(self, x, y, color)` に変え、`self.color = color` を足す
- `draw()` の `pg.Color("GOLD")` を、`self.color` に変える
- `Block` の上に、`ROW_COLORS = ["RED", "ORANGE", "YELLOW", "GREEN"]` を足す（行ごとの色の名前）

`ROW_COLORS`:

<details>
<summary>コードを見る</summary>

```python
ROW_COLORS = ["RED", "ORANGE", "YELLOW", "GREEN"]
```

</details>

`Block`:

<details>
<summary>コードを見る</summary>

```python
class Block():
    def __init__(self, x, y, color):
        self.rect   = pg.Rect(x, y, *BLOCK_SIZE)
        self.color  = color
        self.active = True

    def draw(self):
        if self.active:
            pg.draw.rect(screen, self.color, self.rect)
```

</details>

## ステップ21. make_blocks() で行ごとの色を渡す

`make_blocks()` を書き換える。

- `for yy in range(BLOCK_ROWS):` の中の最初に、`color = pg.Color(ROW_COLORS[yy])` で、その行の色を求める
- `Block(...)` の最後の引数に、`color` を足す

<details>
<summary>コードを見る</summary>

```python
def make_blocks():
    result = []
    for yy in range(BLOCK_ROWS):
        color = pg.Color(ROW_COLORS[yy])
        for xx in range(BLOCK_COLS):
            result.append(Block(BLOCK_START[0] + xx * BLOCK_SPACING[0],
                                 BLOCK_START[1] + yy * BLOCK_SPACING[1], color))
    return result
```

</details>

ここまでで、`example/ex04.py` と同じ動きになる。ブロックは行ごとに色が変わり、3つのクラスで構成される。

### 実行する

ターミナルで、リポジトリのルートから実行する（自分のファイルなら、ファイル名を置き換える）。

```bash
python 17_BreakoutClone_class_ver/example/ex04.py
```

---

# ex05 — ボールを複数に増やす

`ball` 1個を `balls` リストに変えて、ブロックを一定数壊すごとにボールを増やす。何個になるか事前にはわからないので、`append()` していく形が自然に必要になる（完成形は [example/ex05.py](example/ex05.py)）。

## ステップ22. Ball の開始位置を引数にする

ここから、ボールを複数にする。

- `Ball.__init__` の引数を `(self, img, x)` に変える
- `self.rect = pg.Rect(x, 450, BALL_SIZE, BALL_SIZE)` に変える（開始位置を変えられるようにする）
- `reset()` は、もう使わないので消す（`gamereset()` で、ボールを作り直すため）

<details>
<summary>コードを見る</summary>

```python
class Ball():
    def __init__(self, img, x):
        self.img  = img
        self.rect = pg.Rect(x, 450, BALL_SIZE, BALL_SIZE)
        self.vx   = random.randint(*INITIAL_VX_RANGE)
        self.vy   = INITIAL_VY
```

</details>

## ステップ23. make_balls() 関数を書く

`make_blocks()` の下に、2行空けて書く。

- `BLOCK_COLS` の定数の下に、`BALL_SPAWN_INTERVAL = BLOCK_COLS` を足す（ブロックを7個壊すごとに、ボールが1個増える）
- `def make_balls():` を定義して、`return [Ball(ballimg, 400)]` と、ボールを1個だけ入れたリストを返す

`BALL_SPAWN_INTERVAL`:

<details>
<summary>コードを見る</summary>

```python
BALL_SPAWN_INTERVAL = BLOCK_COLS   # ブロックを7個壊すごとにボールが1個増える
```

</details>

`make_balls()`:

<details>
<summary>コードを見る</summary>

```python
def make_balls():
    # ── ex04 との違い: 最初は1個だけ。増える分は gamestage() で balls に追加する ──
    return [Ball(ballimg, 400)]
```

</details>

## ステップ24. ball を balls リストに置き換える

データと `gamestage()` の `global` を書き換える。

- `ball = Ball(ballimg)` を消して、`blocks = make_blocks()` の下に、`balls = make_balls()` を足す
- `gamestage()` の1行目を、`global page, score, blocks, balls` に変える

`balls` の作成:

<details>
<summary>コードを見る</summary>

```python
ballimg    = pg.image.load(IMG_DIR / "kaeru.png")
ballimg    = pg.transform.scale(ballimg, (BALL_SIZE, BALL_SIZE))
bar        = Bar()
REPLAY_BTN_POS   = (320, 480)
RESULT_FONT_SIZE = 150
replay_img = pg.image.load(IMG_DIR / "replaybtn.png")
blocks     = make_blocks()
balls      = make_balls()
```

</details>

`global` の行:

<details>
<summary>コードを見る</summary>

```python
    global page, score, blocks, balls
```

</details>

## ステップ25. 全ボールを動かして、画面外のボールを除く

`gamestage()` のボールの処理（`ball.bounce_wall()` から `ball.draw()` まで）を、すべて消して、書き換える。ボールは、途中で減るので、生き残ったボールだけを新しいリストに集める。

- `alive_balls = []` で、空のリストを作る
- `for ball in balls:` で、ボールを順番に取り出し、`ball.bounce_wall()`、`ball.bounce_bar(bar)`、`ball.move()`、`ball.draw()` を呼ぶ
- `if not ball.is_out():`（画面の中にいる）なら、`alive_balls.append(ball)`
- くり返しが終わったら、`balls = alive_balls` で、リストを置き換える
- `if len(balls) == 0:`（全部のボールが落ちた）なら、`page = 2` と、音を鳴らす

<details>
<summary>コードを見る</summary>

```python
    alive_balls = []
    for ball in balls:
        ball.bounce_wall()
        ball.bounce_bar(bar)
        ball.move()
        ball.draw()
        if not ball.is_out():
            alive_balls.append(ball)
    balls = alive_balls

    if len(balls) == 0:
        page = 2
        pg.mixer.Sound(SND_DIR / "pi.wav").play()
```

</details>

## ステップ26. ブロックを壊すたびに、ボールを増やす

ブロックの処理を書き換える。

- `for block in blocks:` の上に、`new_balls = []` を足す（増やすボールを、一旦ここに入れる）
- `block.draw()` の下に、`for ball in balls:` を足して、全ボールで当たり判定をする（`if block.check_hit(ball):` 以降は、1段深くなる）
- 当たったら、`score += 1` の下に、`if score % BALL_SPAWN_INTERVAL == 0 and score < BLOCK_ROWS * BLOCK_COLS:`（7個壊すごとで、最後のブロックではない）なら、`new_balls.append(Ball(ballimg, 400))`
- クリアの判定（`score == BLOCK_ROWS * BLOCK_COLS`）は、そのまま
- `for block` が終わったあと（`for` と同じ字下げ）に、`balls += new_balls` で、まとめて足す。`balls` を回している途中で、`balls` に足すと、同じフレームで、足したボールも判定されるので、`new_balls` に一旦分けている

<details>
<summary>コードを見る</summary>

```python
    new_balls = []
    for block in blocks:
        block.draw()
        for ball in balls:
            if block.check_hit(ball):
                score += 1
                if score % BALL_SPAWN_INTERVAL == 0 and score < BLOCK_ROWS * BLOCK_COLS:
                    new_balls.append(Ball(ballimg, 400))
                if score == BLOCK_ROWS * BLOCK_COLS:
                    pg.mixer.Sound(SND_DIR / "up.wav").play()
                    page = 3
    balls += new_balls
```

</details>

## ステップ27. gamereset() でボールを作り直す

`gamereset()` を変更する。

- 1行目を、`global score, blocks, balls` に変える
- `ball.reset()` の行は、消す
- `blocks = make_blocks()` の下に、`balls = make_balls()` を足す

<details>
<summary>コードを見る</summary>

```python
def gamereset():
    global score, blocks, balls
    score  = 0
    blocks = make_blocks()
    balls  = make_balls()
```

</details>

ここまでで、`example/ex05.py` と同じ、完成版の動きになる。ブロックを7個壊すごとにボールが増え、全部のボールが落ちるとゲームオーバーになる。

### 実行する

ターミナルで、リポジトリのルートから実行する（自分のファイルなら、ファイル名を置き換える）。

```bash
python 17_BreakoutClone_class_ver/example/ex05.py
```
