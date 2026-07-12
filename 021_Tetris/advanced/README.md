```text
基本版（../）に4つの発展機能を追加したバージョンです
```

# 目次
- [キー操作](#キー操作)
- [ファイル構成](#ファイル構成)
- [発展1 — ネクストミノの表示](#発展1--ネクストミノの表示)
- [発展2 — スコア表示](#発展2--スコア表示)
- [発展3 — ホールド機能](#発展3--ホールド機能)
- [発展4 — ゴーストピース](#発展4--ゴーストピース)

---

# キー操作

| キー | 動作 |
| --- | --- |
| ← → | 左右移動 |
| ↓ | 下に移動 |
| ↑ | 最下段へ落とす |
| A | 左回転（反時計回り） |
| S | 右回転（時計回り） |
| H | ホールド |
| SPACE | スタート / リスタート |

---

# ファイル構成

基本版と同じクラス構成で、各ファイルに機能を追加している。

| ファイル | 変更点 |
| --- | --- |
| `config.py` | `MINI_CELL` / `PANEL_X` / `SCORE_TABLE` を追加。`WIDTH` を 420px に拡張 |
| `game/tetrimino.py` | `kind` 属性を追加（ホールド復元に使用） |
| `game/tetris_game.py` | `next_piece` / `hold_kind` / `can_hold` / `score` を追加 |
| `game/tetris_renderer.py` | ゴーストピース・サイドパネル（NEXT / HOLD / SCORE / LINES）の描画を追加 |
| `main.py` | ウィンドウ幅を 420px に変更 |

---

# 発展1 — ネクストミノの表示

サンプル: [game/tetris_game.py](game/tetris_game.py) / [game/tetris_renderer.py](game/tetris_renderer.py)

次に出るピースをサイドパネルに表示する。

## やること

```
step1. TetrisGame に next_piece を追加する
         __init__ で next_piece = _spawn_piece() を先に生成しておく
         current_piece は next_piece から取り出す（_pop_next）
         ピースが着地するたびに _pop_next() で次を補充する

step2. _pop_next() メソッドを作る
         piece = self.next_piece を保存する
         self.next_piece = self._spawn_piece() で新しいネクストを生成する
         piece を返す

step3. config.py に MINI_CELL と PANEL_X を追加する
         MINI_CELL = 18  プレビュー用の小さいセルサイズ
         PANEL_X   = COLS * CELL_SIZE  サイドパネルの開始 X 座標

step4. Renderer に _draw_mini_piece(shape, color, origin_x, origin_y) を作る
         shape の二重ループで cell == 1 のマスを MINI_CELL サイズで描く

step5. Renderer に _draw_panel(game) を作る
         "NEXT" ラベルを描画する
         game.next_piece の shape と color で _draw_mini_piece() を呼ぶ
         パネル内で中央に来るよう origin_x を計算する
```

<details>
<summary>コードを見る</summary>

```python
# tetris_game.py
def __init__(self):
    ...
    self.next_piece    = self._spawn_piece()
    self.current_piece = self._pop_next()   # next から取り出す

def _pop_next(self):
    piece           = self.next_piece
    self.next_piece = self._spawn_piece()   # 次を補充
    return piece
```

```python
# config.py
MINI_CELL = 18
PANEL_X   = COLS * CELL_SIZE   # 300
WIDTH     = 420                 # 300 + 120 (サイドパネル)
```

```python
# tetris_renderer.py
def _draw_mini_piece(self, shape, color, origin_x, origin_y):
    for row_idx, row in enumerate(shape):
        for col_idx, cell in enumerate(row):
            if cell:
                x    = origin_x + col_idx * MINI_CELL
                y    = origin_y + row_idx * MINI_CELL
                rect = pg.Rect(x, y, MINI_CELL, MINI_CELL)
                pg.draw.rect(self.screen, color, rect)
                pg.draw.rect(self.screen, GRAY, rect, 1)

def _draw_panel(self, game):
    panel_cx = PANEL_X + (WIDTH - PANEL_X) // 2   # パネル中央 X
    pg.draw.line(self.screen, GRAY, (PANEL_X, 0), (PANEL_X, HEIGHT), 1)

    label = self.font.render("NEXT", True, WHITE)
    self.screen.blit(label, label.get_rect(centerx=panel_cx, y=20))

    shape    = game.next_piece.shape
    color    = game.next_piece.color
    origin_x = PANEL_X + (WIDTH - PANEL_X - len(shape[0]) * MINI_CELL) // 2
    self._draw_mini_piece(shape, color, origin_x, 50)
```

</details>

---

# 発展2 — スコア表示

サンプル: [game/tetris_game.py](game/tetris_game.py)

消去ライン数に応じて点数を加算する。まとめて消すほど高得点になる。

| 消去ライン数 | 点数 |
| --- | --- |
| 1 | 100 |
| 2 | 300 |
| 3 | 500 |
| 4（テトリス） | 800 |

## やること

```
step1. config.py に SCORE_TABLE を追加する
         SCORE_TABLE = [0, 100, 300, 500, 800]
         インデックスが消去ライン数に対応する

step2. TetrisGame に self.score = 0 を追加する

step3. _clear_lines() でライン消去後に score を加算する
         cleared の値を SCORE_TABLE のインデックスとして使う
         cleared が 4 を超えないようインデックスを制限する

step4. Renderer の _draw_panel() にスコアとライン数の表示を追加する
         font.render() でテキストを作り screen.blit() で描画する
```

<details>
<summary>コードを見る</summary>

```python
# config.py
SCORE_TABLE = [0, 100, 300, 500, 800]
```

```python
# tetris_game.py
def _clear_lines(self):
    new_grid = []
    cleared  = 0
    for row in self.grid:
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
    self.grid = new_grid

    self.total_lines += cleared

    if cleared > 0:
        idx = cleared
        if idx >= len(SCORE_TABLE):
            idx = len(SCORE_TABLE) - 1
        self.score += SCORE_TABLE[idx]   # スコア加算

    # 落下速度の更新
    new_interval = FALL_INTERVAL_INIT - (self.total_lines // FALL_SPEED_STEP_LINES) * FALL_SPEED_STEP_MS
    if new_interval < self.min_interval:
        new_interval = self.min_interval
    self.fall_interval = new_interval
```

```python
# tetris_renderer.py（_draw_panel 内）
label = self.font.render("SCORE", True, WHITE)
self.screen.blit(label, label.get_rect(centerx=panel_cx, y=320))
val = self.font.render(str(game.score), True, WHITE)
self.screen.blit(val, val.get_rect(centerx=panel_cx, y=350))

label = self.font.render("LINES", True, WHITE)
self.screen.blit(label, label.get_rect(centerx=panel_cx, y=400))
val = self.font.render(str(game.total_lines), True, WHITE)
self.screen.blit(val, val.get_rect(centerx=panel_cx, y=430))
```

</details>

---

# 発展3 — ホールド機能

サンプル: [game/tetris_game.py](game/tetris_game.py)

H キーで現在のピースを退避しておき、後で呼び出せる。同じピースを持っているあいだは再ホールドできない。

```
現在ピース → [H キー] → ホールドに退避
                       ↓
            ホールドが空なら next_piece を昇格
            ホールドにピースがあれば current と swap
```

## やること

```
step1. Tetrimino に kind 属性を追加する
         __init__(self, shape, color, x, y, kind="") に引数を追加する
         self.kind = kind で保持する
         _spawn_piece() で kind を渡すようにする

step2. TetrisGame に hold_kind と can_hold を追加する
         self.hold_kind = None   退避中のミノ種類（"I" / "O" 等）
         self.can_hold  = True   同じピース中に1回しかホールドできない

step3. _do_hold() メソッドを作る
         can_hold が False なら何もしない
         hold_kind が None のとき
           hold_kind = current.kind で退避する
           current = _pop_next() で次のピースに切り替える
         hold_kind にピースがあるとき
           old_hold = hold_kind を保存する
           hold_kind = current.kind に更新する
           current = _make_piece(old_hold) で退避ピースを復元する
         can_hold = False にして再ホールドを禁止する

step4. _make_piece(kind) メソッドを作る
         TETRIMINO_SHAPES[kind] から shape と color を取得する
         Tetrimino を新しく作って spawn_tetrimino() で位置を設定して返す

step5. ピースが着地したとき（update 内）can_hold = True に戻す

step6. handle_input() に K_h の処理を追加して _do_hold() を呼ぶ

step7. Renderer の _draw_panel() に HOLD プレビューを追加する
         hold_kind が None のときは "H key" と表示する
         can_hold が False のときはピースを GRAY で暗く描画する
```

<details>
<summary>コードを見る</summary>

```python
# game/tetrimino.py（kind 追加）
class Tetrimino:
    def __init__(self, shape, color, x, y, kind=""):
        self.shape = shape
        self.color = color
        self.x     = x
        self.y     = y
        self.kind  = kind
```

```python
# tetris_game.py
def _make_piece(self, kind):
    data = TETRIMINO_SHAPES[kind]
    shape_copy = []
    for row in data["shape"]:
        shape_copy.append(row[:])
    piece = Tetrimino(
        shape=shape_copy,
        color=data["color"],
        x=0, y=0,
        kind=kind,
    )
    piece.spawn_tetrimino(COLS)
    return piece

def _do_hold(self):
    if not self.can_hold:
        return
    if self.hold_kind is None:
        self.hold_kind     = self.current_piece.kind
        self.current_piece = self._pop_next()
    else:
        old_hold       = self.hold_kind
        self.hold_kind = self.current_piece.kind
        self.current_piece = self._make_piece(old_hold)
    self.can_hold = False
    if not self.current_piece.can_move(0, 0, self.grid, ROWS, COLS):
        self.game_over = True

def update(self):
    ...
    else:
        self.current_piece.lock(self.grid)
        self._clear_lines()
        self.can_hold      = True        # ホールド権を回復
        self.current_piece = self._pop_next()
        ...

def handle_input(self, event):
    ...
    elif event.key == pg.K_h:
        self._do_hold()
```

```python
# tetris_renderer.py（_draw_panel 内）
label = self.font.render("HOLD", True, WHITE)
self.screen.blit(label, label.get_rect(centerx=panel_cx, y=170))

if game.hold_kind is not None:
    shape  = TETRIMINO_SHAPES[game.hold_kind]["shape"]
    color  = TETRIMINO_SHAPES[game.hold_kind]["color"]
    if not game.can_hold:
        color = GRAY   # ホールド使用済みは暗くする
    origin_x = PANEL_X + (WIDTH - PANEL_X - len(shape[0]) * MINI_CELL) // 2
    self._draw_mini_piece(shape, color, origin_x, 200)
else:
    hint = self.font.render("H key", True, GRAY)
    self.screen.blit(hint, hint.get_rect(centerx=panel_cx, y=205))
```

</details>

---

# 発展4 — ゴーストピース

サンプル: [game/tetris_renderer.py](game/tetris_renderer.py)

現在のピースが落下したときの着地位置を枠線だけで表示する。

## やること

```
step1. _calc_ghost_dy(piece, grid) メソッドを作る
         dy = 0 から始めて、can_move(0, dy+1, ...) が True のあいだ dy を増やす
         dy がゴーストの落下オフセット（何マス下か）になる

step2. _draw_ghost(piece, grid) メソッドを作る
         dy = _calc_ghost_dy() で落下距離を取得する
         dy == 0（すでに着地直前）のときは描画しない
         piece.shape の二重ループで cell == 1 のマスについて
           y = (piece.y + dy + row_idx) * CELL_SIZE でゴーストの Y 座標を計算する
           pg.draw.rect(..., piece.color, rect, 2) で枠線のみ描画する

step3. draw() の中でゴーストを実ピースより前に描画する
         _draw_ghost() → _draw_tetrimino() の順にすることで
         実ピースがゴーストの上に重なって表示される
```

<details>
<summary>コードを見る</summary>

```python
# tetris_renderer.py
def _calc_ghost_dy(self, piece, grid):
    dy = 0
    while piece.can_move(0, dy + 1, grid, ROWS, COLS):
        dy += 1
    return dy

def _draw_ghost(self, piece, grid):
    dy = self._calc_ghost_dy(piece, grid)
    if dy == 0:
        return
    for row_idx, row in enumerate(piece.shape):
        for col_idx, cell in enumerate(row):
            if cell:
                x    = (piece.x + col_idx) * CELL_SIZE
                y    = (piece.y + dy + row_idx) * CELL_SIZE
                rect = pg.Rect(x, y, CELL_SIZE, CELL_SIZE)
                pg.draw.rect(self.screen, piece.color, rect, 2)  # 枠線のみ

def draw(self, game):
    self.screen.fill(BLACK)
    self._draw_grid(game.grid)
    self._draw_ghost(game.current_piece, game.grid)   # ゴーストを先に描く
    self._draw_tetrimino(game.current_piece)           # 実ピースを上に重ねる
    self._draw_panel(game)
```

</details>
