```text
Python と pygame を使って、ゼロからテトリスを作りましょう
```

# 目次
- [キー操作](#キー操作)
- [ファイル構成](#ファイル構成)
- [Step 1 — ウィンドウを表示する](#step-1--ウィンドウを表示する)
- [Step 2 — グリッドを作る](#step-2--グリッドを作る)
- [Step 3 — テトリミノのデータを定義する](#step-3--テトリミノのデータを定義する)
- [Step 4 — Tetrimino クラスを作る](#step-4--tetrimino-クラスを作る)
- [Step 5 — ミノを表示してキーで動かす](#step-5--ミノを表示してキーで動かす)
- [Step 6 — 自動落下を実装する](#step-6--自動落下を実装する)
- [Step 7 — 着地したら次のミノを生成する](#step-7--着地したら次のミノを生成する)
- [Step 8 — ラインを消す](#step-8--ラインを消す)
- [Step 9 — スピードアップする](#step-9--スピードアップする)
- [Step 10 — クラスに整理する](#step-10--クラスに整理する)
- [Step 11 — ゲームオーバーを実装する](#step-11--ゲームオーバーを実装する)
- [Step 12 — スタート画面とゲームオーバー画面を作る](#step-12--スタート画面とゲームオーバー画面を作る)
- [発展課題](#発展課題)

---

# キー操作

| キー | 動作 |
| --- | --- |
| ← → | 左右移動 |
| ↓ | 下に移動 |
| ↑ | 最下段へ落とす |
| A | 左回転（反時計回り） |
| S | 右回転（時計回り） |
| SPACE | スタート / リスタート |

---

# ファイル構成

| ファイル | 役割 |
| --- | --- |
| `main.py` | ゲームの起動・メインループ・ステート管理 |
| `config.py` | 定数・ミノ形状データ |
| `game/tetrimino.py` | `Tetrimino` クラス（ピースの状態・移動・回転・固定） |
| `game/tetris_game.py` | `TetrisGame` クラス（グリッド・落下・入力・ライン消去） |
| `game/tetris_renderer.py` | `Renderer` クラス（画面描画） |

---

# Step 1 — ウィンドウを表示する

`main.py` だけで始める。pygame を初期化してウィンドウを表示し、閉じるまでループを回す。

## やること

```
step1. pg.init() で pygame を初期化する
step2. pg.display.set_mode((300, 600)) でウィンドウを作る
step3. running = True でループ管理フラグを用意する
step4. for event in pg.event.get(): で毎フレームイベントを処理する
         pg.QUIT イベントが来たら running = False にして終了する
step5. pg.display.update() で画面を更新する
step6. ループを抜けたら pg.quit() で終了する
```

`pg.event.get()` を毎フレーム呼ばないとウィンドウが固まるので必ず入れる。

<details>
<summary>コードを見る</summary>

```python
import pygame as pg

pg.init()
screen = pg.display.set_mode((300, 600))
pg.display.set_caption("Tetris")

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.display.update()

pg.quit()
```

</details>

---

# Step 2 — グリッドを作る

テトリスのフィールドは **20行 × 10列** のグリッド。`0` を「空セル」として二次元リストで表現する。

## やること

```
step1. ROWS = 20 / COLS = 10 / CELL_SIZE = 30 を定数として定義する
step2. grid = [[0] * COLS for _ in range(ROWS)] で二次元リストを作る
step3. draw_grid(grid) 関数を作る
         二重ループで row / col を回す
         x = col * CELL_SIZE / y = row * CELL_SIZE でピクセル座標を計算する
         grid[row][col] が 0 でなければ色で塗る
         pg.draw.rect() でセルの枠線を描く
```

<details>
<summary>コードを見る</summary>

```python
ROWS      = 20
COLS      = 10
CELL_SIZE = 30
GRAY      = (100, 100, 100)

grid = [[0] * COLS for _ in range(ROWS)]

def draw_grid(grid):
    for row in range(ROWS):
        for col in range(COLS):
            x    = col * CELL_SIZE
            y    = row * CELL_SIZE
            rect = pg.Rect(x, y, CELL_SIZE, CELL_SIZE)
            if grid[row][col]:
                pg.draw.rect(screen, grid[row][col], rect)
            pg.draw.rect(screen, GRAY, rect, 1)  # 枠線
```

</details>

---

# Step 3 — テトリミノのデータを定義する

`config.py` に7種類のミノの形と色を辞書で定義する。形は `1` が「ブロックあり」の二次元リスト。

## やること

```
step1. TETORIMINO_SHAPES 辞書を作る
         キー: "I" / "O" / "T" / "S" / "Z" / "J" / "L"
         値: {"shape": [[...]], "color": (R, G, B)}
step2. shape は 1 がブロックあり、0 が空白の二次元リストで定義する
```

<details>
<summary>コードを見る</summary>

```python
TETORIMINO_SHAPES = {
    "I": {"shape": [[1, 1, 1, 1]],           "color": (0, 240, 240)},
    "O": {"shape": [[1, 1], [1, 1]],          "color": (240, 240, 0)},
    "T": {"shape": [[0,1,0],[1,1,1]],         "color": (160, 0, 240)},
    "S": {"shape": [[0,1,1],[1,1,0]],         "color": (0, 240, 0)},
    "Z": {"shape": [[1,1,0],[0,1,1]],         "color": (240, 0, 0)},
    "J": {"shape": [[1,0,0],[1,1,1]],         "color": (0, 0, 240)},
    "L": {"shape": [[0,0,1],[1,1,1]],         "color": (240, 160, 0)},
}
```

</details>

---

# Step 4 — Tetrimino クラスを作る

`game/tetrimino.py` に1ピースを表すクラスを作る。

## やること

```
step1. Tetrimino クラスを定義する
         __init__(self, shape, color, x, y) でプロパティを設定する

step2. move(self, dx, dy) を作る
         self.x += dx / self.y += dy で座標を更新する

step3. can_move(self, dx, dy, grid, rows, cols) を作る
         shape の各セルについて移動後の座標を計算する
         左右壁・床・既存ブロックに衝突するなら False を返す

step4. lock(self, grid) を作る
         shape の各セルが 1 なら grid[y][x] = self.color で色を書き込む

step5. spawn_tetrimino(self, cols) を作る
         self.x = (cols - len(shape[0])) // 2 で上部中央に配置する

step6. rotate_right(self) / rotate_left(self) を作る
         右回転: shape の転置と上下反転の組み合わせで実装する
         左回転: 上下反転してから転置する
```

<details>
<summary>コードを見る</summary>

```python
class Tetrimino:
    def __init__(self, shape, color, x, y):
        self.shape = shape
        self.color = color
        self.x     = x
        self.y     = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def can_move(self, dx, dy, grid, rows, cols):
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    new_x = self.x + col_idx + dx
                    new_y = self.y + row_idx + dy
                    if new_x < 0 or new_x >= cols:
                        return False
                    if new_y >= rows:
                        return False
                    if new_y >= 0 and grid[new_y][new_x]:
                        return False
        return True

    def lock(self, grid):
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    grid[self.y + row_idx][self.x + col_idx] = self.color

    def spawn_tetrimino(self, cols=10):
        self.x = (cols - len(self.shape[0])) // 2
        self.y = 0

    def rotate_right(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

    def rotate_left(self):
        self.shape = [list(row) for row in zip(*self.shape)][::-1]
```

</details>

---

# Step 5 — ミノを表示してキーで動かす

現在のピースを描画する関数を作り、キー入力で左右移動・回転できるようにする。

## やること

```
step1. draw_tetrimino(piece) 関数を作る
         shape の二重ループで cell == 1 のマスを pg.draw.rect() で描く
         x = (piece.x + col_idx) * CELL_SIZE でピクセル座標を計算する

step2. イベントループに pg.KEYDOWN の処理を追加する
         K_LEFT / K_RIGHT: can_move() で判定してから move() を呼ぶ
         K_DOWN: 1マス下に移動する
         K_UP: can_move(0,1,...) が False になるまで繰り返し move(0,1) する
         K_a / K_s: rotate_left() / rotate_right() を呼ぶ
                    回転後に can_move(0,0,...) が False なら shape を元に戻す
```

<details>
<summary>コードを見る</summary>

```python
def draw_tetrimino(piece):
    for row_idx, row in enumerate(piece.shape):
        for col_idx, cell in enumerate(row):
            if cell:
                x    = (piece.x + col_idx) * CELL_SIZE
                y    = (piece.y + row_idx) * CELL_SIZE
                rect = pg.Rect(x, y, CELL_SIZE, CELL_SIZE)
                pg.draw.rect(screen, piece.color, rect)
                pg.draw.rect(screen, GRAY, rect, 1)
```

```python
if event.type == pg.KEYDOWN:
    if event.key == pg.K_LEFT:
        if piece.can_move(-1, 0, grid, ROWS, COLS):
            piece.move(-1, 0)
    elif event.key == pg.K_RIGHT:
        if piece.can_move(1, 0, grid, ROWS, COLS):
            piece.move(1, 0)
    elif event.key == pg.K_UP:
        while piece.can_move(0, 1, grid, ROWS, COLS):
            piece.move(0, 1)
    elif event.key == pg.K_a:
        original_shape = [row[:] for row in piece.shape]
        piece.rotate_left()
        if not piece.can_move(0, 0, grid, ROWS, COLS):
            piece.shape = original_shape
```

</details>

---

# Step 6 — 自動落下を実装する

タイマーで一定時間ごとにミノを1マス下に落とす。

## やること

```
step1. fall_interval = 500 で落下間隔(ms)を設定する
step2. last_fall = pg.time.get_ticks() で最後に落下した時刻を記録する
step3. メインループの中で毎フレーム現在時刻を取得する
         now = pg.time.get_ticks()
step4. now - last_fall >= fall_interval になったら落下処理を行う
         can_move(0, 1, ...) が True なら move(0, 1) で1マス落とす
         last_fall = now で時刻を更新する
```

<details>
<summary>コードを見る</summary>

```python
fall_interval = 500
last_fall     = pg.time.get_ticks()

# メインループ内
now = pg.time.get_ticks()
if now - last_fall >= fall_interval:
    if piece.can_move(0, 1, grid, ROWS, COLS):
        piece.move(0, 1)
    last_fall = now
```

</details>

---

# Step 7 — 着地したら次のミノを生成する

`can_move(0, 1, ...)` が `False` のとき着地。グリッドに固定して次のミノを生成する。

## やること

```
step1. can_move(0, 1, ...) が False のとき着地と判断する
step2. piece.lock(grid) でグリッドにピースの色を書き込む
step3. ランダムに新しいミノを生成して piece に代入する
         random.choice(list(TETORIMINO_SHAPES.values())) でデータを選ぶ
         Tetrimino(...) でインスタンスを作り spawn_tetrimino() で位置を設定する
```

<details>
<summary>コードを見る</summary>

```python
def spawn_piece():
    mino_data = random.choice(list(TETORIMINO_SHAPES.values()))
    piece = Tetrimino(
        shape=[row[:] for row in mino_data["shape"]],
        color=mino_data["color"],
        x=0,
        y=0,
    )
    piece.spawn_tetrimino(COLS)
    return piece

# メインループ内（落下タイマーの else 節）
else:
    piece.lock(grid)
    piece = spawn_piece()
```

</details>

---

# Step 8 — ラインを消す

全セルが埋まった行を除去し、上に空行を追加してブロックを「落とす」。

## やること

```
step1. clear_lines(grid) 関数を作る
step2. grid の各行を確認して、空セル（0）が1つもない行を取り除く
step3. 取り除いた行数だけ先頭に空行 ([0] * COLS) を追加する
         → ブロックが上から落ちてくる見た目になる
step4. 消去した行数を total_lines に加算してスコアを更新する
```

<details>
<summary>コードを見る</summary>

```python
def clear_lines(grid, total_lines):
    new_grid = []
    cleared  = 0
    for row in grid:
        has_empty = False
        for cell in row:
            if cell == 0:
                has_empty = True
                break
        if has_empty:
            new_grid.append(row)
        else:
            cleared += 1

    for _ in range(cleared):
        new_grid.insert(0, [0] * COLS)

    total_lines += cleared
    return new_grid, total_lines
```

</details>

---

# Step 9 — スピードアップする

消去ライン数に応じて落下間隔を短くする。最小値を設けて難易度が上がりすぎないようにする。

## やること

```
step1. FALL_INTERVAL_MIN = 100 で最速の落下間隔(ms)を定義する
step2. FALL_SPEED_STEP_LINES = 5 で何ライン消すごとに加速するかを定義する
step3. FALL_SPEED_STEP_MS = 50 で加速ごとに短縮する時間(ms)を定義する
step4. ライン消去のたびに fall_interval を再計算する
         減らした値が FALL_INTERVAL_MIN を下回らないよう制限する
```

<details>
<summary>コードを見る</summary>

```python
FALL_INTERVAL_INIT      = 500
FALL_INTERVAL_MIN       = 100
FALL_SPEED_STEP_LINES   = 5
FALL_SPEED_STEP_MS      = 50

# ライン消去後に再計算する
new_interval = FALL_INTERVAL_INIT - (total_lines // FALL_SPEED_STEP_LINES) * FALL_SPEED_STEP_MS
if new_interval < FALL_INTERVAL_MIN:
    new_interval = FALL_INTERVAL_MIN
fall_interval = new_interval
```

</details>

---

# Step 10 — クラスに整理する

コードが大きくなってきたら、責務ごとにクラスに分けてファイルを整理する。

## やること

```
step1. Tetrimino クラス → game/tetrimino.py
         ピースの状態・移動・回転・固定を担当する

step2. TetrisGame クラス → game/tetris_game.py
         grid / current_piece / total_lines / fall_interval を持つ
         update() で落下タイマーと着地処理を行う
         handle_input(event) でキー入力を処理する
         _clear_lines() でライン消去とスピードアップを行う

step3. Renderer クラス → game/tetris_renderer.py
         __init__(self, screen) で screen とフォントを持つ
         draw(game) でグリッド・ピース・スコアをまとめて描画する

step4. main.py はゲームループとステート管理だけにする
         game.update() と renderer.draw(game) を呼ぶだけになる
```

<details>
<summary>コードを見る</summary>

```python
# main.py（クラス整理後）
game     = TetrisGame()
renderer = Renderer(screen)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            game.handle_input(event)

    game.update()
    renderer.draw(game)
    pg.display.update()
    clock.tick(FPS)
```

</details>

---

# Step 11 — ゲームオーバーを実装する

新しいミノがスポーン位置に置けないときをゲームオーバーとする。

## やること

```
step1. TetrisGame に game_over = False フラグを追加する
step2. _spawn_piece() で新しいミノを生成した直後に判定する
         can_move(0, 0, ...) が False ならスポーン位置が埋まっている → ゲームオーバー
         game_over = True にする
step3. main.py で game.game_over を監視する
         True になったら state を GAME_OVER に切り替える
step4. GAME_OVER 状態のときは game.update() と handle_input() を呼ばない
```

<details>
<summary>コードを見る</summary>

```python
# TetrisGame.update() 内
self.current_piece = self._spawn_piece()
if not self.current_piece.can_move(0, 0, self.grid, ROWS, COLS):
    self.game_over = True
```

```python
# main.py 内
if state == PLAYING:
    game.update()
    if game.game_over:
        state = GAME_OVER
```

</details>

---

# Step 12 — スタート画面とゲームオーバー画面を作る

`main.py` に3つのステートを用意してシーンを切り替える。

## やること

```
step1. START / PLAYING / GAME_OVER の3つのステート文字列を定義する
step2. state = START で初期状態を設定する
step3. SPACE キーでステートを遷移させる
         START → PLAYING: そのままゲーム開始
         GAME_OVER → PLAYING: TetrisGame() を作り直して再スタート
step4. Renderer に draw_overlay(title, subtitle) メソッドを追加する
         pg.Surface で半透明の黒いオーバーレイを作って画面に重ねる
         タイトルとサブタイトルを中央に描画する
step5. ステートに応じて draw_overlay() を呼び分ける
```

```
START → (SPACE) → PLAYING → (game over) → GAME_OVER → (SPACE) → PLAYING
```

<details>
<summary>コードを見る</summary>

```python
START     = "start"
PLAYING   = "playing"
GAME_OVER = "game_over"

state = START

# SPACE キーの処理
if event.key == pg.K_SPACE:
    if state == START:
        state = PLAYING
    elif state == GAME_OVER:
        game  = TetrisGame()
        state = PLAYING
```

```python
# Renderer.draw_overlay()
def draw_overlay(self, title, subtitle):
    overlay = pg.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(160)        # 半透明
    overlay.fill((0, 0, 0))
    self.screen.blit(overlay, (0, 0))

    cx         = WIDTH // 2
    title_surf = self.title_font.render(title, True, (255, 255, 255))
    sub_surf   = self.font.render(subtitle, True, (100, 100, 100))
    self.screen.blit(title_surf, title_surf.get_rect(center=(cx, HEIGHT // 2 - 30)))
    self.screen.blit(sub_surf,   sub_surf.get_rect(center=(cx, HEIGHT // 2 + 20)))
```

```python
# main.py — ステートに応じてオーバーレイを表示する
renderer.draw(game)
if state == START:
    renderer.draw_overlay("TETRIS", "Press SPACE to Start")
elif state == GAME_OVER:
    renderer.draw_overlay("GAME OVER", f"Lines: {game.total_lines}  |  Press SPACE to Restart")
```

</details>

---

# 発展課題

基本版は `Tetris/`、発展版は `advanced/` フォルダにある。

| バージョン | 起動コマンド |
| --- | --- |
| 基本版 | `python Tetris/main.py` |
| 発展版 | `python advanced/main.py` |

`advanced/` フォルダに4つの機能を追加した完成版がある。

| 機能 | 操作 | 実装場所 |
| --- | --- | --- |
| ネクストミノ表示 | — | `tetris_renderer.py` `_draw_panel()` |
| スコア表示 | — | `tetris_game.py` `_clear_lines()` / `config.py` `SCORE_TABLE` |
| ホールド | H キー | `tetris_game.py` `_do_hold()` |
| ゴーストピース | — | `tetris_renderer.py` `_draw_ghost()` |

| キー | 動作 |
| --- | --- |
| ← → | 左右移動 |
| ↓ | 下に移動 |
| ↑ | 最下段へ落とす |
| A | 左回転 |
| S | 右回転 |
| H | ホールド |
| SPACE | スタート / リスタート |

## スコア計算

1回のライン消去で得られる点数は消去ライン数に応じて増加する。

| 消去ライン数 | 点数 |
| --- | --- |
| 1 | 100 |
| 2 | 300 |
| 3 | 500 |
| 4（テトリス） | 800 |

## ホールド機能の仕組み

```
step1. H キーで現在のピースを hold_kind に退避する
step2. hold_kind が空のときは next_piece を current に昇格する
step3. hold_kind にすでにピースがあるときは current と swap する
step4. 同じピースを持っている間は再ホールドできない（can_hold フラグで管理）
step5. ピースが着地したら can_hold を True に戻す
```

## ゴーストピースの仕組み

```
step1. can_move(0, dy+1, ...) が False になるまで dy を増やす
step2. piece.y + dy がゴーストの Y 座標になる
step3. 実ピースと同じ形を、同じ色の枠線のみ（塗りつぶしなし）で描画する
```
