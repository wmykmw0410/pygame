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
myimgR = pg.image.load("../images/playerR.png")
myimgR = pg.transform.scale(myimgR, (40, 50))
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
    vx = 4
    rightFlag = True
if key[pg.K_LEFT]:
    vx = -4
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
walls = [pg.Rect(0, 0, 800, 20),   # 上
         pg.Rect(0, 0, 20, 600),    # 左
         pg.Rect(780, 0, 20, 600),  # 右
         pg.Rect(0, 580, 800, 20)]  # 下

if myrect.collidelist(walls) != -1:  # いずれかと衝突したら
    myrect.x -= vx
    myrect.y -= vy
```

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

traps = []
for i in range(20):
    wx = 150 + i * 30
    wy = random.randint(20, 550)  # Y座標はランダム
    traps.append(pg.Rect(wx, wy, 30, 30))
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
    pg.mixer.Sound("../sounds/pi.wav").play()
    page = 2
```

ゲームオーバー画面ではデータをリセットしてリプレイボタンを表示する

```python
def gamereset():
    myrect.x = 50
    myrect.y = 100
    for d in range(20):
        traps[d].x = 150 + d * 30
        traps[d].y = random.randint(20, 550)

def gameover():
    gamereset()
    screen.fill(pg.Color("NAVY"))
    font = pg.font.Font(None, 150)
    text = font.render("GAMEOVER", True, pg.Color("RED"))
    screen.blit(text, (100, 200))
    btn1 = screen.blit(replay_img, (320, 480))
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
    pg.mixer.Sound("../sounds/up.wav").play()
    page = 3
```

---

# 追いかけてくる敵

サンプル: [example/ex07.py](example/ex07.py)

毎フレーム、プレイヤーの方向に1ずつ近づく

```python
ovx = 1 if enemyrect.x < myrect.x else -1  # プレイヤーが右なら+1、左なら-1
ovy = 1 if enemyrect.y < myrect.y else -1
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
