```text
衝突判定・ゲームオーバー・ゲームクリアを組み合わせてアクションゲームを作りましょう
```

# 目次
- [キャラクタを動かす](#キャラクタを動かす)
- [衝突判定](#衝突判定)
  - [1つのRectとの衝突: colliderect](#1つのrectとの衝突-colliderect)
  - [複数のRectとの衝突: collidelist](#複数のrectとの衝突-collidelist)
- [罠をばら撒く](#罠をばら撒く)
- [ゲームオーバー](#ゲームオーバー)
- [ゲームクリア](#ゲームクリア)
- [追いかけてくる敵](#追いかけてくる敵)

---

# キャラクタを動かす

サンプル: [example/ex01.py](example/ex01.py)

```python
## プレイヤーデータ
PLAYER_SIZE  = (40, 50)
PLAYER_SPEED = 4
myimgR = pg.image.load(IMG_DIR / "playerR.png")
myimgR = pg.transform.scale(myimgR, PLAYER_SIZE)
myimgL = pg.transform.flip(myimgR, True, False)  # 左右反転した画像
myrect = myimgR.get_rect(topleft=(50, 200))

rightFlag = True  # True: 右向き / False: 左向き
```

キーが押されたら速度(vx, vy)を変化させ、毎フレーム座標に加算する

```python
vx = 0
vy = 0
key = pg.key.get_pressed()

if key[pg.K_RIGHT]:
    vx = PLAYER_SPEED
    rightFlag = True
if key[pg.K_LEFT]:
    vx = -PLAYER_SPEED
    rightFlag = False

myrect.x += vx
myrect.y += vy
```

---

# 衝突判定

## 1つのRectとの衝突: colliderect

サンプル: [example/ex02.py](example/ex02.py)

```python
myrect.x += vx
myrect.y += vy
if myrect.colliderect(boxrect):  # 衝突したら
    myrect.x -= vx               # 移動を戻す
    myrect.y -= vy
```

| 戻り値 | 意味 |
| --- | --- |
| `True` | 衝突している |
| `False` | 衝突していない |

## 複数のRectとの衝突: collidelist

サンプル: [example/ex03.py](example/ex03.py)

```python
WALL_THICKNESS = 20
walls = [pg.Rect(0, 0, WIDTH, WALL_THICKNESS),                       # 上
         pg.Rect(0, 0, WALL_THICKNESS, HEIGHT),                      # 左
         pg.Rect(WIDTH - WALL_THICKNESS, 0, WALL_THICKNESS, HEIGHT), # 右
         pg.Rect(0, HEIGHT - WALL_THICKNESS, WIDTH, WALL_THICKNESS)] # 下

if myrect.collidelist(walls) != -1:  # いずれかと衝突したら
    myrect.x -= vx
    myrect.y -= vy
```

`WIDTH` / `HEIGHT` はステップ1で `pg.display.set_mode((WIDTH, HEIGHT))` に使った画面サイズの定数（[01_window](../01_window/README.md)を参照）。壁の位置を `800` や `600` と直接書く代わりにこれらを使うと、画面サイズを変えても壁の位置がずれない。

| 戻り値 | 意味 |
| --- | --- |
| `0以上の整数` | 衝突したRectのインデックス |
| `-1` | 衝突なし |

---

# 罠をばら撒く

サンプル: [example/ex04.py](example/ex04.py)

`random.randint()` でY座標をランダムに決めてリストに追加する

```python
import random

TRAP_COUNT   = 20
TRAP_SPACING = 30
TRAP_SIZE    = (30, 30)
TRAP_START_X = 150
TRAP_Y_MIN   = 20
TRAP_Y_MAX   = 550

traps = []
for i in range(TRAP_COUNT):
    wx = TRAP_START_X + i * TRAP_SPACING
    wy = random.randint(TRAP_Y_MIN, TRAP_Y_MAX)  # Y座標はランダム
    traps.append(pg.Rect(wx, wy, *TRAP_SIZE))
```

描画はfor文でまとめて行う

```python
for trap in traps:
    screen.blit(trapimg, trap)
```

---

# ゲームオーバー

サンプル: [example/ex05.py](example/ex05.py)

罠と衝突したらページ2(ゲームオーバー画面)に切り替える

```python
if myrect.collidelist(traps) != -1:
    pg.mixer.Sound(SND_DIR / "pi.wav").play()
    page = 2
```

ゲームオーバー画面ではデータをリセットしてリプレイボタンを表示する

```python
REPLAY_BTN_POS   = (320, 480)
RESULT_FONT_SIZE = 150

def gamereset():
    myrect.x = 50
    myrect.y = 100
    for d in range(TRAP_COUNT):
        traps[d].x = TRAP_START_X + d * TRAP_SPACING
        traps[d].y = random.randint(TRAP_Y_MIN, TRAP_Y_MAX)

def gameover():
    gamereset()
    screen.fill(pg.Color("NAVY"))
    font = pg.font.Font(None, RESULT_FONT_SIZE)
    text = font.render("GAMEOVER", True, pg.Color("RED"))
    screen.blit(text, (100, 200))
    btn1 = screen.blit(replay_img, REPLAY_BTN_POS)
    button_to_jump(btn1, 1)  # リプレイボタンでページ1へ
```

---

# ゲームクリア

サンプル: [example/ex06.py](example/ex06.py)

ゴール(金色のRect)に触れたらページ3(ゲームクリア画面)に切り替える

```python
goalrect = pg.Rect(750, 250, 30, 100)

pg.draw.rect(screen, pg.Color("GOLD"), goalrect)
if myrect.colliderect(goalrect):
    pg.mixer.Sound(SND_DIR / "up.wav").play()
    page = 3
```

---

# 追いかけてくる敵

サンプル: [example/ex07.py](example/ex07.py)

毎フレーム、プレイヤーの方向に`ENEMY_SPEED`ずつ近づく

```python
ENEMY_SPEED = 1

if enemyrect.x < myrect.x:  # プレイヤーの方向に近づく
    ovx = ENEMY_SPEED
else:
    ovx = -ENEMY_SPEED
if enemyrect.y < myrect.y:
    ovy = ENEMY_SPEED
else:
    ovy = -ENEMY_SPEED
enemyrect.x += ovx
enemyrect.y += ovy
```

向きに応じて左右の画像を使い分ける

```python
if ovx > 0:
    screen.blit(enemyimgR, enemyrect)
else:
    screen.blit(enemyimgL, enemyrect)
```
