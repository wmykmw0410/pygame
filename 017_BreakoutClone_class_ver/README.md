```text
013_BreakoutClone の関数ベースのコードを、クラスを使って段階的に書き直します
```

# 目次
- [出発点](#出発点)
- [ex02 — Ball クラスにまとめる](#ex02--ball-クラスにまとめる)
- [ex03 — Block クラスを作る](#ex03--block-クラスを作る)
- [ex04 — Bar クラスを作る](#ex04--bar-クラスを作る)
- [ex05 — ボールを複数に増やす](#ex05--ボールを複数に増やす)

---

# 出発点

サンプル: [example/ex01.py](example/ex01.py)

013_BreakoutClone の完成コードをそのまま使う。  
ボール・ブロック・バーのデータが次のようにバラバラに存在している。

```python
# ボールのデータが4つの変数に散らばっている
ballimg  = pg.image.load(...)
ballrect = pg.Rect(400, 450, 30, 30)
vx = random.randint(-10, 10)
vy = -5

# gamestage() の中でも変数を直接操作している
ballrect.x += vx
ballrect.y += vy
screen.blit(ballimg, ballrect)
```

→ 変数が増えるほど管理が大変になる。次のステップでクラスにまとめていく。

---

# ex02 — Ball クラスにまとめる

サンプル: [example/ex02.py](example/ex02.py)

## やること

`ballrect / vx / vy / ballimg` という4つのバラバラな変数を `Ball` クラスに集約する。

```
step1. Ball クラスを定義する
         __init__(self, img) でプロパティを設定する
           self.img  = img
           self.rect = pg.Rect(400, 450, 30, 30)
           self.vx   = random.randint(-10, 10)
           self.vy   = -5

step2. 以下のメソッドを追加する
         bounce_wall()       壁に当たったら vx / vy を反転する
         bounce_bar(barrect) バーに当たったら vx / vy を更新する
         move()              rect.x と rect.y を vx / vy 分動かす
         draw()              screen.blit(self.img, self.rect) で描画する
         is_out()            rect.y > 600 なら True を返す
         reset()             rect と vx / vy を初期値に戻す

step3. グローバル変数の ballrect / vx / vy を削除し、
       ball = Ball(ballimg) に置き換える

step4. gamestage() を書き直す
         ball.bounce_wall() / ball.bounce_bar(barrect)
         ball.move() / ball.draw() / ball.is_out() を使う
```

<details>
<summary>コードを見る</summary>

```python
class Ball():
    def __init__(self, img):
        self.img  = img
        self.rect = pg.Rect(400, 450, 30, 30)
        self.vx   = random.randint(-10, 10)
        self.vy   = -5

    def bounce_wall(self):
        if self.rect.y < 0:
            self.vy = -self.vy
        if self.rect.x < 0 or self.rect.x > 800 - 30:
            self.vx = -self.vx

    def bounce_bar(self, barrect):
        if barrect.colliderect(self.rect):
            self.vx = int(((self.rect.x + 15) - (barrect.x + 50)) / 4)
            self.vy = random.randint(-10, -5)
            pg.mixer.Sound(SND_DIR / "pi.wav").play()

    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

    def draw(self):
        screen.blit(self.img, self.rect)

    def is_out(self):
        return self.rect.y > 600

    def reset(self):
        self.rect.x = 400
        self.rect.y = 450
        self.vx = random.randint(-10, 10)
        self.vy = -5
```

```python
# gamestage() のボール処理
ball.bounce_wall()
ball.bounce_bar(barrect)
if ball.is_out():
    page = 2
    pg.mixer.Sound(SND_DIR / "pi.wav").play()
ball.move()
ball.draw()
```

</details>

---

# ex03 — Block クラスを作る

サンプル: [example/ex03.py](example/ex03.py)

## やること

ブロックを `pg.Rect` のリストから `Block` クラスのリストに変換する。  
「消えているかどうか」を `active` フラグで管理し、当たり判定を `check_hit()` に持たせる。

```
step1. Block クラスを定義する
         __init__(self, x, y) でプロパティを設定する
           self.rect   = pg.Rect(x, y, 80, 30)
           self.active = True   ← 生存フラグ

step2. 以下のメソッドを追加する
         draw()              active が True のときだけ描画する
         check_hit(ball)     active かつ ball.rect と重なっていたら
                               self.active = False にして
                               ball.vy を反転し True を返す
                               当たっていなければ False を返す

step3. make_blocks() 関数を書き直す
         pg.Rect(...) の代わりに Block(...) をリストに入れる

step4. gamestage() のブロック処理を書き直す
         block.draw() と block.check_hit(ball) を使う
         for n, block in enumerate(blocks) は不要になる
```

<details>
<summary>コードを見る</summary>

```python
class Block():
    def __init__(self, x, y):
        self.rect   = pg.Rect(x, y, 80, 30)
        self.active = True

    def draw(self):
        if self.active:
            pg.draw.rect(screen, pg.Color("GOLD"), self.rect)

    def check_hit(self, ball):
        if self.active and self.rect.colliderect(ball.rect):
            self.active = False
            ball.vy = -ball.vy
            pg.mixer.Sound(SND_DIR / "piko.wav").play()
            return True
        return False
```

```python
def make_blocks():
    result = []
    for yy in range(4):
        for xx in range(7):
            result.append(Block(50 + xx * 100, 40 + yy * 50))
    return result

blocks = make_blocks()
```

```python
# gamestage() のブロック処理
for block in blocks:
    block.draw()
    if block.check_hit(ball):
        score += 1
        if score == 28:
            pg.mixer.Sound(SND_DIR / "up.wav").play()
            page = 3
```

</details>

---

# ex04 — Bar クラスを作る

サンプル: [example/ex04.py](example/ex04.py)

## やること

バーも `Bar` クラスにまとめ、`Ball` / `Block` / `Bar` の3クラス構成を完成させる。  
あわせて `Block` に `color` プロパティを追加して行ごとに色を変える。

```
step1. Bar クラスを定義する
         __init__(self) で self.rect = pg.Rect(400, 500, 100, 20) を設定する
         update(self, mx) で self.rect.x = mx - 50 にする
         draw(self) で pg.draw.rect(...) を描画する

step2. グローバル変数の barrect を削除し、
       bar = Bar() に置き換える

step3. gamestage() を書き直す
         barrect.x = mx - 50 → bar.update(mx)
         pg.draw.rect(..., barrect) → bar.draw()
         ball.bounce_bar(barrect) → ball.bounce_bar(bar)
         bounce_bar() の引数も barrect → bar.rect に変更する

step4. Block に color を追加する
         __init__(self, x, y, color) に引数を追加し self.color = color を設定する
         draw() で pg.Color("GOLD") の代わりに self.color を使う

step5. ROW_COLORS リストを定義し、make_blocks() で行番号に応じて色を渡す
         ROW_COLORS = ["RED", "ORANGE", "YELLOW", "GREEN"]
         color = pg.Color(ROW_COLORS[yy]) を Block に渡す
```

<details>
<summary>コードを見る</summary>

```python
class Bar():
    def __init__(self):
        self.rect = pg.Rect(400, 500, 100, 20)

    def update(self, mx):
        self.rect.x = mx - 50

    def draw(self):
        pg.draw.rect(screen, pg.Color("CYAN"), self.rect)
```

```python
ROW_COLORS = ["RED", "ORANGE", "YELLOW", "GREEN"]

class Block():
    def __init__(self, x, y, color):
        self.rect   = pg.Rect(x, y, 80, 30)
        self.color  = color
        self.active = True

    def draw(self):
        if self.active:
            pg.draw.rect(screen, self.color, self.rect)

    def check_hit(self, ball):
        if self.active and self.rect.colliderect(ball.rect):
            self.active = False
            ball.vy = -ball.vy
            pg.mixer.Sound(SND_DIR / "piko.wav").play()
            return True
        return False
```

```python
def make_blocks():
    result = []
    for yy in range(4):
        color = pg.Color(ROW_COLORS[yy])
        for xx in range(7):
            result.append(Block(50 + xx * 100, 40 + yy * 50, color))
    return result
```

```python
# gamestage() のバー処理
bar.update(mx)
bar.draw()
```

</details>

---

# ex05 — ボールを複数に増やす

サンプル: [example/ex05.py](example/ex05.py)

## やること

`ball` 1個を `balls` リストに変えて、複数の Ball インスタンスを管理する。  
画面外に出たボールをリストから除いて、全滅でゲームオーバーにする。

```
step1. Ball.__init__ に x 引数を追加する
         self.rect = pg.Rect(x, 450, 30, 30) にして開始位置を変えられるようにする

step2. make_balls() 関数を作る
         Ball インスタンスを3個（x=200 / 400 / 600）リストに入れて返す

step3. ball = Ball(...) を balls = make_balls() に置き換える

step4. gamestage() のボール処理を書き直す
         for ball in balls: でリストを回す
         alive_balls リストを用意して is_out() が False のボールだけ追加する
         ループ後に balls = alive_balls で上書きする
         len(balls) == 0 になったらゲームオーバーにする

step5. ブロックの当たり判定を for ball in balls: で全ボール分チェックする

step6. gamereset() で balls = make_balls() に書き直す
```

<details>
<summary>コードを見る</summary>

```python
def make_balls():
    result = []
    result.append(Ball(ballimg, 200))
    result.append(Ball(ballimg, 400))
    result.append(Ball(ballimg, 600))
    return result

balls = make_balls()
```

```python
# gamestage() のボール処理
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

```python
# ブロックの当たり判定（全ボール分チェック）
for block in blocks:
    block.draw()
    for ball in balls:
        if block.check_hit(ball):
            score += 1
            if score == 28:
                pg.mixer.Sound(SND_DIR / "up.wav").play()
                page = 3
```

</details>
