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

サンプル: [example/ex01.py](example/ex01.py)

練習: [practice/practice01.py](practice/practice01.py)（「# ★」の部分が空欄になっているので、サンプルを見ながら自分の手でコードを打ち込んで完成させよう。サンプルは前のサンプルに少しずつ足していく作りなので、練習2以降は、前の練習で作った部分が最初から書いてあり、新しく習う部分だけが空欄になっている。画像や音は `pathlib` で読み込んでいる → [08_pathlib_module](../08_pathlib_module/README.md)）

動いたら、書き換えてもう一度動かし、変化を確認する。

| 試すこと | 確認すること |
| --- | --- |
| `PLAYER_SPEED` の `4` → `1` / `10` | 数が大きいほど速く動く（1フレームで動くピクセル数） |
| 右キーと上キーを同時に押す | 右上へ斜めに動く（`vx` と `vy` が、毎フレーム両方足される） |
| 左キーを押してから離す | 左向きのまま止まる（`rightFlag` が、最後に向いていた方向を覚えている） |
| 緑の四角の上を通る | 何も起きず、すり抜ける（まだ衝突判定をしていないため） |
| `PLAYER_SIZE` の `(40, 50)` → `(80, 100)` | キャラクタが大きく表示され、`myrect` の大きさも変わる |

---

# 衝突判定

## 1つのRectとの衝突: colliderect

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

サンプル: [example/ex02.py](example/ex02.py)

練習: [practice/practice02.py](practice/practice02.py)

| 試すこと | 確認すること |
| --- | --- |
| 右キーを押し続けて緑の四角にぶつける | 四角の左ぎりぎりで止まる（ぶつかった分の移動が取り消されるため） |
| 戻す2行（`myrect.x -= vx` と `myrect.y -= vy`）をどちらも消す | 四角をすり抜ける（衝突を調べても、何も起きない） |
| `myrect.x -= vx` の行だけ消す | 右キーでは四角をすり抜ける（横の移動が戻らない）。上下キーでは、今までどおり止まる |
| `myrect.y -= vy` の行だけ消す | 上下キーでは四角をすり抜ける（縦の移動が戻らない）。右キーでは、今までどおり止まる |
| `boxrect = pg.Rect(300, 200, 100, 100)` の数字 | 緑の四角の位置と大きさが変わる |

## 複数のRectとの衝突: collidelist

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

サンプル: [example/ex03.py](example/ex03.py)

練習: [practice/practice03.py](practice/practice03.py)

| 試すこと | 確認すること |
| --- | --- |
| 4つの壁にぶつかるまで進む | どの壁でも移動が戻されるので、画面の外には出られない |
| `WALL_THICKNESS` の `20` → `40` | 壁が厚くなり、動ける範囲が狭くなる（左端で止まる位置が `x = 22` から `x = 42` に変わる） |
| `WALL_THICKNESS` → `100` | 最初の位置（`x = 50`）が壁の中になり、移動を戻しても壁の中のままなので、動けなくなる |
| 下の壁（4つ目の `Rect`）をリストから消す | 下に進み続けると、画面の外に出ていく |
| `if` の前に `print(myrect.collidelist(walls))` を足す | ぶつかっていないときは `-1`、ぶつかったときは壁の番号（リストの順に、上 `0`・左 `1`・右 `2`・下 `3`）が表示される |

---

# 罠をばら撒く

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

サンプル: [example/ex04.py](example/ex04.py)

練習: [practice/practice04.py](practice/practice04.py)

| 試すこと | 確認すること |
| --- | --- |
| プログラムを何回か実行し直す | 罠のY座標が毎回変わる（`random.randint()` でランダムに決めているため） |
| `TRAP_COUNT` の `20` → `5` / `40` | 罠の数が変わる。`40` だと、右側の罠が画面の外（`x` が `800` 以上）にはみ出す |
| `TRAP_SPACING` の `30` → `60` | 罠の間隔が広がり、右側の罠が画面の外にはみ出す |
| `TRAP_Y_MIN` と `TRAP_Y_MAX` → `100` と `150` | 罠が、Y座標 `100`〜`150` の帯の中に並ぶ |
| 罠の上を通る | 何も起きない（まだ、罠との衝突判定をしていないため） |

---

# ゲームオーバー

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

サンプル: [example/ex05.py](example/ex05.py)

練習: [practice/practice05.py](practice/practice05.py)

| 試すこと | 確認すること |
| --- | --- |
| 罠に触れる | ゲームオーバー画面（青い背景に `GAMEOVER` とリプレイボタン）に切り替わる |
| リプレイボタンを押す | ページ1に戻る。`gamereset()` が、プレイヤーを最初の位置に戻し、罠の位置をランダムに決め直す |
| `RESULT_FONT_SIZE` の `150` → `50` / `250` | 数が大きいほど、大きな文字になる |
| `REPLAY_BTN_POS` → `(100, 100)` | ボタンの表示位置が変わり、反応する場所も一緒に変わる |
| `gameover()` の中の `gamereset()` の行を消す | リプレイボタンを押しても、プレイヤーが罠に触れた位置から再開するので、すぐゲームオーバー画面に戻ってしまう |

---

# ゲームクリア

ゴール(金色のRect)に触れたらページ3(ゲームクリア画面)に切り替える

```python
goalrect = pg.Rect(750, 250, 30, 100)

pg.draw.rect(screen, pg.Color("GOLD"), goalrect)
if myrect.colliderect(goalrect):
    pg.mixer.Sound(SND_DIR / "up.wav").play()
    page = 3
```

サンプル: [example/ex06.py](example/ex06.py)

練習: [practice/practice06.py](practice/practice06.py)

| 試すこと | 確認すること |
| --- | --- |
| ゴールの金色の四角に触れる | ゲームクリア画面（金色の背景に `GAMECLEAR` とリプレイボタン）に切り替わる |
| `goalrect = pg.Rect(750, 250, 30, 100)` の数字 | ゴールの位置と大きさが変わる |
| `GOLD` や、文字の色 `RED` を別の色に変える | 指定した部分（ゴール、またはクリア画面の背景・文字）の色が変わる |
| `gameclear()` の中の `gamereset()` の行を消す | リプレイボタンを押しても、ゴールに触れた位置から再開するので、すぐゲームクリア画面に戻ってしまう |

---

# 追いかけてくる敵

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

サンプル: [example/ex07.py](example/ex07.py)

練習: [practice/practice07.py](practice/practice07.py)

| 試すこと | 確認すること |
| --- | --- |
| オバケの動き | プレイヤーのいる方向へ、1フレームに `x`・`y` とも `ENEMY_SPEED` ずつ近づく。プレイヤーが動かなければ、やがて追いつく |
| `ENEMY_SPEED` の `1` → `3` / `5` | 数が大きいほど速く追いかけてくる。プレイヤー（`PLAYER_SPEED = 4`）より速い `5` だと、まっすぐ逃げても追いつかれる |
| オバケがプレイヤーと同じ高さになったとき | 上下に1ピクセルずつ、細かく震える（`y` が同じときは `else` の方に入って上へ動き、次のフレームでは下へ動く、を繰り返すため） |
| 縦方向の追いかけを `ovy = 0` に書き換える | 横にしか動かなくなり、プレイヤーと同じ高さにならない |
| オバケに触れる | ゲームオーバー画面に切り替わる（`down.wav` が鳴る） |
| `gamereset()` の `enemyrect.x = 650`、`enemyrect.y = 200` を消す | リプレイしても、オバケはゲームオーバーになった位置に残ったまま（最初の位置に戻らない） |
