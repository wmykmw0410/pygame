```text
キーボード・マウスの入力を受け取ってゲームに反映する方法を学びましょう
以下のサンプルファイルを見ながら実際に動かしてみよう
```

# 目次
- [キー操作](#キー操作)
  - [どのキーが押されているか調べる](#どのキーが押されているか調べる)
  - [左右キーでキャラクタが動くプログラム](#左右キーでキャラクタが動くプログラム)
  - [左に進むときは絵を反転する](#左に進むときは絵を反転する)
- [マウス操作](#マウス操作)
  - [マウスが押されているか調べる](#マウスが押されているか調べる)
  - [マウスの座標を取得する](#マウスの座標を取得する)
  - [マウスで図形を動かす](#マウスで図形を動かす)
- [ボタンを作る](#ボタンを作る)
  - [クリックした位置がボタンの範囲内か調べる](#クリックした位置がボタンの範囲内か調べる)
  - [押したときに1回だけ実行する](#押したときに1回だけ実行する)
- [補足: イベント方式](#補足-イベント方式)
  - [get_pressedとの使い分け](#get_pressedとの使い分け)
  - [キーイベント](#キーイベント)
  - [マウスイベント](#マウスイベント)
- [付録: キーコード一覧](keycode.md)

---

# キー操作

サンプル: [01_keyboard/ex01.py](01_keyboard/ex01.py) / [01_keyboard/ex02.py](01_keyboard/ex02.py) / [01_keyboard/ex03.py](01_keyboard/ex03.py)

## どのキーが押されているか調べる

```python
# どのキーが押されているか調べる
key = pg.key.get_pressed()

# 右キーが押されたら
if key[pg.K_RIGHT]:
    <処理>

# 左キーが押されたら
if key[pg.K_LEFT]:
    <処理>
```

返ってきた変数には「どのキーが押されているか」の情報が入っている

| キー | 定数 |
| --- | --- |
| 上キー | `pg.K_UP` |
| 下キー | `pg.K_DOWN` |
| 右キー | `pg.K_RIGHT` |
| 左キー | `pg.K_LEFT` |
| 数字キー | `pg.K_0`, `pg.K_1` ... |

## 左右キーでキャラクタが動くプログラム

### step1. ゲームの準備をする
キャラクタの画像を変数に読み込んで、登場位置を変数 `myrect` に代入する

### step3. 画面を初期化する
キーが押されていない状態では画像は止まっているので、移動量 `vx` の初期値は `0` とする

### step5. 絵を描いたり、判定する
```python
if key[pg.K_RIGHT]:
    vx = 5
if key[pg.K_LEFT]:
    vx = -5
myrect.x += vx
```

## 左に進むときは絵を反転する

`transform.flip` 関数を使い、反転したい向きの引数を `True` にする

```python
# 左右反転した画像を作る(上下反転はFalse)
imageL = pg.transform.flip(imageR, True, False)
```

---

# マウス操作

サンプル: [02_mouse/ex04.py](02_mouse/ex04.py) / [02_mouse/ex05.py](02_mouse/ex05.py)

## マウスが押されているか調べる

```python
mdown = pg.mouse.get_pressed()
```

ボタンが押されている間 `True` になる

| インデックス | ボタン |
| --- | --- |
| `mdown[0]` | 左ボタン |
| `mdown[1]` | 真ん中ボタン |
| `mdown[2]` | 右ボタン |

## マウスの座標を取得する

```python
(mx, my) = pg.mouse.get_pos()
```

マウスが指している座標が `(mx, my)` に代入される

## マウスで図形を動かす

マウスで押した位置に図形を表示する

```python
if mdown[0]:
    pg.draw.rect(screen, pg.Color("RED"), (mx - 50, my - 50, 100, 100))
```

デフォルトでは `(mx, my)` が四角形の左上になるため、
幅・高さの半分(50)を引くことで四角形の中心をマウス位置に合わせる

---

# ボタンを作る

サンプル: [03_push_flag/ex06.py](03_push_flag/ex06.py) / [03_push_flag/ex07.py](03_push_flag/ex07.py)

## クリックした位置がボタンの範囲内か調べる

`blit` 関数の戻り値はボタン画像の範囲(Rect)なので、
`collidepoint` でクリック座標がその範囲内かどうかを調べられる

```python
# 画像を描画して、その範囲(Rect)を取得する
btn = screen.blit(next_img, (350, 200))

# マウスの座標がボタンの範囲内にあるか調べる
if mdown[0] and btn.collidepoint(mx, my):
    print("押した")
```

## 押したときに1回だけ実行する

`get_pressed()` はボタンを押し続けている間ずっと `True` になるため、
そのまま使うと処理が毎フレーム実行されてしまう

フラグ変数 `pushFlag` を使って「押した瞬間だけ」実行する

```python
pushFlag = False  # 最初は「まだ押されていない」

if mdown[0]:
    if btn.collidepoint(mx, my) and not pushFlag:
        print("押した")   # 押した瞬間だけ実行
        pushFlag = True   # 「押した」状態にする
else:
    pushFlag = False      # マウスを離したらリセット
```

| 状態 | `pushFlag` |
| --- | --- |
| 最初 / マウスを離した | `False` |
| ボタンを押した瞬間 | `False` → 処理実行 → `True` |
| 押し続けている間 | `True`(処理スキップ) |

---

# 補足: イベント方式

サンプル: [04_event/ex08.py](04_event/ex08.py)

## pg.event.get()

```python
for event in pg.event.get():
```

キーボード・マウス操作などをpygameが「イベント」としてキューに溜めておき、
`pg.event.get()` で溜まったイベントを一括取得してfor文で1つずつ取り出す

| 項目 | 内容 |
| --- | --- |
| 戻り値 | 発生したイベントのリスト |
| 呼び出しタイミング | 毎フレーム呼び出す(溜まったイベントをリセットする役割もある) |
| 呼び出さないと | イベントキューが溜まり続け、ウィンドウが応答しなくなる |

主なイベントの種類(`event.type` で判定する)

| `event.type` | 発生タイミング |
| --- | --- |
| `pg.QUIT` | 閉じるボタンを押した |
| `pg.KEYDOWN` | キーを押した瞬間 |
| `pg.KEYUP` | キーを離した瞬間 |
| `pg.MOUSEBUTTONDOWN` | マウスボタンを押した瞬間 |
| `pg.MOUSEBUTTONUP` | マウスボタンを離した瞬間 |
| `pg.MOUSEMOTION` | マウスを動かしたとき |

## get_pressedとの使い分け

| 方式 | 検知タイミング | 向いている用途 |
| --- | --- | --- |
| `get_pressed()` | 押している間ずっと | キャラの移動など連続動作 |
| イベント方式 | 押した瞬間・離した瞬間 | ジャンプ・射撃など1回きりの動作 |

## キーイベント

```python
for event in pg.event.get():
    if event.type == pg.KEYDOWN:      # キーを押した瞬間
        if event.key == pg.K_SPACE:
            print("スペース押した")   # 1回だけ実行される
    if event.type == pg.KEYUP:        # キーを離した瞬間
        if event.key == pg.K_SPACE:
            print("スペース離した")
```

## マウスイベント

イベント方式を使うと `pushFlag` なしで「押した瞬間だけ」を検知できる

```python
for event in pg.event.get():
    if event.type == pg.MOUSEBUTTONDOWN:   # マウスを押した瞬間
        if event.button == 1:              # 左ボタン
            print("マウス押した")          # 1回だけ実行される
    if event.type == pg.MOUSEBUTTONUP:     # マウスを離した瞬間
        if event.button == 1:
            print("マウス離した")
```

`event.button` の値はボタンの番号を表す(`get_pressed()` のインデックスと異なり1始まり)

| `event.button` | ボタン |
| --- | --- |
| `1` | 左ボタン |
| `2` | 真ん中ボタン |
| `3` | 右ボタン |

---

# 付録: キーコード一覧

→ [keycode.md](keycode.md) を参照
