```text
マウスで自機を操作し、弾を撃ってUFOを倒すシューティングゲームを作りましょう
```

# 目次
- [出発点 — 自機と弾を動かす](#出発点--自機と弾を動かす)
- [ex02 — UFOを降らせる](#ex02--ufoを降らせる)
- [ex03 — ゲームオーバーを作る](#ex03--ゲームオーバーを作る)
- [ex04 — 弾でUFOを撃ち落とす](#ex04--弾でufoを撃ち落とす)
- [ex05 — スコアを追加する](#ex05--スコアを追加する)

---

# 出発点 — 自機と弾を動かす

サンプル: [example/ex01.py](example/ex01.py)

マウスで自機を操作し、左クリックで弾を発射する。弾は1発だけ飛ばせる。

## やること

```
step1. SHIP_SIZE = 50 を定義し、myrect = pg.Rect(400, 500, SHIP_SIZE, SHIP_SIZE) で自機の初期位置を設定する
step2. gamestage() の中でマウスの x 座標を取得して自機を動かす
         myrect.x = mx - SHIP_SIZE // 2  （中心をマウスに合わせるために自機幅の半分を引く）
step3. BULLET_SIZE = 16 / OFFSCREEN_Y = -100 を定義し、
         bulletrect = pg.Rect(400, OFFSCREEN_Y, BULLET_SIZE, BULLET_SIZE) で弾を画面外に待機させる
step4. 左クリック かつ bulletrect.y < 0（待機中）のときだけ弾を発射する
         bulletrect.x = myrect.x + SHIP_SIZE // 2 - BULLET_SIZE // 2  （自機の中心から発射）
         bulletrect.y = myrect.y
step5. bulletrect.y >= 0（発射中）のあいだ毎フレーム上へ移動させる
         BULLET_SPEED = 15 を定義し、bulletrect.y -= BULLET_SPEED
```

<details>
<summary>コードを見る</summary>

```python
SHIP_SIZE = 50
BULLET_SIZE = 16
BULLET_SPEED = 15
OFFSCREEN_Y = -100

myrect    = pg.Rect(400, 500, SHIP_SIZE, SHIP_SIZE)
bulletrect = pg.Rect(400, OFFSCREEN_Y, BULLET_SIZE, BULLET_SIZE)

def gamestage():
    (mx, _) = pg.mouse.get_pos()
    mdown = pg.mouse.get_pressed()

    myrect.x = mx - SHIP_SIZE // 2
    screen.blit(myimg, myrect)

    if mdown[0] and bulletrect.y < 0:
        bulletrect.x = myrect.x + SHIP_SIZE // 2 - BULLET_SIZE // 2
        bulletrect.y = myrect.y
        pg.mixer.Sound(SOUND_DIR / "pi.wav").play()
    if bulletrect.y >= 0:
        bulletrect.y -= BULLET_SPEED
        screen.blit(bulletimg, bulletrect)
```

</details>

---

# ex02 — UFOを降らせる

サンプル: [example/ex02.py](example/ex02.py)

UFOを10体リストで管理して、上から次々と降らせる。

## やること

```
step1. UFO_SIZE=50 / UFO_COUNT=10 / UFO_SPEED=10 を定義する
         ufos リストを作り、UFO_COUNT 体分の pg.Rect を追加する
         縦に OFFSCREEN_Y * i ずつずらして配置することで、一度に出現しないようにする

step2. gamestage() の中で for ufo in ufos: を回す
         ufo.y += UFO_SPEED  で毎フレーム下へ移動させる
         ufo.y > HEIGHT になったら画面上部（y = OFFSCREEN_Y）に戻す
         screen.blit(ufoimg, ufo) で描画する
```

<details>
<summary>コードを見る</summary>

```python
UFO_SIZE  = 50
UFO_COUNT = 10
UFO_SPEED = 10

ufos = []
for i in range(UFO_COUNT):
    ux = random.randint(0, WIDTH)
    uy = OFFSCREEN_Y * i
    ufos.append(pg.Rect(ux, uy, UFO_SIZE, UFO_SIZE))
```

```python
for ufo in ufos:
    ufo.y += UFO_SPEED
    screen.blit(ufoimg, ufo)
    if ufo.y > HEIGHT:
        ufo.x = random.randint(0, WIDTH)
        ufo.y = OFFSCREEN_Y
```

</details>

---

# ex03 — ゲームオーバーを作る

サンプル: [example/ex03.py](example/ex03.py)

自機とUFOが衝突したらゲームオーバー画面に切り替える。リプレイボタンでリセットして再プレイできる。

## やること

```
step1. page 変数を追加する（1=ゲーム中、2=ゲームオーバー）
step2. UFO の for ループの中で自機との衝突を判定する
         ufo.colliderect(myrect) が True なら page = 2 にする
step3. gameover() 関数を作る
         "GAMEOVER" テキストとリプレイボタンを描画する
         button_to_jump(btn1, 1) でボタンを押したら page = 1 に戻す
step4. gamereset() 関数を作る
         自機・弾・UFO の位置を初期値に戻す
         gameover() の中でページが戻ったタイミングで呼ぶ
step5. メインループを page で分岐させる
         page == 1 → gamestage()
         page == 2 → gameover()
```

`pushFlag` でボタンを押しっぱなしにしたときの連続ページ切り替えを防ぐ

<details>
<summary>コードを見る</summary>

```python
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

```python
# UFOの衝突処理（gamestage 内）
if ufo.colliderect(myrect):
    page = 2
    pg.mixer.Sound(SOUND_DIR / "down.wav").play()
```

```python
REPLAY_BTN_POS   = (320, 480)
RESULT_FONT_SIZE = 150

def gamereset():
    myrect.x = 400
    myrect.y = 500
    bulletrect.y = OFFSCREEN_Y
    for i in range(UFO_COUNT):
        ufos[i] = pg.Rect(random.randint(0, WIDTH), OFFSCREEN_Y * i, UFO_SIZE, UFO_SIZE)

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

# ex04 — 弾でUFOを撃ち落とす

サンプル: [example/ex04.py](example/ex04.py)

弾とUFOが衝突したらUFOを上に戻し、弾も待機状態にリセットする。

## やること

```
step1. UFO の for ループの中に弾との衝突判定を追加する
         ufo.colliderect(bulletrect) が True なら
           ufo を画面外（y = OFFSCREEN_Y）に戻す
           bulletrect.y = OFFSCREEN_Y で弾を待機状態に戻す
           効果音を鳴らす
```

<details>
<summary>コードを見る</summary>

```python
if ufo.colliderect(bulletrect):
    ufo.y = OFFSCREEN_Y
    ufo.x = random.randint(0, WIDTH)
    bulletrect.y = OFFSCREEN_Y
    pg.mixer.Sound(SOUND_DIR / "piko.wav").play()
```

</details>

---

# ex05 — スコアを追加する

サンプル: [example/ex05.py](example/ex05.py)

UFOを撃墜するたびに 10 点加算する。ゲームオーバー画面でも確認できる。

## やること

```
step1. score 変数を追加する（初期値 0）
step2. SCORE_PER_HIT = 10 を定義し、UFO を撃墜したときに score += SCORE_PER_HIT する
step3. gamestage() の中でスコアをテキストとして描画する
         font.render("SCORE:" + str(score), ...) で文字列を作る
step4. gameover() にもスコアの描画を追加する
step5. gamereset() で score = 0 にリセットする
step6. gameover() 内の gamereset() 呼び出しを条件付きにする
         これまでは毎フレーム無条件に gamereset() を呼んでいたが、
         page == 1（ボタンでリプレイに戻った直後）のときだけ呼ぶように変更し、
         ゲームオーバー画面表示中に自機やUFOの位置がリセットされ続けないようにする
```

<details>
<summary>コードを見る</summary>

```python
SCORE_FONT_SIZE = 40
SCORE_POS       = (20, 20)
SCORE_PER_HIT   = 10

# UFO撃墜時（gamestage 内）
if ufo.colliderect(bulletrect):
    score += SCORE_PER_HIT
    ufo.y = OFFSCREEN_Y
    ufo.x = random.randint(0, WIDTH)
    bulletrect.y = OFFSCREEN_Y
    pg.mixer.Sound(SOUND_DIR / "piko.wav").play()
```

```python
# スコア描画（gamestage 内）
font = pg.font.Font(None, SCORE_FONT_SIZE)
text = font.render("SCORE:" + str(score), True, pg.Color("WHITE"))
screen.blit(text, SCORE_POS)
```

```python
def gamereset():
    global score
    score = 0
    myrect.x = 400
    myrect.y = 500
    bulletrect.y = OFFSCREEN_Y
    for i in range(UFO_COUNT):
        ufos[i] = pg.Rect(random.randint(0, WIDTH), OFFSCREEN_Y * i, UFO_SIZE, UFO_SIZE)
```

```python
# gameover 内: gamereset() の呼び出しを条件付きにする
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
