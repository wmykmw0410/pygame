```text
マルバツゲーム（○×ゲーム）をCLIで作り、その後pygameに移植しましょう
```

# 目次
- [ゲームの仕様](#ゲームの仕様)
- [CLI版](#cli版)
  - [ボードの管理](#ボードの管理)
  - [ボードの表示](#ボードの表示)
  - [勝利判定](#勝利判定)
  - [メインループ](#メインループ)
- [pygame版](#pygame版)
  - [Step1 — ウィンドウを作る](#step1--ウィンドウを作る)
  - [Step2 — グリッドを描画する](#step2--グリッドを描画する)
  - [Step3 — ボードを管理する変数を作る](#step3--ボードを管理する変数を作る)
  - [Step4 — クリックしたセルに記号を描画する](#step4--クリックしたセルに記号を描画する)
  - [Step5 — 勝利判定](#step5--勝利判定)
  - [Step6 — 引き分け判定](#step6--引き分け判定)
  - [Step7 — 文字描画](#step7--文字描画)
  - [Step8 — リトライ機能](#step8--リトライ機能)

---

# ゲームの仕様

- 2人で交互に ○ / × を置く
- 縦・横・斜めのいずれか3マスが揃ったら勝ち
- 全マスが埋まって誰も揃わなければ引き分け

---

# CLI版

サンプル: [example/TicTocToe_cli.py](example/TicTocToe_cli.py)

まずはターミナル上で動く版を作る。

## ボードの管理

3×3の二次元リストで盤面を管理する。数値で状態を表すことで、勝利判定を合計値で計算できる。

| 値 | 意味 |
| --- | --- |
| `0` | 空白 |
| `1` | 先攻 |
| `-1` | 後攻 |

```
step1. board = [[0,0,0],[0,0,0],[0,0,0]] で3×3の盤面を作る
step2. current = 1 で現在のプレイヤーを管理する（1: 先攻, -1: 後攻）
```

<details>
<summary>コードを見る</summary>

```python
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
current = 1  # 1: 先攻, -1: 後攻
```

</details>

## ボードの表示

`print(*row)` でリストの要素をスペース区切りで出力する。

```
step1. print_board() 関数を作る
step2. for row in board: でリストを1行ずつ回す
step3. print(*row) で各行を出力する（* でリストを展開してスペース区切りにする）
```

出力例
```
0 0 0
0 1 0
0 0 -1
```

<details>
<summary>コードを見る</summary>

```python
def print_board():
    for row in board:
        print(*row)
```

</details>

## 勝利判定

横・縦・斜めの合計が `+3` なら先攻の勝ち、`-3` なら後攻の勝ち。先攻は `+1`、後攻は `-1` なので、3マス揃うと合計が `±3` になる。

```
step1. check_winner() 関数を作る
step2. 横の判定: 各行の sum が ±3 かチェックする
step3. 縦の判定: 各列の合計を求めて ±3 かチェックする
step4. 斜めの判定: 左上→右下と右上→左下の合計を求めてチェックする
step5. 全マス埋まって勝者なし → "draw" を返す
step6. 決着がついていないときは None を返す
```

<details>
<summary>コードを見る</summary>

```python
def check_winner():
    size = len(board)
    for i in range(size):
        if sum(board[i]) == size:  return 1    # 横
        if sum(board[i]) == -size: return -1
        col = sum(board[r][i] for r in range(size))
        if col == size:  return 1              # 縦
        if col == -size: return -1
    d1 = sum(board[i][i] for i in range(size))
    d2 = sum(board[i][size - 1 - i] for i in range(size))
    if d1 == size or d2 == size:  return 1    # 斜め
    if d1 == -size or d2 == -size: return -1
    if all(board[r][c] != 0 for r in range(size) for c in range(size)):
        return "draw"                          # 引き分け
    return None
```

</details>

## メインループ

`input()` で行・列を受け取り交互に置いていく。

```
step1. while True: でループを回す
step2. print_board() でボードを表示する
step3. input() で行・列を受け取る（int に変換する）
step4. すでに埋まっているマスなら continue で再入力させる
step5. board[row][col] = current で値をセットする
step6. check_winner() で勝敗を確認する
         None でなければゲーム終了メッセージを表示して break する
step7. current *= -1 でプレイヤーを交代する（1 ↔ -1）
```

<details>
<summary>コードを見る</summary>

```python
while True:
    print_board()
    row = int(input(f"{current} 行(0-2): "))
    col = int(input(f"{current} 列(0-2): "))
    if board[row][col] != 0:
        print("そのマスは埋まっています")
        continue
    board[row][col] = current
    result = check_winner()
    if result is not None:
        print_board()
        print(f"{result} の勝ち！" if result != "draw" else "引き分け！")
        break
    current *= -1  # プレイヤー交代（1 ↔ -1）
```

</details>

---

# pygame版

サンプル: [example/TicTocToe.py](example/TicTocToe.py)

CLI版の仕組みをpygameに移植する。

## Step1 — ウィンドウを作る

```
step1. pg.init() で初期化する
step2. pg.display.set_mode() でウィンドウサイズを指定する
step3. 色の定数（BLACK / WHITE / RED / GREEN / BLUE）を定義する
step4. メインループで pg.QUIT イベントを検知して終了する
```

<details>
<summary>コードを見る</summary>

```python
import pygame as pg

pg.init()
screen_width  = 600
screen_height = 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('OXゲーム')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    screen.fill(WHITE)
    pg.display.update()

pg.quit()
```

</details>

## Step2 — グリッドを描画する

```
step1. draw_grid() 関数を作る
step2. for i in range(1, 3): で2本の線を引く
step3. pg.draw.line() で横線と縦線をそれぞれ描く
         i * 200 でセル幅（200px）ごとに線の位置を計算する
```

<details>
<summary>コードを見る</summary>

```python
def draw_grid():
    for i in range(1, 3):
        pg.draw.line(screen, BLACK, (0, i * 200), (screen_width, i * 200), 5)
        pg.draw.line(screen, BLACK, (i * 200, 0), (i * 200, screen_height), 5)
```

</details>

## Step3 — ボードを管理する変数を作る

CLI版と同じ `0 / 1 / -1` の二次元リストをそのまま使える。

```
step1. board を3×3の二次元リストで初期化する
step2. number = 1 で現在のプレイヤーを管理する（1: ○, -1: ×）
```

<details>
<summary>コードを見る</summary>

```python
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
number = 1  # 1: ○, -1: ×
```

</details>

## Step4 — クリックしたセルに記号を描画する

```
step1. マウス座標 ÷ 200 で列・行のインデックスを求める
step2. pg.MOUSEBUTTONDOWN イベントでクリック位置の board に値をセットする
         空白（0）のときだけセットして number *= -1 で交代する
step3. draw_board() 関数を作る
         board の値が 1 なら ○（circle）、-1 なら ×（line×2）を描く
         各セルの中心座標 = (列 * 200 + 100, 行 * 200 + 100)
```

<details>
<summary>コードを見る</summary>

```python
mx, my = pg.mouse.get_pos()
x = mx // 200  # 列
y = my // 200  # 行

if event.type == pg.MOUSEBUTTONDOWN:
    if board[y][x] == 0:
        board[y][x] = number
        number *= -1
```

```python
def draw_board():
    for row_index in range(3):
        for col_index in range(3):
            val = board[row_index][col_index]
            cx = col_index * 200 + 100
            cy = row_index * 200 + 100
            if val == 1:
                pg.draw.circle(screen, RED, (cx, cy), 80, 5)
            elif val == -1:
                pg.draw.line(screen, BLUE, (cx - 80, cy - 80), (cx + 80, cy + 80), 5)
                pg.draw.line(screen, BLUE, (cx + 80, cy - 80), (cx - 80, cy + 80), 5)
```

</details>

## Step5 — 勝利判定

横・縦・斜めの合計が `±3` になったら勝ち。CLI版のロジックをそのまま流用できる。

```
step1. check_winner() 関数を作る（CLI版と同じ判定ロジック）
step2. 勝者が決まったら draw_message() で結果を表示する
step3. game_over = True を返してクリック入力を止める
```

<details>
<summary>コードを見る</summary>

```python
def check_winner():
    winner    = None
    game_over = False
    size = len(board)

    for row_index in range(size):
        if sum(board[row_index]) == size:  winner = 'o'
        if sum(board[row_index]) == -size: winner = 'x'
        col_sum = sum(board[i][row_index] for i in range(size))
        if col_sum == size:  winner = 'o'
        if col_sum == -size: winner = 'x'

    diag1 = sum(board[i][i] for i in range(size))
    diag2 = sum(board[i][size - 1 - i] for i in range(size))
    if diag1 == size  or diag2 == size:  winner = 'o'
    if diag1 == -size or diag2 == -size: winner = 'x'

    if winner:
        draw_message(winner + ' Win!', 'click to reset')
        game_over = True

    return game_over
```

</details>

## Step6 — 引き分け判定

勝者なし かつ 全セルが埋まっている → 引き分け。

```
step1. all_filled フラグを True で初期化する
step2. board の全セルを二重ループで確認する
         0（空白）が1つでも見つかれば all_filled = False にして break する
step3. all_filled が True かつ winner がなければ引き分けにする
```

<details>
<summary>コードを見る</summary>

```python
all_filled = True

for row in board:
    for cell in row:
        if cell == 0:
            all_filled = False
            break
    if not all_filled:
        break

if all_filled and not winner:
    draw_message('Draw!', 'click to reset')
    game_over = True
```

</details>

## Step7 — 文字描画

```
step1. pg.font.SysFont() でフォントを作成する
step2. draw_message(main_text, sub_text) 関数を作る
step3. font.render() でテキストを Surface に変換して screen.blit() で貼り付ける
step4. sub_text はデフォルト引数 None にして省略できるようにする
```

<details>
<summary>コードを見る</summary>

```python
font = pg.font.SysFont(None, 100)

def draw_message(main_text, sub_text=None, main_pos=(200, 200), sub_pos=(100, 400)):
    main_img = font.render(main_text, True, BLACK, GREEN)
    screen.blit(main_img, main_pos)
    if sub_text:
        sub_img = font.render(sub_text, True, BLACK, GREEN)
        screen.blit(sub_img, sub_pos)
```

</details>

## Step8 — リトライ機能

```
step1. game_over が True のときにクリックされたかを判定する
step2. board を初期状態の二次元リストで上書きする
step3. number = 1 でプレイヤーを先攻に戻す
```

<details>
<summary>コードを見る</summary>

```python
if game_over and event.type == pg.MOUSEBUTTONDOWN:
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    number = 1
```

</details>
