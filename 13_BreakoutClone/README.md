```text
バーでボールを打ち返し、ブロックを全て壊すブロック崩しゲームを作りましょう
ステップごとにコードを書き足して、動かしながら完成させよう
```

# 目次
- [出発点 — バーとボールを動かす](#出発点--バーとボールを動かす)
  - [ステップ1. ライブラリを読み込んで初期化する](#ステップ1-ライブラリを読み込んで初期化する)
  - [ステップ2. 画像と音のフォルダを決める](#ステップ2-画像と音のフォルダを決める)
  - [ステップ3. ウィンドウを作る](#ステップ3-ウィンドウを作る)
  - [ステップ4. バーのデータを作る](#ステップ4-バーのデータを作る)
  - [ステップ5. ボールのデータを作る](#ステップ5-ボールのデータを作る)
  - [ステップ6. gamestage() 関数を作る](#ステップ6-gamestage-関数を作る)
  - [ステップ7. バーを動かして描く](#ステップ7-バーを動かして描く)
  - [ステップ8. ボールを壁で跳ね返す](#ステップ8-ボールを壁で跳ね返す)
  - [ステップ9. ボールをバーで跳ね返す](#ステップ9-ボールをバーで跳ね返す)
  - [ステップ10. ボールを動かして描く](#ステップ10-ボールを動かして描く)
  - [ステップ11. メインループを作る](#ステップ11-メインループを作る)
- [ex02 — ゲームオーバーを作る](#ex02--ゲームオーバーを作る)
  - [ステップ12. ボタンとページの変数を作る](#ステップ12-ボタンとページの変数を作る)
  - [ステップ13. button_to_jump() 関数を作る](#ステップ13-button_to_jump-関数を作る)
  - [ステップ14. ボールが落ちたらゲームオーバーにする](#ステップ14-ボールが落ちたらゲームオーバーにする)
  - [ステップ15. gamereset() 関数を作る](#ステップ15-gamereset-関数を作る)
  - [ステップ16. gameover() 関数を作る](#ステップ16-gameover-関数を作る)
  - [ステップ17. メインループをページで分岐させる](#ステップ17-メインループをページで分岐させる)
- [ex03 — ブロックを並べる](#ex03--ブロックを並べる)
  - [ステップ18. ブロックのデータを作る](#ステップ18-ブロックのデータを作る)
  - [ステップ19. スコアの変数を作る](#ステップ19-スコアの変数を作る)
  - [ステップ20. ブロックを描いて、当たり判定をする](#ステップ20-ブロックを描いて当たり判定をする)
  - [ステップ21. gamereset() にスコアとブロックのリセットを足す](#ステップ21-gamereset-にスコアとブロックのリセットを足す)
  - [ステップ22. gameclear() 関数を作る](#ステップ22-gameclear-関数を作る)
  - [ステップ23. メインループにゲームクリアの分岐を足す](#ステップ23-メインループにゲームクリアの分岐を足す)

---

# 出発点 — バーとボールを動かす

マウスでバーを操作し、ボールを打ち返す。ステップごとにコードを書き足していく（完成形は [example/ex01.py](example/ex01.py)）。

## ステップ1. ライブラリを読み込んで初期化する

新しい `.py` ファイルの1行目から、次の順に書く。

- `from pathlib import Path` で、パスを扱う `Path` を読み込む
- `import pygame as pg`、`import sys`、`import random` で、ライブラリを読み込む（`sys` は終了に、`random` はボールの速さをランダムに決めるのに使う）
- 1行空けて、`pg.init()` で、pygame を初期化する

<details>
<summary>コードを見る</summary>

```python
from pathlib import Path
import pygame as pg
import sys
import random

pg.init()
```

</details>


## ステップ2. 画像と音のフォルダを決める

`pg.init()` の下に、3つのフォルダを変数にする。`pathlib` の使い方は [08_pathlib_module](../08_pathlib_module/README.md) を参照。

- `BASE_DIR = Path(__file__).resolve().parent.parent` で、このファイルの1つ上のフォルダ（`13_BreakoutClone`）を求める
- `IMG_DIR = BASE_DIR / "images"` で、画像のフォルダにする
- `SND_DIR = BASE_DIR / "sounds"` で、音のフォルダにする

<details>
<summary>コードを見る</summary>

```python
BASE_DIR = Path(__file__).resolve().parent.parent
IMG_DIR  = BASE_DIR / "images"
SND_DIR  = BASE_DIR / "sounds"
```

</details>


## ステップ3. ウィンドウを作る

フォルダの設定の下に、画面の設定を書く。

- `WIDTH, HEIGHT = 800, 600` で、ウィンドウの幅と高さを決める
- `FPS = 60` で、1秒間に更新する回数を決める
- `screen = pg.display.set_mode((WIDTH, HEIGHT))` で、ウィンドウを作る（幅と高さを `(幅, 高さ)` の形で、1つ渡す）
- `pg.display.set_caption("BreakoutClone")` で、タイトルバーの文字を設定する
- `clock = pg.time.Clock()` で、FPSを管理する `clock` を作る

<details>
<summary>コードを見る</summary>

```python
WIDTH, HEIGHT = 800, 600

FPS = 60

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("BreakoutClone")
clock = pg.time.Clock()
```

</details>


## ステップ4. バーのデータを作る

ウィンドウの下に、ゲームで使うデータを書いていく（`# データ` というコメントで区切る）。まず、バーのデータ。

- `BAR_SIZE = (100, 20)` で、バーの大きさ（幅100、高さ20）を決める
- `barrect = pg.Rect(400, 500, *BAR_SIZE)` で、バーの位置と大きさを `Rect` にする（`*BAR_SIZE` は、タプルを幅と高さの2つの引数に展開する）

<details>
<summary>コードを見る</summary>

```python
# データ
## バーデータ
BAR_SIZE = (100, 20)
barrect = pg.Rect(400, 500, *BAR_SIZE)
```

</details>


## ステップ5. ボールのデータを作る

バーのデータの下に、ボールのデータを書く。

- `BALL_SIZE = 30` で、ボールの大きさ（1辺30）を決める
- `INITIAL_VX_RANGE = (-10, 10)` と `INITIAL_VY = -5` で、最初の速さを決める。`vy` がマイナスなのは、上向きに進むため
- `BOUNCE_VY_RANGE = (-10, -5)` で、バーで跳ね返ったあとの、上向きの速さの範囲を決める
- `ballimg` に `kaeru.png` を読み込み、`pg.transform.scale()` で `BALL_SIZE` の大きさに縮小する（→ [04_draw_images](../04_draw_images/README.md)）
- `ballrect = pg.Rect(400, 450, BALL_SIZE, BALL_SIZE)` で、ボールの位置と大きさを `Rect` にする
- `vx = random.randint(*INITIAL_VX_RANGE)` で、左右の速さをランダムに決める
- `vy = INITIAL_VY` で、上下の速さを決める

<details>
<summary>コードを見る</summary>

```python

## ボールデータ
BALL_SIZE = 30
INITIAL_VX_RANGE = (-10, 10)
INITIAL_VY = -5
BOUNCE_VY_RANGE = (-10, -5)
ballimg = pg.image.load(IMG_DIR / "kaeru.png")
ballimg = pg.transform.scale(ballimg, (BALL_SIZE, BALL_SIZE))
ballrect = pg.Rect(400, 450, BALL_SIZE, BALL_SIZE)
vx = random.randint(*INITIAL_VX_RANGE)
vy = INITIAL_VY
```

</details>


## ステップ6. gamestage() 関数を作る

ゲーム中の処理を、`gamestage()` 関数にまとめる。データの下に書く。

- `def gamestage():` で、引数のない関数を定義する
- 関数の中の1行目に、`global vx, vy` を書く（関数の中で、外の変数 `vx`・`vy` を書き換えるために必要。→ [06_function](../06_function/README.md) の「グローバル変数」）
- `screen.fill(pg.Color("NAVY"))` で、背景を紺色で塗りつぶす
- `(mx, my) = pg.mouse.get_pos()` で、マウスの座標を取得する

<details>
<summary>コードを見る</summary>

```python
## ゲームステージ
def gamestage():
    global vx, vy
    screen.fill(pg.Color("NAVY"))

    (mx, my) = pg.mouse.get_pos()
```

</details>


## ステップ7. バーを動かして描く

`gamestage()` の中の、マウスの座標を取得した下に書く。

- `barrect.x = mx - BAR_SIZE[0] // 2` で、バーの左端の位置を決める（バーの中心をマウスに合わせるため、バーの幅の半分を引く）
- `pg.draw.rect(screen, pg.Color("CYAN"), barrect)` で、シアンのバーを描く

<details>
<summary>コードを見る</summary>

```python

    ## バーの処理
    barrect.x = mx - BAR_SIZE[0] // 2
    pg.draw.rect(screen, pg.Color("CYAN"), barrect)
```

</details>


## ステップ8. ボールを壁で跳ね返す

バーの処理の下に、壁との判定を書く。跳ね返るときは、速さの向きを反対（`-1` を掛ける）にする。

- `if ballrect.y < 0:` （上の壁に当たった）なら、`vy = -vy`
- `if ballrect.x < 0 or ballrect.x > WIDTH - BALL_SIZE:` （左か右の壁に当たった）なら、`vx = -vx`
  - 右の壁は、ボールの左端 `x` で調べるので、ボールの大きさ `BALL_SIZE` を引く
- 下の壁には跳ね返らない（落ちたらゲームオーバーにするため）

<details>
<summary>コードを見る</summary>

```python

    ## ボールの処理
    if ballrect.y < 0:
        vy = -vy
    if ballrect.x < 0 or ballrect.x > WIDTH - BALL_SIZE:
        vx = -vx
```

</details>


## ステップ9. ボールをバーで跳ね返す

壁の判定の下に、バーとの判定を書く。

- `if barrect.colliderect(ballrect):` （ボールがバーに当たった）のとき、次の3つを行う（→ [09_actiongame](../09_actiongame/README.md) の「衝突判定」）
  - `vx = int(((ballrect.x + BALL_SIZE // 2) - (barrect.x + BAR_SIZE[0] // 2)) / 4)` で、左右の速さを決める。ボールの中心とバーの中心の差を4で割るので、バーの端で打つほど、横に大きく跳ねる
  - `vy = random.randint(*BOUNCE_VY_RANGE)` で、上向きの速さをランダムに決める
  - `pg.mixer.Sound(SND_DIR / "pi.wav").play()` で、音を鳴らす

<details>
<summary>コードを見る</summary>

```python
    if barrect.colliderect(ballrect):
        vx = int(((ballrect.x + BALL_SIZE // 2) - (barrect.x + BAR_SIZE[0] // 2)) / 4)
        vy = random.randint(*BOUNCE_VY_RANGE)
        pg.mixer.Sound(SND_DIR / "pi.wav").play()
```

</details>


## ステップ10. ボールを動かして描く

`gamestage()` の最後に書く。

- `ballrect.x += vx`、`ballrect.y += vy` で、ボールを速さの分だけ動かす
- `screen.blit(ballimg, ballrect)` で、ボールの画像を `ballrect` の位置に描く

<details>
<summary>コードを見る</summary>

```python
    ballrect.x += vx
    ballrect.y += vy
    screen.blit(ballimg, ballrect)
```

</details>


## ステップ11. メインループを作る

関数の外（字下げなし）の、一番下に書く。

- `# ループ` の下で、`while True:` のくり返しを作る
- ループの中の最初に、`for event in pg.event.get():` でイベントを調べ、`event.type == pg.QUIT`（閉じるボタン）なら、`pg.quit()` と `sys.exit()` で終了する
- 空行をはさんで、`gamestage()` を呼び出す
- `pg.display.update()` で、画面を更新する
- `clock.tick(FPS)` で、FPSを一定にする

<details>
<summary>コードを見る</summary>

```python

# ループ
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    gamestage()
    pg.display.update()
    clock.tick(FPS)
```

</details>

ここまでで、`example/ex01.py` と同じ動きになる。マウスでバーを動かして、ボールを打ち返せる。画面の下に落ちたボールは、そのまま消えていく。


### 実行する

ターミナルで、リポジトリのルートから実行する（自分のファイルなら、ファイル名を置き換える）。

```bash
python 13_BreakoutClone/example/ex01.py
```

---

# ex02 — ゲームオーバーを作る

ボールが画面下に出たら、ゲームオーバー画面に切り替える。リプレイボタンでリセットして、再プレイできる（完成形は [example/ex02.py](example/ex02.py)）。

## ステップ12. ボタンとページの変数を作る

ゲームオーバー画面を作る準備として、リプレイボタンの変数と、画面を切り替えるための変数を書く。ボールのデータの下に書く（→ [07_switch_screen](../07_switch_screen/README.md)）。

- `REPLAY_BTN_POS = (320, 480)` で、リプレイボタンの位置を決める
- `RESULT_FONT_SIZE = 150` で、結果の文字の大きさを決める
- `replay_img` に、`replaybtn.png` を読み込む
- `pushFlag = False` で、ボタンを押したか（1回だけ反応させるためのフラグ）を覚える
- `page = 1` で、今のページを覚える（`1`: ゲーム中、`2`: ゲームオーバー）

<details>
<summary>コードを見る</summary>

```python

## ボタンデータ
REPLAY_BTN_POS   = (320, 480)
RESULT_FONT_SIZE = 150
replay_img = pg.image.load(IMG_DIR / "replaybtn.png")

## メインループで使う変数
pushFlag = False
page = 1
```

</details>


## ステップ13. button_to_jump() 関数を作る

ボタンを押したら、別のページに切り替える関数を作る。`gamestage()` の前に書く。考え方は、[07_switch_screen](../07_switch_screen/README.md) の `button_to_jump()` と同じ。

- `def button_to_jump(btn, newpage):` で、ボタンの `Rect` と、移動先のページ番号を受け取る
- 関数の中の1行目に、`global page, pushFlag` を書く
- `mdown = pg.mouse.get_pressed()` と `(mx, my) = pg.mouse.get_pos()` で、マウスの状態と座標を調べる
- `mdown[0]`（左ボタンが押されている）のとき
  - `btn.collidepoint(mx, my) and not pushFlag`（ボタンの上で、まだ押していない）なら、音を鳴らして `page = newpage`、`pushFlag = True`
- 左ボタンが押されていなければ（`else:`）、`pushFlag = False` に戻す

<details>
<summary>コードを見る</summary>

```python

## btnを押したら、newpageにジャンプする
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
```

</details>


## ステップ14. ボールが落ちたらゲームオーバーにする

`gamestage()` を変更する。

- 関数の1行目を、`global vx, vy, page` に変える（`page` を書き換えるため）
- ボールを動かす前（バーとの判定の下）に、`if ballrect.y > HEIGHT:`（ボールが画面の下に出た）を書く
  - `page = 2` で、ゲームオーバーのページに切り替える
  - `pg.mixer.Sound(SND_DIR / "down.wav").play()` で、音を鳴らす

`global` の行:

<details>
<summary>コードを見る</summary>

```python
def gamestage():
    global vx, vy, page
```

</details>

ボールの処理の中:

<details>
<summary>コードを見る</summary>

```python
    if ballrect.y > HEIGHT:
        page = 2
        pg.mixer.Sound(SND_DIR / "down.wav").play()
```

</details>


## ステップ15. gamereset() 関数を作る

ゲームを最初の状態に戻す関数を作る。`gamestage()` の下に書く。

- `def gamereset():` で、引数のない関数を定義する
- 関数の中の1行目に、`global vx, vy` を書く
- `vx` を、また `random.randint(*INITIAL_VX_RANGE)` で決め、`vy` を `INITIAL_VY` に戻す
- `ballrect.x = 400`、`ballrect.y = 450` で、ボールを最初の位置に戻す

<details>
<summary>コードを見る</summary>

```python

## データのリセット
def gamereset():
    global vx, vy
    vx = random.randint(*INITIAL_VX_RANGE)
    vy = INITIAL_VY
    ballrect.x = 400
    ballrect.y = 450
```

</details>


## ステップ16. gameover() 関数を作る

ゲームオーバー画面を描く関数を作る。`gamereset()` の下に書く。

- `def gameover():` で、引数のない関数を定義する
- 最初に `gamereset()` を呼んで、データをリセットしておく（リプレイボタンを押したら、すぐ始められる）
- `screen.fill(pg.Color("NAVY"))` で、背景を塗りつぶす
- `font = pg.font.Font(None, RESULT_FONT_SIZE)` で、フォントを作る
- `text = font.render("GAMEOVER", True, pg.Color("RED"))` で、赤い文字の画像を作り、`screen.blit(text, (100, 200))` で貼り付ける
- `btn1 = screen.blit(replay_img, REPLAY_BTN_POS)` で、リプレイボタンを描いて、その範囲を `btn1` に受け取る
- `button_to_jump(btn1, 1)` で、ボタンを押したらページ1（ゲーム中）に戻す

<details>
<summary>コードを見る</summary>

```python

## ゲームオーバー
def gameover():
    gamereset()
    screen.fill(pg.Color("NAVY"))
    font = pg.font.Font(None, RESULT_FONT_SIZE)
    text = font.render("GAMEOVER", True, pg.Color("RED"))
    screen.blit(text, (100, 200))
    btn1 = screen.blit(replay_img, REPLAY_BTN_POS)
    button_to_jump(btn1, 1)
```

</details>


## ステップ17. メインループをページで分岐させる

メインループの中の `gamestage()` の呼び出しを、`page` の値で分けるように書き換える。

- `if page == 1:` なら `gamestage()`
- `elif page == 2:` なら `gameover()`

<details>
<summary>コードを見る</summary>

```python
    if page == 1:
        gamestage()
    elif page == 2:
        gameover()
```

</details>

ここまでで、`example/ex02.py` と同じ動きになる。ボールを落とすとゲームオーバー画面になり、リプレイボタンで最初からやり直せる。


### 実行する

ターミナルで、リポジトリのルートから実行する（自分のファイルなら、ファイル名を置き換える）。

```bash
python 13_BreakoutClone/example/ex02.py
```

---

# ex03 — ブロックを並べる

二重ループでブロックを4行×7列 = 28個並べる。ボールが当たったブロックを消してスコアを増やし、全部消したらゲームクリアにする（完成形は [example/ex03.py](example/ex03.py)）。

## ステップ18. ブロックのデータを作る

ブロックの大きさや並べ方を決めて、二重のくり返しで `Rect` を28個作る。ボタンのデータの下に書く。

- `BLOCK_ROWS = 4`、`BLOCK_COLS = 7` で、行数と列数を決める
- `BLOCK_START = (50, 40)` で、左上のブロックの位置を決める
- `BLOCK_SPACING = (100, 50)` で、ブロックの間隔（横・縦）を決める
- `BLOCK_SIZE = (80, 30)` で、ブロック1つの大きさを決める
- `blocks = []` で、空のリストを作る
- `for yy in range(BLOCK_ROWS):` の中に、`for xx in range(BLOCK_COLS):` を書く
  - 一番内側で、`blocks.append(pg.Rect(x, y, *BLOCK_SIZE))` を書く
  - `x` は `BLOCK_START[0] + xx * BLOCK_SPACING[0]`、`y` は `BLOCK_START[1] + yy * BLOCK_SPACING[1]`

<details>
<summary>コードを見る</summary>

```python

## ブロックデータ
BLOCK_ROWS    = 4
BLOCK_COLS    = 7
BLOCK_START   = (50, 40)
BLOCK_SPACING = (100, 50)
BLOCK_SIZE    = (80, 30)
blocks = []
for yy in range(BLOCK_ROWS):
    for xx in range(BLOCK_COLS):
        blocks.append(pg.Rect(BLOCK_START[0] + xx * BLOCK_SPACING[0],
                               BLOCK_START[1] + yy * BLOCK_SPACING[1], *BLOCK_SIZE))
```

</details>


## ステップ19. スコアの変数を作る

壊したブロックの数を数える `score` を作る。`page = 1` の下に書く。さらに、`gamestage()` の1行目を、`score` も書き換えられるように変える。

- `score = 0` で、スコアを `0` にしておく
- `gamestage()` の `global` の行を、`global vx, vy, page, score` に変える

メインループで使う変数:

<details>
<summary>コードを見る</summary>

```python
page = 1
score = 0
```

</details>

`global` の行:

<details>
<summary>コードを見る</summary>

```python
def gamestage():
    global vx, vy, page, score
```

</details>


## ステップ20. ブロックを描いて、当たり判定をする

`gamestage()` の最後（ボールを描いたあと）に書く。`enumerate()` で、番号 `n` と、ブロック `block` を一緒に取り出す。

- `for n, block in enumerate(blocks):` で、全ブロックを1つずつ調べる
- ブロックを `pg.Color("GOLD")` で描く
- `block.colliderect(ballrect)`（ボールが当たった）なら、次の5つを行う
  - `piko.wav` の音を鳴らす
  - `vy = -vy` で、ボールを跳ね返す
  - `blocks[n] = pg.Rect(0, 0, 0, 0)` で、そのブロックを、大きさ `0` の `Rect` に置き換えて、消す（リストの要素の数は変えない）
  - `score += 1` で、スコアを増やす
  - `score == BLOCK_ROWS * BLOCK_COLS`（全部壊した）なら、`up.wav` の音を鳴らして、`page = 3`（ゲームクリア）にする

<details>
<summary>コードを見る</summary>

```python

    ## ブロックの処理
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
```

</details>


## ステップ21. gamereset() にスコアとブロックのリセットを足す

`gamereset()` を変更する。

- `global` の行を、`global vx, vy, score, blocks` に変える（`score` と `blocks` も書き換えるため）
- 関数の最後に、`score = 0` と `blocks = []` を足す
- 続けて、ブロックを並べ直す二重の `for` を、ステップ18と同じように書く（`blocks.append(...)` の部分も同じ）

<details>
<summary>コードを見る</summary>

```python
def gamereset():
    global vx, vy, score, blocks
    vx = random.randint(*INITIAL_VX_RANGE)
    vy = INITIAL_VY
    ballrect.x = 400
    ballrect.y = 450
    score = 0
    blocks = []
    for yy in range(BLOCK_ROWS):
        for xx in range(BLOCK_COLS):
            blocks.append(pg.Rect(BLOCK_START[0] + xx * BLOCK_SPACING[0],
                                   BLOCK_START[1] + yy * BLOCK_SPACING[1], *BLOCK_SIZE))
```

</details>


## ステップ22. gameclear() 関数を作る

ゲームクリア画面の関数を作る。`gameover()` の下に書く。`gameover()` とほぼ同じで、違うのは次の3点。

- 背景を `pg.Color("GOLD")`（金色）で塗りつぶす
- 文字を `"GAMECLEAR"` にして、貼り付ける位置を `(60, 200)` にする
- それ以外（`gamereset()` を呼ぶ、赤い文字、リプレイボタン、`button_to_jump(btn1, 1)`）は、`gameover()` と同じ

<details>
<summary>コードを見る</summary>

```python

## ゲームクリア
def gameclear():
    gamereset()
    screen.fill(pg.Color("GOLD"))
    font = pg.font.Font(None, RESULT_FONT_SIZE)
    text = font.render("GAMECLEAR", True, pg.Color("RED"))
    screen.blit(text, (60, 200))
    btn1 = screen.blit(replay_img, REPLAY_BTN_POS)
    button_to_jump(btn1, 1)
```

</details>


## ステップ23. メインループにゲームクリアの分岐を足す

メインループの `if page == 1:` の分岐に、`elif page == 3:` を足して、`gameclear()` を呼ぶ。

<details>
<summary>コードを見る</summary>

```python
    elif page == 3:
        gameclear()
```

</details>

ここまでで、`example/ex03.py` と同じ、完成版の動きになる。ブロックを全部壊すとゲームクリア画面になる。


### 実行する

ターミナルで、リポジトリのルートから実行する（自分のファイルなら、ファイル名を置き換える）。

```bash
python 13_BreakoutClone/example/ex03.py
```
