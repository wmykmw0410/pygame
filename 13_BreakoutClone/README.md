```text
バーでボールを打ち返し、ブロックを全て壊すブロック崩しゲームを作りましょう
```

# 目次
- [出発点 — バーとボールを動かす](#出発点--バーとボールを動かす)
- [ex02 — ゲームオーバーを作る](#ex02--ゲームオーバーを作る)
- [ex03 — ブロックを並べる](#ex03--ブロックを並べる)

---

# 出発点 — バーとボールを動かす

サンプル: [example/ex01.py](example/ex01.py)

マウスでバーを操作し、ボールを打ち返す。

## やること

```
step1. BAR_SIZE = (100, 20) を定義し、barrect = pg.Rect(400, 500, *BAR_SIZE) でバーの初期位置を設定する
step2. gamestage() の中でマウスの x 座標を取得してバーを動かす
         barrect.x = mx - BAR_SIZE[0] // 2  （中心をマウスに合わせるためにバー幅の半分を引く）
step3. vx / vy でボールの速度を設定する
         vx = random.randint(*INITIAL_VX_RANGE)  （左右のランダムな速度、範囲は(-10, 10)）
         vy = INITIAL_VY  （初速は上向き、-5）
step4. ボールの跳ね返り処理を書く
         上壁（y < 0）: vy を反転する
         左右壁（x < 0 または x > WIDTH - BALL_SIZE）: vx を反転する
         バーに当たったとき: vy をランダムな上向きに、
           vx は当たった位置で角度を変える
step5. ballrect.x += vx / ballrect.y += vy でボールを移動させる
```

<details>
<summary>コードを見る</summary>

```python
BAR_SIZE = (100, 20)
BALL_SIZE = 30
INITIAL_VX_RANGE = (-10, 10)
INITIAL_VY = -5
BOUNCE_VY_RANGE = (-10, -5)

barrect  = pg.Rect(400, 500, *BAR_SIZE)
ballrect = pg.Rect(400, 450, BALL_SIZE, BALL_SIZE)
vx = random.randint(*INITIAL_VX_RANGE)
vy = INITIAL_VY

def gamestage():
    global vx, vy
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
    ballrect.x += vx
    ballrect.y += vy
    screen.blit(ballimg, ballrect)
```

</details>

---

# ex02 — ゲームオーバーを作る

サンプル: [example/ex02.py](example/ex02.py)

ボールが画面下に出たらゲームオーバー画面に切り替える。リプレイボタンでリセットして再プレイできる。

## やること

```
step1. page 変数を追加する（1=ゲーム中、2=ゲームオーバー）
step2. gamestage() の中でボールが y > HEIGHT になったら page = 2 にする
step3. gamereset() 関数を作る
         vx / vy を初期値に戻す
         ballrect の位置を初期値に戻す
step4. gameover() 関数を作る
         gamereset() を呼んでデータをリセットする
         "GAMEOVER" テキストとリプレイボタンを描画する
         button_to_jump(btn1, 1) でボタンを押したら page = 1 に戻す
step5. メインループを page で分岐させる
         page == 1 → gamestage()
         page == 2 → gameover()
```

<details>
<summary>コードを見る</summary>

```python
# ボールが落ちたらゲームオーバー（gamestage 内）
if ballrect.y > HEIGHT:
    page = 2
    pg.mixer.Sound(SND_DIR / "down.wav").play()
```

```python
REPLAY_BTN_POS   = (320, 480)
RESULT_FONT_SIZE = 150

def gamereset():
    global vx, vy
    vx = random.randint(*INITIAL_VX_RANGE)
    vy = INITIAL_VY
    ballrect.x = 400
    ballrect.y = 450

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

---

# ex03 — ブロックを並べる

サンプル: [example/ex03.py](example/ex03.py)

二重ループでブロックを4行×7列 = 28個並べる。ボールが当たったブロックを消してスコアを増やし、全消しでゲームクリアにする。

## やること

```
step1. 二重ループで blocks リストに pg.Rect を28個追加する
         xx（列）と yy（行）の値で座標を計算する
step2. gamestage() の中で for n, block in enumerate(blocks): を回す
         pg.draw.rect(..., block) で描画する
         block.colliderect(ballrect) が True なら
           vy を反転してボールを跳ね返す
           blocks[n] = pg.Rect(0, 0, 0, 0) でブロックを消す
           score += 1 でスコアを増やす
           score == BLOCK_ROWS * BLOCK_COLS（28）になったら page = 3（ゲームクリア）にする
step3. gameclear() 関数を作る
         gameover() と同様に画面を描画し、リプレイボタンを表示する
step4. gamereset() に score と blocks のリセットを追加する
step5. メインループに page == 3 → gameclear() の分岐を追加する
```

<details>
<summary>コードを見る</summary>

```python
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

```python
# ブロックの処理（gamestage 内）
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

```python
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
