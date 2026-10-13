```text
マウスで自機を操作し、弾を撃ってUFOを倒すシューティングゲームを作りましょう
ステップごとにコードを書き足して、動かしながら完成させよう
```

# 目次
- [出発点 — 自機と弾を動かす](#出発点--自機と弾を動かす)
  - [ステップ1. ライブラリを読み込んで初期化する](#ステップ1-ライブラリを読み込んで初期化する)
  - [ステップ2. 画像と音のフォルダを決める](#ステップ2-画像と音のフォルダを決める)
  - [ステップ3. ウィンドウを作る](#ステップ3-ウィンドウを作る)
  - [ステップ4. 自機のデータを作る](#ステップ4-自機のデータを作る)
  - [ステップ5. 弾のデータを作る](#ステップ5-弾のデータを作る)
  - [ステップ6. gamestage() 関数を作る](#ステップ6-gamestage-関数を作る)
  - [ステップ7. 自機を動かして描く](#ステップ7-自機を動かして描く)
  - [ステップ8. 弾を発射する](#ステップ8-弾を発射する)
  - [ステップ9. 弾を飛ばして描く](#ステップ9-弾を飛ばして描く)
  - [ステップ10. メインループを作る](#ステップ10-メインループを作る)
- [ex02 — UFOを降らせる](#ex02--ufoを降らせる)
  - [ステップ11. UFOのデータを作る](#ステップ11-ufoのデータを作る)
  - [ステップ12. UFOを動かして描く](#ステップ12-ufoを動かして描く)
  - [ステップ13. 画面の下に出たら、上に戻す](#ステップ13-画面の下に出たら上に戻す)
- [ex03 — ゲームオーバーを作る](#ex03--ゲームオーバーを作る)
  - [ステップ14. ボタンとページの変数を作る](#ステップ14-ボタンとページの変数を作る)
  - [ステップ15. button_to_jump() 関数を作る](#ステップ15-button_to_jump-関数を作る)
  - [ステップ16. 自機とUFOが衝突したらゲームオーバーにする](#ステップ16-自機とufoが衝突したらゲームオーバーにする)
  - [ステップ17. gamereset() 関数を作る](#ステップ17-gamereset-関数を作る)
  - [ステップ18. gameover() 関数を作る](#ステップ18-gameover-関数を作る)
  - [ステップ19. メインループをページで分岐させる](#ステップ19-メインループをページで分岐させる)
- [ex04 — 弾でUFOを撃ち落とす](#ex04--弾でufoを撃ち落とす)
  - [ステップ20. 弾とUFOが衝突したら、UFOを撃ち落とす](#ステップ20-弾とufoが衝突したらufoを撃ち落とす)
- [ex05 — スコアを追加する](#ex05--スコアを追加する)
  - [ステップ21. スコアの変数を作る](#ステップ21-スコアの変数を作る)
  - [ステップ22. 撃ち落としたら、スコアを増やす](#ステップ22-撃ち落としたらスコアを増やす)
  - [ステップ23. スコアを描く](#ステップ23-スコアを描く)
  - [ステップ24. gamereset() でスコアをリセットする](#ステップ24-gamereset-でスコアをリセットする)
  - [ステップ25. ゲームオーバー画面にスコアを描く](#ステップ25-ゲームオーバー画面にスコアを描く)
  - [ステップ26. gameover() の gamereset() を条件付きにする](#ステップ26-gameover-の-gamereset-を条件付きにする)

---

# 出発点 — 自機と弾を動かす

マウスで自機を操作し、左クリックで弾を発射する。弾は1発だけ飛ばせる。ステップごとにコードを書き足していく（完成形は [example/ex01.py](example/ex01.py)）。

## ステップ1. ライブラリを読み込んで初期化する

新しい `.py` ファイルの1行目から、次の順に書く。

- `from pathlib import Path` で、パスを扱う `Path` を読み込む
- `import pygame as pg`、`import sys`、`import random` で、ライブラリを読み込む（`sys` は終了に、`random` はUFOの位置をランダムに決めるのに使う）
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

- `BASE_DIR = Path(__file__).resolve().parent.parent` で、このファイルの1つ上のフォルダ（`14_shooting_game`）を求める
- `IMG_DIR = BASE_DIR / "images"` で、画像のフォルダにする
- `SOUND_DIR = BASE_DIR / "sounds"` で、音のフォルダにする

<details>
<summary>コードを見る</summary>

```python
BASE_DIR  = Path(__file__).resolve().parent.parent
IMG_DIR   = BASE_DIR / "images"
SOUND_DIR = BASE_DIR / "sounds"
```

</details>


## ステップ3. ウィンドウを作る

フォルダの設定の下に、画面の設定を書く。

- `WIDTH, HEIGHT = 800, 600` で、ウィンドウの幅と高さを決める
- `FPS = 60` で、1秒間に更新する回数を決める
- `screen = pg.display.set_mode((WIDTH, HEIGHT))` で、ウィンドウを作る（幅と高さを `(幅, 高さ)` の形で、1つ渡す）
- `pg.display.set_caption("シューティングゲーム")` で、タイトルバーの文字を設定する
- `clock = pg.time.Clock()` で、FPSを管理する `clock` を作る

<details>
<summary>コードを見る</summary>

```python
WIDTH, HEIGHT = 800, 600

FPS = 60

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("シューティングゲーム")
clock = pg.time.Clock()
```

</details>


## ステップ4. 自機のデータを作る

ウィンドウの下に、ゲームで使うデータを書いていく（`# データ` というコメントで区切る）。まず、自機のデータ。

- `SHIP_SIZE = 50` で、自機の大きさ（1辺50）を決める
- `myimg` に `myship.png` を読み込み、`pg.transform.scale()` で `SHIP_SIZE` の大きさに縮小する（→ [04_draw_images](../04_draw_images/README.md)）
- `myrect = pg.Rect(400, 500, SHIP_SIZE, SHIP_SIZE)` で、自機の位置（画面の下のほう）と大きさを `Rect` にする

<details>
<summary>コードを見る</summary>

```python

# データ
## 自機データ
SHIP_SIZE = 50
myimg = pg.image.load(IMG_DIR / "myship.png")
myimg = pg.transform.scale(myimg, (SHIP_SIZE, SHIP_SIZE))
myrect = pg.Rect(400, 500, SHIP_SIZE, SHIP_SIZE)
```

</details>


## ステップ5. 弾のデータを作る

自機のデータの下に、弾のデータを書く。弾が飛んでいないときは、画面の外（上）に待機させておく。

- `BULLET_SIZE = 16` で、弾の大きさを決める
- `BULLET_SPEED = 15` で、1フレームに進むピクセル数を決める
- `OFFSCREEN_Y = -100` で、画面の外（上）のY座標を決める。弾が待機している位置になる
- `bulletimg` に `bullet.png` を読み込み、`BULLET_SIZE` の大きさに縮小する
- `bulletrect = pg.Rect(400, OFFSCREEN_Y, BULLET_SIZE, BULLET_SIZE)` で、待機している弾の `Rect` を作る

<details>
<summary>コードを見る</summary>

```python

## 弾データ
BULLET_SIZE  = 16
BULLET_SPEED = 15
OFFSCREEN_Y  = -100
bulletimg = pg.image.load(IMG_DIR / "bullet.png")
bulletimg = pg.transform.scale(bulletimg, (BULLET_SIZE, BULLET_SIZE))
bulletrect = pg.Rect(400, OFFSCREEN_Y, BULLET_SIZE, BULLET_SIZE)
```

</details>


## ステップ6. gamestage() 関数を作る

ゲーム中の処理を、`gamestage()` 関数にまとめる。データの下に書く。

- `def gamestage():` で、引数のない関数を定義する
- `screen.fill(pg.Color("NAVY"))` で、背景を紺色で塗りつぶす
- `(mx, _) = pg.mouse.get_pos()` で、マウスのX座標だけを取り出す（Y座標は使わないので、`_` で受ける）
- `mdown = pg.mouse.get_pressed()` で、マウスボタンの状態を調べる

<details>
<summary>コードを見る</summary>

```python

## ゲームステージ
def gamestage():
    screen.fill(pg.Color("NAVY"))
    (mx, _) = pg.mouse.get_pos()
    mdown = pg.mouse.get_pressed()
```

</details>


## ステップ7. 自機を動かして描く

`gamestage()` の中の、`mdown` の下に書く。

- `myrect.x = mx - SHIP_SIZE // 2` で、自機の左端の位置を決める（自機の中心をマウスに合わせるため、自機の幅の半分を引く）
- `screen.blit(myimg, myrect)` で、自機の画像を `myrect` の位置に描く

<details>
<summary>コードを見る</summary>

```python

    ## 自機の処理
    myrect.x = mx - SHIP_SIZE // 2
    screen.blit(myimg, myrect)
```

</details>


## ステップ8. 弾を発射する

自機の処理の下に書く。左ボタンを押したとき、待機している弾を、自機の位置に移して発射する。

- `if mdown[0] and bulletrect.y < 0:`（左ボタンが押されていて、弾が待機中＝画面の外にある）のとき、次の3つを行う
  - `bulletrect.x = myrect.x + SHIP_SIZE // 2 - BULLET_SIZE // 2` で、弾を自機の中心から出す（自機の中心のX座標から、弾の幅の半分を引く）
  - `bulletrect.y = myrect.y` で、弾を自機と同じ高さに置く
  - `pg.mixer.Sound(SOUND_DIR / "pi.wav").play()` で、発射の音を鳴らす
- 弾が飛んでいる間は、`bulletrect.y` が `0` 以上なので、次の弾は撃てない（弾は1発だけ）

<details>
<summary>コードを見る</summary>

```python

    ## 弾の処理
    if mdown[0] and bulletrect.y < 0:
        bulletrect.x = myrect.x + SHIP_SIZE // 2 - BULLET_SIZE // 2
        bulletrect.y = myrect.y
        pg.mixer.Sound(SOUND_DIR / "pi.wav").play()
```

</details>


## ステップ9. 弾を飛ばして描く

弾を発射する処理の下に書く。

- `if bulletrect.y >= 0:`（弾が飛んでいる）のあいだ、次の2つを行う
  - `bulletrect.y -= BULLET_SPEED` で、毎フレーム、上へ進める
  - `screen.blit(bulletimg, bulletrect)` で、弾を描く
- 弾が画面の上に出ると、`bulletrect.y` が `0` より小さくなり、また待機中に戻る（次の弾を撃てる）

<details>
<summary>コードを見る</summary>

```python
    if bulletrect.y >= 0:
        bulletrect.y -= BULLET_SPEED
        screen.blit(bulletimg, bulletrect)
```

</details>


## ステップ10. メインループを作る

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

ここまでで、`example/ex01.py` と同じ動きになる。マウスで自機を動かして、左クリックで弾を発射できる。


### 実行する

ターミナルで、リポジトリのルートから実行する（自分のファイルなら、ファイル名を置き換える）。

```bash
python 14_shooting_game/example/ex01.py
```

---

# ex02 — UFOを降らせる

UFOを10体リストで管理して、上から次々と降らせる（完成形は [example/ex02.py](example/ex02.py)）。

## ステップ11. UFOのデータを作る

UFOを10体、リストで管理する。弾のデータの下に書く。

- `UFO_SIZE = 50`、`UFO_COUNT = 10`、`UFO_SPEED = 10` で、大きさ・数・落ちる速さを決める
- `ufoimg` に `UFO.png` を読み込み、`UFO_SIZE` の大きさに縮小する
- `ufos = []` で、空のリストを作る
- `for i in range(UFO_COUNT):` で、`UFO_COUNT` 回くり返し、次のようにUFOを作ってリストに足す
  - `ux = random.randint(0, WIDTH)` で、X座標をランダムに決める
  - `uy = OFFSCREEN_Y * i` で、Y座標を決める。`i` が大きいほど上の高い位置になるので、10体が一度に出ず、順番に降ってくる
  - `ufos.append(pg.Rect(ux, uy, UFO_SIZE, UFO_SIZE))` で、リストに足す

<details>
<summary>コードを見る</summary>

```python

## UFOデータ
UFO_SIZE  = 50
UFO_COUNT = 10
UFO_SPEED = 10
ufoimg = pg.image.load(IMG_DIR / "UFO.png")
ufoimg = pg.transform.scale(ufoimg, (UFO_SIZE, UFO_SIZE))
ufos = []
for i in range(UFO_COUNT):
    ux = random.randint(0, WIDTH)
    uy = OFFSCREEN_Y * i
    ufos.append(pg.Rect(ux, uy, UFO_SIZE, UFO_SIZE))
```

</details>


## ステップ12. UFOを動かして描く

`gamestage()` の中の、弾の処理の下に書く。

- `for ufo in ufos:` で、UFOを1体ずつ取り出す
- `ufo.y += UFO_SPEED` で、毎フレーム、下へ進める
- `screen.blit(ufoimg, ufo)` で、UFOを描く

<details>
<summary>コードを見る</summary>

```python

    ## UFOの処理
    for ufo in ufos:
        ufo.y += UFO_SPEED
        screen.blit(ufoimg, ufo)
```

</details>


## ステップ13. 画面の下に出たら、上に戻す

`for ufo in ufos:` の中の、`screen.blit(...)` の下に書く。

- `if ufo.y > HEIGHT:`（UFOが画面の下に出た）のとき、次の2つを行う
  - `ufo.x = random.randint(0, WIDTH)` で、X座標を決め直す
  - `ufo.y = OFFSCREEN_Y` で、画面の外（上）に戻す。こうすると、UFOが何度も降ってくる

<details>
<summary>コードを見る</summary>

```python
        if ufo.y > HEIGHT:
            ufo.x = random.randint(0, WIDTH)
            ufo.y = OFFSCREEN_Y
```

</details>

ここまでで、`example/ex02.py` と同じ動きになる。UFOが次々と降ってくる（まだ、自機や弾に当たっても何も起きない）。


### 実行する

ターミナルで、リポジトリのルートから実行する（自分のファイルなら、ファイル名を置き換える）。

```bash
python 14_shooting_game/example/ex02.py
```

---

# ex03 — ゲームオーバーを作る

自機とUFOが衝突したらゲームオーバー画面に切り替える。リプレイボタンでリセットして再プレイできる（完成形は [example/ex03.py](example/ex03.py)）。

## ステップ14. ボタンとページの変数を作る

ゲームオーバー画面を作る準備として、リプレイボタンの変数と、画面を切り替えるための変数を書く。UFOのデータの下に書く（→ [07_switch_screen](../07_switch_screen/README.md)）。

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


## ステップ15. button_to_jump() 関数を作る

ボタンを押したら、別のページに切り替える関数を作る。`gamestage()` の前に書く。考え方は、[07_switch_screen](../07_switch_screen/README.md) の `button_to_jump()` と同じ。

- `def button_to_jump(btn, newpage):` で、ボタンの `Rect` と、移動先のページ番号を受け取る
- 関数の中の1行目に、`global page, pushFlag` を書く
- `mdown = pg.mouse.get_pressed()` と `(mx, my) = pg.mouse.get_pos()` で、マウスの状態と座標を調べる
- `mdown[0]`（左ボタンが押されている）のとき
  - `btn.collidepoint(mx, my) and not pushFlag`（ボタンの上で、まだ押していない）なら、音を鳴らして `page = newpage`、`pushFlag = True`
- 左ボタンが押されていなければ（`else:`）、`pushFlag = False` に戻す（`pushFlag` で、押しっぱなしのときに、ページが何度も切り替わるのを防ぐ）

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
            pg.mixer.Sound(SOUND_DIR / "pi.wav").play()
            page = newpage
            pushFlag = True
    else:
        pushFlag = False
```

</details>


## ステップ16. 自機とUFOが衝突したらゲームオーバーにする

`gamestage()` を変更する。

- 関数の1行目（`def gamestage():` の下）に、`global page` を足す（`page` を書き換えるため）
- `for ufo in ufos:` の中の、画面の下に出たUFOを戻す処理の下に、衝突の判定を書く
  - `if ufo.colliderect(myrect):`（UFOが自機に当たった）なら、`page = 2` でゲームオーバーのページに切り替え、`down.wav` の音を鳴らす

`global` の行:

<details>
<summary>コードを見る</summary>

```python
def gamestage():
    global page
```

</details>

UFOの処理の中:

<details>
<summary>コードを見る</summary>

```python
        ## 自機とUFOの衝突処理
        if ufo.colliderect(myrect):
            page = 2
            pg.mixer.Sound(SOUND_DIR / "down.wav").play()
```

</details>


## ステップ17. gamereset() 関数を作る

ゲームを最初の状態に戻す関数を作る。`gamestage()` の下に書く。

- `def gamereset():` で、引数のない関数を定義する
- `myrect.x = 400`、`myrect.y = 500` で、自機を最初の位置に戻す
- `bulletrect.y = OFFSCREEN_Y` で、弾を待機状態に戻す
- `for i in range(UFO_COUNT):` で、UFOを1体ずつ作り直す。`ufos[i] = pg.Rect(random.randint(0, WIDTH), OFFSCREEN_Y * i, UFO_SIZE, UFO_SIZE)` で、X座標をランダムに、Y座標を `OFFSCREEN_Y * i` にする（ステップ11と同じ）

<details>
<summary>コードを見る</summary>

```python

## データのリセット
def gamereset():
    myrect.x = 400
    myrect.y = 500
    bulletrect.y = OFFSCREEN_Y
    for i in range(UFO_COUNT):
        ufos[i] = pg.Rect(random.randint(0, WIDTH), OFFSCREEN_Y * i, UFO_SIZE, UFO_SIZE)
```

</details>


## ステップ18. gameover() 関数を作る

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


## ステップ19. メインループをページで分岐させる

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

ここまでで、`example/ex03.py` と同じ動きになる。UFOが自機に当たるとゲームオーバー画面になり、リプレイボタンで最初からやり直せる。


### 実行する

ターミナルで、リポジトリのルートから実行する（自分のファイルなら、ファイル名を置き換える）。

```bash
python 14_shooting_game/example/ex03.py
```

---

# ex04 — 弾でUFOを撃ち落とす

弾とUFOが衝突したらUFOを上に戻し、弾も待機状態にリセットする（完成形は [example/ex04.py](example/ex04.py)）。

## ステップ20. 弾とUFOが衝突したら、UFOを撃ち落とす

`for ufo in ufos:` の中の、自機との衝突の処理の下に書く。

- `if ufo.colliderect(bulletrect):`（UFOが弾に当たった）のとき、次の3つを行う
  - `ufo.y = OFFSCREEN_Y` と `ufo.x = random.randint(0, WIDTH)` で、そのUFOを、画面の外（上）の別の位置に戻す
  - `bulletrect.y = OFFSCREEN_Y` で、弾を待機状態に戻す（次の弾を撃てる）
  - `pg.mixer.Sound(SOUND_DIR / "piko.wav").play()` で、音を鳴らす

<details>
<summary>コードを見る</summary>

```python
        ## 弾とUFOの衝突処理
        if ufo.colliderect(bulletrect):
            ufo.y = OFFSCREEN_Y
            ufo.x = random.randint(0, WIDTH)
            bulletrect.y = OFFSCREEN_Y
            pg.mixer.Sound(SOUND_DIR / "piko.wav").play()
```

</details>

ここまでで、`example/ex04.py` と同じ動きになる。弾に当たったUFOが、画面の上に戻る。


### 実行する

ターミナルで、リポジトリのルートから実行する（自分のファイルなら、ファイル名を置き換える）。

```bash
python 14_shooting_game/example/ex04.py
```

---

# ex05 — スコアを追加する

UFOを撃墜するたびに 10 点加算する。ゲームオーバー画面でも確認できる（完成形は [example/ex05.py](example/ex05.py)）。

## ステップ21. スコアの変数を作る

撃ち落としたUFOの点数を数える `score` を作る。

- ボタンのデータのあとの「メインループで使う変数」の最初に、3つの定数を書く
  - `SCORE_FONT_SIZE = 40`: スコアの文字の大きさ
  - `SCORE_POS = (20, 20)`: スコアを描く位置
  - `SCORE_PER_HIT = 10`: UFOを1体撃ち落としたときの点数
- `page = 1` の下に、`score = 0` を書く
- `gamestage()` の `global` の行を、`global page, score` に変える（`score` も書き換えるため）

メインループで使う変数:

<details>
<summary>コードを見る</summary>

```python
## メインループで使う変数
SCORE_FONT_SIZE = 40
SCORE_POS       = (20, 20)
SCORE_PER_HIT   = 10

pushFlag = False
page = 1
score = 0
```

</details>

`global` の行:

<details>
<summary>コードを見る</summary>

```python
def gamestage():
    global page, score
```

</details>


## ステップ22. 撃ち落としたら、スコアを増やす

ステップ20の `if ufo.colliderect(bulletrect):` の中の、最初に書く。

- `score += SCORE_PER_HIT` で、スコアを `SCORE_PER_HIT`（10）点増やす

<details>
<summary>コードを見る</summary>

```python
        if ufo.colliderect(bulletrect):
            score += SCORE_PER_HIT
```

</details>


## ステップ23. スコアを描く

`gamestage()` の一番最後（`for ufo in ufos:` の外。字下げは、`for` と同じ）に書く。

- `## スコアの処理` の下で、`font = pg.font.Font(None, SCORE_FONT_SIZE)` で、フォントを作る
- `text = font.render("SCORE:" + str(score), True, pg.Color("WHITE"))` で、白い文字の画像を作る（`str(score)` で、数字を文字列に変えて、`"SCORE:"` とつなぐ）
- `screen.blit(text, SCORE_POS)` で、`SCORE_POS` の位置に貼り付ける

<details>
<summary>コードを見る</summary>

```python

    ## スコアの処理
    font = pg.font.Font(None, SCORE_FONT_SIZE)
    text = font.render("SCORE:" + str(score), True, pg.Color("WHITE"))
    screen.blit(text, SCORE_POS)
```

</details>


## ステップ24. gamereset() でスコアをリセットする

`gamereset()` を変更する。

- 関数の1行目に、`global score` を足す
- その下に、`score = 0` を足す（リプレイしたら、スコアを `0` に戻す）

<details>
<summary>コードを見る</summary>

```python
def gamereset():
    global score
    score = 0
```

</details>


## ステップ25. ゲームオーバー画面にスコアを描く

`gameover()` の中の、`btn1 = screen.blit(...)` の下（`button_to_jump(btn1, 1)` の前）に書く。ステップ23と同じ3行。

- `font = pg.font.Font(None, SCORE_FONT_SIZE)` で、フォントを作り直す（ゲームオーバーの文字より小さい大きさにするため）
- `text = font.render("SCORE:" + str(score), True, pg.Color("WHITE"))` で、文字の画像を作る
- `screen.blit(text, SCORE_POS)` で、貼り付ける

<details>
<summary>コードを見る</summary>

```python
    btn1 = screen.blit(replay_img, REPLAY_BTN_POS)
    font = pg.font.Font(None, SCORE_FONT_SIZE)
    text = font.render("SCORE:" + str(score), True, pg.Color("WHITE"))
    screen.blit(text, SCORE_POS)
    button_to_jump(btn1, 1)
```

</details>


## ステップ26. gameover() の gamereset() を条件付きにする

これまでは、`gameover()` の最初で、毎フレーム `gamereset()` を呼んでいた。ところが、ステップ24で `gamereset()` が `score` を `0` に戻すので、ゲームオーバー画面で、スコアが毎フレーム消えてしまう。リプレイボタンを押して、ページ1に戻ったあとだけ、リセットするように変える。

- `gameover()` の最初の `gamereset()` の行を、消す
- `button_to_jump(btn1, 1)` の下に、`if page == 1:`（ボタンが押されて、ページ1に戻った）を書き、その中で `gamereset()` を呼ぶ

<details>
<summary>コードを見る</summary>

```python
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

    ## ボタンを押してリプレイ時にリセット
    if page == 1:
        gamereset()
```

</details>

ここまでで、`example/ex05.py` と同じ、完成版の動きになる。UFOを撃ち落とすたびに10点増え、ゲームオーバー画面でもスコアを確認できる。


### 実行する

ターミナルで、リポジトリのルートから実行する（自分のファイルなら、ファイル名を置き換える）。

```bash
python 14_shooting_game/example/ex05.py
```
