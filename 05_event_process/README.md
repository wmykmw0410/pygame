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
- [演習問題1](#演習問題1)

---

# キー操作

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

サンプル: [01_keyboard/ex01.py](01_keyboard/ex01.py)

練習: [01_keyboard/practice01.py](01_keyboard/practice01.py)（「# ★」の部分が空欄になっているので、サンプルを見ながら自分の手でコードを打ち込んで完成させよう）

動いたら、書き換えてもう一度動かし、変化を確認する。

| 試すこと | 確認すること |
| --- | --- |
| 右キーを押し続ける | 押している間、毎フレーム（1秒に約60回）表示され続ける |
| 右キーと左キーを同時に押す | 2つの `if` がどちらも成り立つので、`RIGHT` と `LEFT` の両方が表示される |
| `pg.K_RIGHT` → `pg.K_UP` / `pg.K_SPACE` | 指定したキーに反応するようになる（キーの定数は上の表や [keycode.md](keycode.md) を参照） |
| 上キー・下キー用の `if` を足す | 上下キーにも反応する |

## 左右キーでキャラクタが動くプログラム

### step1. ゲームの準備をする
キャラクタの画像を変数に読み込んで、登場位置を変数 `myrect` に代入する

### step3. 画面を初期化する
キーが押されていない状態では画像は止まっているので、移動量 `vx` の初期値は `0` とする

### step5. 絵を描いたり、判定する
```python
MOVE_SPEED = 5

if key[pg.K_RIGHT]:
    vx = MOVE_SPEED
if key[pg.K_LEFT]:
    vx = -MOVE_SPEED
myrect.x += vx
```

サンプル: [01_keyboard/ex02.py](01_keyboard/ex02.py)

練習: [01_keyboard/practice02.py](01_keyboard/practice02.py)

| 試すこと | 確認すること |
| --- | --- |
| `MOVE_SPEED` の `5` → `1` / `20` | 数が大きいほど速く動く（1フレームで動くピクセル数が変わる） |
| `vx = MOVE_SPEED` と `vx = -MOVE_SPEED` を入れ替える | 右キーで左、左キーで右に動くようになる |
| `vx = 0` をループの外に移動 | キーを離しても止まらず、最後に動いた向きに動き続ける（毎フレーム `vx` を `0` に戻しているから止まる） |
| キーを押し続けて右端まで進む | 画面の外に出ても止まらない（`myrect.x` は増え続ける） |
| `topleft=(300, 200)` → `(0, 400)` | 動き始める位置が変わる |
| 上キー・下キーを `vy` と `myrect.y` で足す | 上下にも動く |

## 左に進むときは絵を反転する

`transform.flip` 関数を使い、反転したい向きの引数を `True` にする

```python
# 左右反転した画像を作る(上下反転はFalse)
imageL = pg.transform.flip(imageR, True, False)
```

サンプル: [01_keyboard/ex03.py](01_keyboard/ex03.py)

練習: [01_keyboard/practice03.py](01_keyboard/practice03.py)

| 試すこと | 確認すること |
| --- | --- |
| `flip(imageR, True, False)` → `(False, True)` / `(True, True)` | 2つ目の引数が上下、1つ目が左右の反転。`(False, True)` は上下が逆さ、`(True, True)` は上下左右が逆になる |
| `rightFlag` の最初の値 `True` → `False` | 最初から左向き（反転した画像）で表示される |
| 左キーのときの `rightFlag = False` を消す | 左キーを押しても向きが変わらず、右向きのまま動く |
| どちらのキーも押さない | 向きは変わらず、最後に向いていた方向のまま（フラグが向きを覚えている） |

---

# マウス操作

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

サンプル: [02_mouse/ex04.py](02_mouse/ex04.py)

練習: [02_mouse/practice04.py](02_mouse/practice04.py)

| 試すこと | 確認すること |
| --- | --- |
| ボタンを押さずにマウスを動かす | 何も表示されない（`mdown[0]` が `True` のときだけ表示する） |
| ボタンを押したままマウスを動かす | 座標が毎フレーム、変わりながら表示される |
| `mdown[0]` → `mdown[2]` | 右ボタンを押したときだけ表示される |
| `mdown[0]` のまま右ボタンを押す | 表示されない（`mdown[0]` は左ボタンの状態） |

## マウスで図形を動かす

マウスで押した位置に図形を表示する

```python
RECT_SIZE = 100

if mdown[0]:
    pg.draw.rect(screen, pg.Color("RED"), (mx - RECT_SIZE // 2, my - RECT_SIZE // 2, RECT_SIZE, RECT_SIZE))
```

デフォルトでは `(mx, my)` が四角形の左上になるため、
幅・高さの半分(`RECT_SIZE // 2`)を引くことで四角形の中心をマウス位置に合わせる

サンプル: [02_mouse/ex05.py](02_mouse/ex05.py)

練習: [02_mouse/practice05.py](02_mouse/practice05.py)

| 試すこと | 確認すること |
| --- | --- |
| `RECT_SIZE` の `100` → `20` / `200` | 四角の大きさが変わる（中心はマウス位置のまま） |
| ボタンを離す | 四角が消える（毎フレーム、画面を白で塗りつぶしているため） |
| `mx - RECT_SIZE // 2, my - RECT_SIZE // 2` → `mx, my` | 四角の左上がマウス位置になり、四角はマウスの右下に描かれる |
| `mdown[0]` → `mdown[2]` | 右ボタンを押したときに描かれる |

---

# ボタンを作る

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

サンプル: [03_push_flag/ex06.py](03_push_flag/ex06.py)

練習: [03_push_flag/practice06.py](03_push_flag/practice06.py)

| 試すこと | 確認すること |
| --- | --- |
| ボタンの外をクリックする | 何も表示されない |
| ボタンの上でボタンを押し続ける | 押している間、毎フレーム「押した」が表示され続ける（次の「押したときに1回だけ実行する」で解決する） |
| `screen.blit(next_img, (350, 200))` の位置を `(100, 400)` に変える | 反応する場所も、画像を描いた新しい位置に移る（`btn` は画像を描いた範囲だから） |

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

サンプル: [03_push_flag/ex07.py](03_push_flag/ex07.py)

練習: [03_push_flag/practice07.py](03_push_flag/practice07.py)

| 試すこと | 確認すること |
| --- | --- |
| ボタンの上でボタンを押し続ける | 「押した」は1回だけ表示される |
| 一度離して、もう一度押す | もう一度、1回だけ表示される（離したときに `pushFlag` が `False` に戻るため） |
| `pushFlag = True` の行を消す | 押し続けている間、毎フレーム表示される（フラグが立たないので、毎回条件が成り立つ） |
| `else:` と `pushFlag = False` の2行を消す | 最初の1回しか表示されない。離してもう一度押しても表示されない（フラグが戻らないため） |
| ボタンの外で押したまま、マウスをボタンの上に動かす | ボタンの範囲に入った瞬間に、1回表示される（押した位置ではなく、押している間の位置で判定しているため） |

---

# 補足: イベント方式

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

サンプル: [04_event/ex08.py](04_event/ex08.py)

練習: [04_event/practice08.py](04_event/practice08.py)

| 試すこと | 確認すること |
| --- | --- |
| `pg.K_SPACE` → `pg.K_RETURN` | Enter キーで四角が表示される（スペースキーでは表示されない） |
| スペースキーを押し続ける | 表示は1回だけ（イベントは「押した瞬間」にだけ発生する） |
| `event.button == 1` → `3` | 右クリックで四角が消える。左クリックでは消えない |
| `pg.MOUSEBUTTONDOWN` → `pg.MOUSEBUTTONUP` | クリックして、ボタンを離したときに四角が消える |
| `pg.KEYDOWN` → `pg.KEYUP` | スペースキーを離したときに四角が表示される |

---

# 付録: キーコード一覧

→ [keycode.md](keycode.md) を参照

---

# 演習問題1

## マウスの座標をトレースして文字を書く

> 問題: [question/question1.py](question/question1.py) / 解答: [question/answer/answer1.py](question/answer/answer1.py)
