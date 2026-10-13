```text
マルバツゲーム（○×ゲーム）をCLIで作り、その後pygameに移植しましょう
ステップごとにコードを書き足して、動かしながら完成させよう
```

# 目次
- [ゲームの仕様](#ゲームの仕様)
- [CLI版](#cli版)
  - [ボードと手番を用意する](#ボードと手番を用意する)
    - [ステップ1. ボードを作る](#ステップ1-ボードを作る)
    - [ステップ2. 現在のプレイヤーを決める](#ステップ2-現在のプレイヤーを決める)
  - [ボードを表示する](#ボードを表示する)
    - [ステップ3. print_board() 関数を作る](#ステップ3-print_board-関数を作る)
    - [ステップ4. 1行ずつ表示する](#ステップ4-1行ずつ表示する)
    - [ステップ5. 最後に空行を出力する](#ステップ5-最後に空行を出力する)
  - [勝利判定](#勝利判定)
    - [ステップ6. check_winner() 関数を作る](#ステップ6-check_winner-関数を作る)
    - [ステップ7. 横の判定](#ステップ7-横の判定)
    - [ステップ8. 縦の判定](#ステップ8-縦の判定)
    - [ステップ9. 斜めの判定](#ステップ9-斜めの判定)
    - [ステップ10. 引き分けの判定](#ステップ10-引き分けの判定)
    - [ステップ11. 決着がついていないとき](#ステップ11-決着がついていないとき)
  - [メインループ](#メインループ)
    - [ステップ12. ループを回して、ボードを表示する](#ステップ12-ループを回してボードを表示する)
    - [ステップ13. 行と列を入力する](#ステップ13-行と列を入力する)
    - [ステップ14. 埋まっているマスをはじく](#ステップ14-埋まっているマスをはじく)
    - [ステップ15. 手を置いて、勝敗を確認する](#ステップ15-手を置いて勝敗を確認する)
    - [ステップ16. 結果を表示して終了する](#ステップ16-結果を表示して終了する)
    - [ステップ17. プレイヤーを交代する](#ステップ17-プレイヤーを交代する)
  - [実行する](#実行する)
- [pygame版](#pygame版)
  - [ウィンドウを作る](#ウィンドウを作る)
    - [ステップ1. pygame を初期化する](#ステップ1-pygame-を初期化する)
    - [ステップ2. ウィンドウを作る](#ステップ2-ウィンドウを作る)
    - [ステップ3. 盤面の定数を決める](#ステップ3-盤面の定数を決める)
    - [ステップ4. メインループを作る](#ステップ4-メインループを作る)
  - [グリッドを描く](#グリッドを描く)
    - [ステップ5. draw_grid() 関数を作る](#ステップ5-draw_grid-関数を作る)
  - [ボードを管理して、記号を置く](#ボードを管理して記号を置く)
    - [ステップ6. ボードと手番の変数を作る](#ステップ6-ボードと手番の変数を作る)
    - [ステップ7. クリックしたセルに手を置く](#ステップ7-クリックしたセルに手を置く)
    - [ステップ8. draw_board() 関数で記号を描く](#ステップ8-draw_board-関数で記号を描く)
  - [勝敗を判定して、表示する](#勝敗を判定して表示する)
    - [ステップ9. 文字を描く関数を作る](#ステップ9-文字を描く関数を作る)
    - [ステップ10. 勝利判定](#ステップ10-勝利判定)
    - [ステップ11. 引き分け判定](#ステップ11-引き分け判定)
    - [ステップ12. 判定を呼び出して、クリック入力を止める](#ステップ12-判定を呼び出してクリック入力を止める)
  - [仕上げ](#仕上げ)
    - [ステップ13. リトライ機能](#ステップ13-リトライ機能)
    - [ステップ14. ESCキーで終了する](#ステップ14-escキーで終了する)
  - [実行する](#実行する-1)

---

# ゲームの仕様

- 2人で交互に ○ / × を置く
- 縦・横・斜めのいずれか3マスが揃ったら勝ち
- 全マスが埋まって誰も揃わなければ引き分け

---

# CLI版

まずはターミナル上で動く版を作る。新しい `.py` ファイルを作って、ステップごとにコードを書き足していく（完成版は [example/TicTocToe_cli.py](example/TicTocToe_cli.py)）。

## ボードと手番を用意する

3×3の二次元リストで盤面を管理する。数値で状態を表すことで、勝利判定を合計値で計算できる。

| 値 | 意味 |
| --- | --- |
| `0` | 空白 |
| `1` | 先攻 |
| `-1` | 後攻 |

### ステップ1. ボードを作る

変数 `board` に、3×3の二次元リストを代入する。

- 外側のリストの中に、行を3つ入れる
- 各行は、`0` を3つ並べたリスト（`[0, 0, 0]`）にする
- `0` は「空白」を表す
- 見やすいように、1行ずつ改行して書く（コメントに `0: 空白, 1: ○, -1: ×` と書いておくとよい）

<details>
<summary>コードを見る</summary>

```python
# 3×3のボード（0: 空白, 1: ○, -1: ×）
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
```

</details>

### ステップ2. 現在のプレイヤーを決める

変数 `current` に `1` を代入する。

- `1` は先攻、`-1` は後攻を表す（コメントに書いておくとよい）
- 手を置くたびに、この値を `1` ⇔ `-1` と入れ替えて、プレイヤーを交代する

<details>
<summary>コードを見る</summary>

```python
current = 1  # 1: 先攻, -1: 後攻
```

</details>

## ボードを表示する

### ステップ3. print_board() 関数を作る

`def print_board():` と書いて、引数のない関数を定義する。

- 関数の中身は、次のステップで書く（このステップだけでは、まだ実行できない）

<details>
<summary>コードを見る</summary>

```python
def print_board():
```

</details>

### ステップ4. 1行ずつ表示する

関数の中に、2行書く。

- `for row in board:` で、`board` の行を1つずつ `row` に取り出す
- `for` の中（1段深く字下げ）で、`print(*row)` を書いて、その行を出力する
  - `*` は、リストの要素を1つずつ取り出して、スペース区切りで出力するという意味

<details>
<summary>コードを見る</summary>

```python
def print_board():
    for row in board:
        print(*row)
```

</details>

出力例
```
0 0 0
0 1 0
0 0 -1
```

### ステップ5. 最後に空行を出力する

次の表示と区切れるように、ボードを出力したあとに空行を1つ出力する。

- 関数の最後（`for` の外。`for` と同じ字下げ）に、`print()` を1行書く

<details>
<summary>コードを見る</summary>

```python
def print_board():
    for row in board:
        print(*row)
    print()
```

</details>

## 勝利判定

横・縦・斜めの合計が `+3` なら先攻の勝ち、`-3` なら後攻の勝ち。先攻は `+1`、後攻は `-1` なので、3マス揃うと合計が `±3` になる。

### ステップ6. check_winner() 関数を作る

`def check_winner():` と書いて、関数を定義する。

- 関数の1行目に、盤面の大きさを `size` に入れる（`len(board)` で、行の数＝3が分かる）

<details>
<summary>コードを見る</summary>

```python
def check_winner():
    size = len(board)
```

</details>

### ステップ7. 横の判定

`size` の下に、各行を調べるくり返しを書く。

- `for i in range(size):` で、`i` を `0`〜`2` にして、くり返す
- `for` の中で、`i` 行目の合計 `sum(board[i])` を調べる
  - `size`（3）と等しければ、先攻が3つ揃っているので、`return 1`
  - `-size`（-3）と等しければ、後攻が3つ揃っているので、`return -1`
  - `if 条件:  return 値` は、1行で書ける
- `return` すると、関数はそこで終わる（勝者が決まったら、それ以上は調べない）

<details>
<summary>コードを見る</summary>

```python
    for i in range(size):
        # 横
        if sum(board[i]) == size:  return 1
        if sum(board[i]) == -size: return -1
```

</details>

### ステップ8. 縦の判定

ステップ7の `for i in range(size):` の中に、続けて書く。`i` 列目の合計を、自分で足して求める。

- `col = 0` で、合計の入れ物を用意する
- `for r in range(size):` で、行を `r` として回し、`col += board[r][i]` で、`i` 列目の値を足していく
- 足し終わったら（内側の `for` の外で）、横の判定と同じように判定する
  - `col == size` なら `return 1`
  - `col == -size` なら `return -1`

<details>
<summary>コードを見る</summary>

```python
        # 縦
        col = 0
        for r in range(size):
            col += board[r][i]
        if col == size:  return 1
        if col == -size: return -1
```

</details>

### ステップ9. 斜めの判定

`for i in range(size):`（ステップ7）の外（字下げを戻す）に書く。斜めは2本あるので、合計も2つ求める。

- `d1, d2 = 0, 0` で、2つの合計を `0` にしておく
- `for i in range(size):` で、次の2つを足していく
  - 左上→右下: `d1 += board[i][i]`
  - 右上→左下: `d2 += board[i][size - 1 - i]`（列を、右端から数える）
- くり返しの外で、判定する
  - `d1` か `d2` が `size` なら `return 1`（`or` で2つをつなぐ）
  - `d1` か `d2` が `-size` なら `return -1`

<details>
<summary>コードを見る</summary>

```python
    # 斜め
    d1, d2 = 0, 0
    for i in range(size):
        d1 += board[i][i]
        d2 += board[i][size - 1 - i]
    if d1 == size or d2 == size:  return 1
    if d1 == -size or d2 == -size: return -1
```

</details>

### ステップ10. 引き分けの判定

斜めの判定の下に書く。勝者がいなくて、空白（`0`）のマスが1つもなければ引き分け。

- `empty = 0` で、空白の数を数える入れ物を用意する
- 二重の `for` で、全マスを調べる
  - `for r in range(size):` の中に、`for c in range(size):` を書く
  - 一番内側で、`board[r][c] == 0` なら `empty += 1`
- くり返しの外で、`empty == 0` なら、`return "draw"`

<details>
<summary>コードを見る</summary>

```python
    # 引き分け
    empty = 0
    for r in range(size):
        for c in range(size):
            if board[r][c] == 0:
                empty += 1
    if empty == 0:
        return "draw"
```

</details>

### ステップ11. 決着がついていないとき

どの判定にも当てはまらなければ、勝負はまだついていない。

- 関数の最後（`for` や `if` の外）に、`return None` を書く

<details>
<summary>コードを見る</summary>

```python
    return None
```

</details>

## メインループ

### ステップ12. ループを回して、ボードを表示する

関数の外（字下げなし）に書く。

- `while True:` で、終わらないくり返しを作る
- ループの中で、`print_board()` を呼び出す

<details>
<summary>コードを見る</summary>

```python
# メインループ
while True:
    print_board()
```

</details>

### ステップ13. 行と列を入力する

ループの中の、`print_board()` の下に、2行書く。

- `row = int(input(...))` で、行を入力する。`input()` は文字列を返すので、`int()` で数字に変換する
- `col = int(input(...))` で、列を入力する
- `input()` の中の文は、`f"{current} 行(0-2): "` のように、`f` を付けて `{current}` を入れると、プレイヤーの番号が表示される

<details>
<summary>コードを見る</summary>

```python
    row = int(input(f"{current} 行(0-2): "))
    col = int(input(f"{current} 列(0-2): "))
```

</details>

### ステップ14. 埋まっているマスをはじく

入力の下に書く。選んだマスにすでに手が置かれていたら、入力し直させる。

- `if board[row][col] != 0:` で、そのマスが空白以外かを調べる
- `if` の中で、`print("そのマスは埋まっています\n")` を書く（`\n` で、表示のあとに空行が入る）
- 続けて `continue` を書くと、ループの先頭（ボードの表示）に戻る

<details>
<summary>コードを見る</summary>

```python
    if board[row][col] != 0:
        print("そのマスは埋まっています\n")
        continue
```

</details>

### ステップ15. 手を置いて、勝敗を確認する

`if` の下（字下げは、`while` の直下）に、2行書く。

- `board[row][col] = current` で、選んだマスに、現在のプレイヤーの値を入れる
- `result = check_winner()` で、勝敗を調べて、結果を `result` に入れる

<details>
<summary>コードを見る</summary>

```python
    board[row][col] = current
    result = check_winner()
```

</details>

### ステップ16. 結果を表示して終了する

`result` を調べて、結果を表示する。`if` と `elif` を使う。

- `result == "draw"` のとき（引き分け）: `print_board()`、`print("引き分け！")`、`break` の順に書く
- `elif result is not None:` のとき（勝者がいる。`result` は `1` か `-1`）: `print_board()`、`print(f"{result} の勝ち！")`、`break` の順に書く
- `break` で、ループを抜けて、プログラムが終わる

<details>
<summary>コードを見る</summary>

```python
    if result == "draw":
        print_board()
        print("引き分け！")
        break
    elif result is not None:
        print_board()
        print(f"{result} の勝ち！")
        break
```

</details>

### ステップ17. プレイヤーを交代する

決着がついていないときだけ、ここまで進む（`if` や `elif` の外。字下げは、`while` の直下）。

- `current *= -1` で、`1` ⇔ `-1` を入れ替える

<details>
<summary>コードを見る</summary>

```python
    current *= -1  # プレイヤー交代
```

</details>

## 実行する

ターミナルで、リポジトリのルートから実行する（自分のファイルなら、ファイル名を置き換える）。

```bash
python 12_TicTocToe/example/TicTocToe_cli.py
```

行と列を `0`〜`2` の数字で入力する。

---

# pygame版

CLI版の仕組みをpygameに移植する。ステップごとにコードを書き足していく（完成版は [example/TicTocToe.py](example/TicTocToe.py)）。

## ウィンドウを作る

### ステップ1. pygame を初期化する

- 1行目に、`import pygame as pg` で、pygame を `pg` という名前で読み込む
- `pg.init()` で、pygame を初期化する

<details>
<summary>コードを見る</summary>

```python
import pygame as pg

pg.init()
```

</details>

### ステップ2. ウィンドウを作る

ステップ1の下に、4行書く。

- `screen_width = 600`、`screen_height = 600` で、ウィンドウの幅と高さを変数にする
- `screen = pg.display.set_mode(...)` で、ウィンドウを作る。引数は、幅と高さを `(幅, 高さ)` の形にして1つ渡す（カッコが2重になる）
- `pg.display.set_caption('ox ゲーム')` で、タイトルバーの文字を設定する

<details>
<summary>コードを見る</summary>

```python
# ウィンドウの作成
screen_width = 600
screen_height = 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('ox ゲーム')
```

</details>

### ステップ3. 盤面の定数を決める

ステップ2の下に、盤面の大きさなどの定数を5つ書く（変えない値なので、名前は全て大文字）。

- `BOARD_SIZE = 3`: 3×3マス
- `CELL_SIZE = screen_width // BOARD_SIZE`: 1マスの大きさ（`600 // 3` で、200）
- `LINE_WIDTH = 5`: 線の太さ
- `CIRCLE_RADIUS = 80`: ○の半径
- `MARK_MARGIN = 20`: ×を描くときの、マスの端からの余白

<details>
<summary>コードを見る</summary>

```python
# 盤面の設定
BOARD_SIZE = 3                            # 3x3マス
CELL_SIZE = screen_width // BOARD_SIZE    # 1マスの大きさ(200)
LINE_WIDTH = 5                            # 線の太さ
CIRCLE_RADIUS = 80                        # 〇の半径
MARK_MARGIN = 20                          # ×を描く余白
```

</details>

### ステップ4. メインループを作る

背景を白（`pg.Color("WHITE")`）で塗りつぶして、画面を更新するだけのループを作る。

- `run = True` を書いて、`while run:` で、くり返す
- ループの中は、次の順番で書く
  1. `screen.fill(pg.Color("WHITE"))` で、背景を白で塗りつぶす
  2. `for event in pg.event.get():` で、イベントを1つずつ調べ、`event.type == pg.QUIT`（閉じるボタン）なら、`run = False` にする
  3. `pg.display.update()` で、画面を更新する
- ループが終わったあと（字下げなし）に、`pg.quit()` を書いて、pygame を終了する

<details>
<summary>コードを見る</summary>

```python
run = True
while run:

    # 背景の塗りつぶし
    screen.fill(pg.Color("WHITE"))

    # イベントの取得
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    # 更新
    pg.display.update()

pg.quit()
```

</details>

実行すると、白いウィンドウが表示される。閉じるボタンで終了できれば、ここまでは完成。

## グリッドを描く

### ステップ5. draw_grid() 関数を作る

縦線・横線を2本ずつ引く関数を作る。メインループ（`run = True`）より前に書く。

- `def draw_grid():` で、引数のない関数を定義する
- 関数の中で、`for i in range(1, BOARD_SIZE):` を書く（`i` は `1` と `2`。両端の線は引かない）
- `for` の中で、`pg.draw.line(screen, pg.Color("BLACK"), 始点, 終点, LINE_WIDTH)` を2本書く
  - 横線: 始点 `(0, i * CELL_SIZE)`、終点 `(screen_width, i * CELL_SIZE)`
  - 縦線: 始点 `(i * CELL_SIZE, 0)`、終点 `(i * CELL_SIZE, screen_height)`
  - `i * CELL_SIZE` で、セルの大きさ（200px）ごとに線の位置を計算する

<details>
<summary>コードを見る</summary>

```python
# グリッド線の描画
def draw_grid():
    for i in range(1, BOARD_SIZE):
        pg.draw.line(screen, pg.Color("BLACK"), (0, i * CELL_SIZE), (screen_width, i * CELL_SIZE), LINE_WIDTH)
        pg.draw.line(screen, pg.Color("BLACK"), (i * CELL_SIZE, 0), (i * CELL_SIZE, screen_height), LINE_WIDTH)
```

</details>

作った関数を、メインループの中の、`screen.fill(...)` の下で呼び出す。

<details>
<summary>コードを見る</summary>

```python
    # グリッド線の描画
    draw_grid()
```

</details>

実行すると、白い画面に、3×3のマス目が描かれる。

## ボードを管理して、記号を置く

### ステップ6. ボードと手番の変数を作る

CLI版と同じ `0 / 1 / -1` の二次元リストを、そのまま使える。ステップ3の下に書く。

- `board` に、`0` を3つ並べた行を3つ持つ、二次元リストを代入する（CLI版のステップ1と同じ）
- `number = 1` で、今の手番を管理する（`1`: ○、`-1`: ×）

<details>
<summary>コードを見る</summary>

```python
# ボード(0: 空白、1: 〇、-1: ×)
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

number = 1  # 1: 〇、-1: ×
```

</details>

### ステップ7. クリックしたセルに手を置く

まず、マウスがどのセルの上にあるかを求める。メインループの中の、`screen.fill(...)` の下に書く。

- `mx, my = pg.mouse.get_pos()` で、マウスの座標を取得する
- `x = mx // CELL_SIZE` で、何列目か（`0`〜`2`）を求める
- `y = my // CELL_SIZE` で、何行目か（`0`〜`2`）を求める

<details>
<summary>コードを見る</summary>

```python
    # マウスの位置の取得
    mx, my = pg.mouse.get_pos()
    x = mx // CELL_SIZE
    y = my // CELL_SIZE
```

</details>

次に、クリックされたときの処理を、イベントを調べる `for event in pg.event.get():` の中に書く。

- `event.type == pg.MOUSEBUTTONDOWN` のとき
- クリックしたセルが空白（`board[y][x] == 0`）のときだけ、次の2つを行う（`board[行][列]` の順なので、`board[y][x]` になる）
  - `board[y][x] = number` で、現在の手を置く
  - `number *= -1` で、`1` ⇔ `-1` を入れ替えて、手番を交代する

<details>
<summary>コードを見る</summary>

```python
        # マウスのクリック
        if event.type == pg.MOUSEBUTTONDOWN:
            if board[y][x] == 0:
                board[y][x] = number
                number *= -1
```

</details>

まだ記号は描いていないので、画面は変わらない。次のステップで描く。

### ステップ8. draw_board() 関数で記号を描く

`board` の値に合わせて、○と×を描く関数を作る。`draw_grid()` のあと（メインループより前）に書く。

- `def draw_board():` で、引数のない関数を定義する
- 関数の最初に、2つの値を求める
  - `center_offset = CELL_SIZE // 2`: マスの中心までの距離
  - `mark_far = CELL_SIZE - MARK_MARGIN`: ×の線の、反対側の端までの距離
- 二重の `for` で、全マスを調べる
  - `for row_index in range(BOARD_SIZE):` の中に、`for col_index in range(BOARD_SIZE):` を書く
  - 一番内側で、`col = board[row_index][col_index]` で、そのマスの値を取り出す
- `col == 1`（○）のとき
  - 中心 `center = (col_index * CELL_SIZE + center_offset, row_index * CELL_SIZE + center_offset)` を求める
  - `pg.draw.circle(screen, pg.Color("RED"), center, CIRCLE_RADIUS, LINE_WIDTH)` で、赤い円を描く
- `elif col == -1`（×）のとき、`pg.draw.line` を2本、`pg.Color("BLUE")` で描く
  - 1本目: 左上 `(col_index * CELL_SIZE + MARK_MARGIN, row_index * CELL_SIZE + MARK_MARGIN)` → 右下 `(col_index * CELL_SIZE + mark_far, row_index * CELL_SIZE + mark_far)`
  - 2本目: 右上 `(col_index * CELL_SIZE + mark_far, row_index * CELL_SIZE + MARK_MARGIN)` → 左下 `(col_index * CELL_SIZE + MARK_MARGIN, row_index * CELL_SIZE + mark_far)`
  - どちらも、太さは `LINE_WIDTH`

<details>
<summary>コードを見る</summary>

```python
# ボードの描画
def draw_board():
    center_offset = CELL_SIZE // 2
    mark_far = CELL_SIZE - MARK_MARGIN
    for row_index in range(BOARD_SIZE):
        for col_index in range(BOARD_SIZE):
            col = board[row_index][col_index]
            if col == 1:
                center = (col_index * CELL_SIZE + center_offset, row_index * CELL_SIZE + center_offset)
                pg.draw.circle(screen, pg.Color("RED"), center, CIRCLE_RADIUS, LINE_WIDTH)
            elif col == -1:
                pg.draw.line(screen, pg.Color("BLUE"), (col_index * CELL_SIZE + MARK_MARGIN, row_index * CELL_SIZE + MARK_MARGIN),
                             (col_index * CELL_SIZE + mark_far, row_index * CELL_SIZE + mark_far), LINE_WIDTH)
                pg.draw.line(screen, pg.Color("BLUE"), (col_index * CELL_SIZE + mark_far, row_index * CELL_SIZE + MARK_MARGIN),
                             (col_index * CELL_SIZE + MARK_MARGIN, row_index * CELL_SIZE + mark_far), LINE_WIDTH)
```

</details>

メインループの中の、`draw_grid()` の下で、呼び出す。

<details>
<summary>コードを見る</summary>

```python
    # ボードの描画
    draw_board()
```

</details>

実行すると、クリックしたマスに、交互に ○（赤）と ×（青）が描かれる。

## 勝敗を判定して、表示する

### ステップ9. 文字を描く関数を作る

まず、フォントを作る。ステップ3の下に書く。

- `font = pg.font.SysFont(None, 100)` で、デフォルトのフォントを、大きさ100で作る

<details>
<summary>コードを見る</summary>

```python
# フォントの設定
font = pg.font.SysFont(None, 100)
```

</details>

次に、文字を描く関数を作る。`draw_board()` のあとに書く。

- `def draw_message(main_text, sub_text=None, main_pos=(200, 200), sub_pos=(100, 400)):` で、関数を定義する
  - `sub_text=None` のように `=` を付けた引数は、省略できる（省略すると `None` になる）
  - `main_pos`・`sub_pos` は、文字を貼り付ける位置。省略すると、`=` の右の値になる
- 関数の中で、メインの文字を描く
  - `main_img = font.render(main_text, True, pg.Color("BLACK"), pg.Color("GREEN"))` で、文字の画像を作る（`True` は滑らかにする指定。続く2つは、文字の色と、背景の色）
  - `screen.blit(main_img, main_pos)` で、画面に貼り付ける
- `if sub_text:` のときだけ、同じように `sub_img` を作って、`sub_pos` に貼り付ける

<details>
<summary>コードを見る</summary>

```python
# 文字描画用関数
def draw_message(main_text, sub_text=None, main_pos=(200, 200), sub_pos=(100, 400)):
    """ 画面に文字を描画する """
    main_img = font.render(main_text, True, pg.Color("BLACK"), pg.Color("GREEN"))
    screen.blit(main_img, main_pos)
    if sub_text:
        sub_img = font.render(sub_text, True, pg.Color("BLACK"), pg.Color("GREEN"))
        screen.blit(sub_img, sub_pos)
```

</details>

### ステップ10. 勝利判定

横・縦・斜めの合計が `±3` になったら勝ち。CLI版のロジックを、pygame版の書き方に直す。勝者を `winner` に覚えておく（`'o'` か `'x'`）。`draw_message()` のあとに書く。

- `def check_winner():` で、関数を定義する
- 関数の最初に、3つの変数を用意する
  - `winner = None`: 勝者（まだ決まっていない）
  - `game_over = False`: 勝負がついたか
  - `size = len(board)`: 盤面の大きさ
- 横列と縦列を、`for row_index in range(size):` の中で調べる
  - 横: `sum(board[row_index])` が `size` なら `winner = 'o'`、`-size` なら `winner = 'x'`
  - 縦: `col_sum = 0` にして、`for i in range(size):` で `col_sum += board[i][row_index]` と足す。その合計が `size` なら `'o'`、`-size` なら `'x'`
- 斜めを、`for` の外で調べる
  - `diag1, diag2 = 0, 0` にして、`for i in range(size):` で、`diag1 += board[i][i]` と `diag2 += board[i][size - 1 - i]` を足す
  - `diag1 == size or diag2 == size` なら `'o'`、`diag1 == -size or diag2 == -size` なら `'x'`

<details>
<summary>コードを見る</summary>

```python
# 勝利／引き分けの確認
def check_winner():
    winner = None
    game_over = False
    size = len(board)

    # 横列・縦列の確認
    for row_index in range(size):
        # 横列
        if sum(board[row_index]) == size:
            winner = 'o'
        if sum(board[row_index]) == -size:
            winner = 'x'
        # 縦列
        col_sum = 0
        for i in range(size):
            col_sum += board[i][row_index]
        if col_sum == size:
            winner = 'o'
        if col_sum == -size:
            winner = 'x'

    # 斜めの確認
    diag1, diag2 = 0, 0
    for i in range(size):
        diag1 += board[i][i]
        diag2 += board[i][size - 1 - i]
    if diag1 == size or diag2 == size:
        winner = 'o'
    if diag1 == -size or diag2 == -size:
        winner = 'x'
```

</details>

続けて、結果の表示を書く（`# 勝敗表示`）。

- `winner == 'o' or winner == 'x'` のとき、`draw_message(winner + ' Win!', 'click to reset')` で、勝者と、リセットの案内を表示する
- 続けて、`game_over = True` にする
- 関数の最後（`if` の外）で、`return game_over` を書く

<details>
<summary>コードを見る</summary>

```python
    # 勝敗表示
    if winner == 'o' or winner == 'x':
        draw_message(winner + ' Win!', 'click to reset')
        game_over = True

    return game_over
```

</details>

### ステップ11. 引き分け判定

勝者がいなくて、全セルが埋まっていたら引き分け。ステップ10の `# 勝敗表示` の `if` の下に、`else:` を足して、その中に書く（`return game_over` の前）。

- `all_filled = True` で、「全部埋まっている」と仮定しておく
- 二重の `for` で、全マスを調べる
  - `for row in board:` の中に、`for cell in row:` を書く
  - `cell == 0`（空白）が見つかったら、`all_filled = False` にして、`break` で、内側の `for` を抜ける
  - 外側の `for` の中でも、`if not all_filled:` なら `break` して、外側も抜ける（見つかったら、それ以上調べない）
- `if all_filled:` のとき、`draw_message('Draw!', 'click to reset')` で表示して、`game_over = True` にする

<details>
<summary>コードを見る</summary>

```python
    else:
        # 全セルが0以外かどうかチェック（引き分け）
        all_filled = True
        for row in board:
            for cell in row:
                if cell == 0:
                    all_filled = False
                    break
            if not all_filled:
                break
        if all_filled:
            draw_message('Draw!', 'click to reset')
            game_over = True
```

</details>

### ステップ12. 判定を呼び出して、クリック入力を止める

まず、判定を呼び出す。メインループの中の、`draw_board()` の下に書く。

- `game_over = check_winner()` で、勝負がついたかを、毎回調べる

<details>
<summary>コードを見る</summary>

```python
    # 勝利の確認
    game_over = check_winner()
```

</details>

次に、勝負がついたあとは、クリックしても手を置けないようにする。ステップ7のクリックの処理を変える。

- `event.type == pg.MOUSEBUTTONDOWN` の中を、`if not game_over:` で囲む
- 囲んだ中（1段深く字下げ）に、これまでの `if board[y][x] == 0:` と、その中の2行を、そのまま入れる

<details>
<summary>コードを見る</summary>

```python
        # マウスのクリック
        if event.type == pg.MOUSEBUTTONDOWN:
            if not game_over:
                if board[y][x] == 0:
                    board[y][x] = number
                    number *= -1
```

</details>

実行すると、3つ揃ったときに `o Win!` や `x Win!`、揃わずに全部埋まったときに `Draw!` が表示される。

## 仕上げ

### ステップ13. リトライ機能

勝負がついたあとにクリックしたら、最初からやり直せるようにする。ステップ12の `if not game_over:` と同じ字下げ（`pg.MOUSEBUTTONDOWN` の中）に書く。

- `if game_over:` のとき、次の2つを行う
  - `board` に、`0` だけの3×3の二次元リストを、もう一度代入する
  - `number = 1` で、手番を先攻（○）に戻す

<details>
<summary>コードを見る</summary>

```python
            # リトライ機能
            if game_over:
                board = [
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]
                ]
                number = 1
```

</details>

### ステップ14. ESCキーで終了する

イベントを調べる `for event in pg.event.get():` の中の、`event.type == pg.QUIT` のあとに書く。

- `event.type == pg.KEYDOWN` のとき
- `event.key == pg.K_ESCAPE`（ESCキー）なら、`run = False` にする

<details>
<summary>コードを見る</summary>

```python
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False
```

</details>

## 実行する

ターミナルで、リポジトリのルートから実行する（自分のファイルなら、ファイル名を置き換える）。

```bash
python 12_TicTocToe/example/TicTocToe.py
```

マス目をクリックして、交互に ○ と × を置く。
