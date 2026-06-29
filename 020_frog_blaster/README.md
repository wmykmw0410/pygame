```text
クラスを活用したゲーム設計を学びましょう
```

# 目次
- [ゲームを体験する](#ゲームを体験する)
- [ファイル構成](#ファイル構成)
- [関数で書く問題点](#関数で書く問題点)
- [Bullet クラスを作る](#bullet-クラスを作る)
- [リストで複数のインスタンスを管理する](#リストで複数のインスタンスを管理する)
- [Enemy クラスと継承](#enemy-クラスと継承)
- [GameManager にまとめる](#gamemanager-にまとめる)
- [Q1. 敵クラスを自分で作る](#q1-敵クラスを自分で作る)
- [Q2. Status に経過時間を追加する](#q2-status-に経過時間を追加する)

---

# ゲームを体験する

`game/main.py` を実行してゲームを体験しよう。

| 操作 | キー |
| --- | --- |
| 左右移動 | ← → |
| 弾を撃つ | A |
| リトライ | SPACE |

---

# ファイル構成

ゲームは役割ごとにファイルを分けている。

| ファイル | 役割 |
| --- | --- |
| `main.py` | ゲームの起動・メインループ |
| `player.py` | プレイヤーの動き・状態管理 |
| `enemy.py` | 敵の動き・種類・爆発エフェクト |
| `bullet.py` | 弾の動き |
| `gamecontrol.py` | ゲーム全体の進行管理・衝突判定 |
| `status.py` | スコア・移動距離の表示 |
| `sound.py` | BGM・効果音の管理 |
| `resultscene.py` | ゲームオーバー・クリア画面 |

各ファイルを開いてコードを確認しながら読み進めよう。

---

# 関数で書く問題点

弾の処理を**関数**だけで書くと次のようになる。

```python
bullet_x     = 0
bullet_y     = 0
bullet_alive = False

def shoot(player_x, player_y):
    global bullet_x, bullet_y, bullet_alive
    bullet_x = player_x + 17
    bullet_y = player_y - 10
    bullet_alive = True

def update_bullet():
    global bullet_y, bullet_alive
    bullet_y -= 8
    if bullet_y < -100:
        bullet_alive = False
```

これは弾が **1発しか** 管理できない。2発・3発と増やそうとすると変数がどんどん増えていく。

```python
# ❌ 発数を増やすたびに変数と関数が必要になる
bullet1_x, bullet1_y, bullet1_alive = 0, 0, False
bullet2_x, bullet2_y, bullet2_alive = 0, 0, False
```

→ 「1発分のデータと処理」をひとまとめにできれば、何発でも同じコードで扱えるはず。

---

# Bullet クラスを作る

サンプル: [game/bullet.py](game/bullet.py)

弾に必要な「データ（座標・生存フラグ）」と「処理（update・draw）」を1つのクラスにまとめる。

## やること

```
step1. Bullet クラスを定義する
         __init__(self, rect) でプレイヤーの rect を受け取る
           self.rect     プレイヤーの位置から弾の初期座標を計算する
           self.vy       上向きの速度（負の値）を設定する
           self.is_alive True で初期化する（画面外に出たら False にする）

step2. update(self) メソッドを作る
         self.rect.y += self.vy で毎フレーム上へ移動させる
         self.rect.y < -100 になったら self.is_alive = False にする

step3. draw(self, screen) メソッドを作る
         screen.blit(self.image, self.rect) で描画する
```

<details>
<summary>コードを見る</summary>

```python
class Bullet():
    def __init__(self, rect):
        x = rect.x + 17
        y = rect.y - 10
        self.image    = pg.image.load(IMG_DIR / "bullet.png")
        self.rect     = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.vy       = -8
        self.is_alive = True

    def update(self):
        self.rect.y += self.vy
        if self.rect.y < -100:
            self.is_alive = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
```

</details>

---

# リストで複数のインスタンスを管理する

サンプル: [game/gamecontrol.py](game/gamecontrol.py)

`Bullet()` を呼ぶたびに**独立した弾のインスタンス**が作られる。  
リストに入れてループで処理すれば、何発でも同じコードで扱える。

## やること

```
step1. bullets = [] でリストを用意する
step2. A キーが押されたら bullets.append(Bullet(player.rect)) で弾を追加する
step3. for b in bullets: でリストを回して b.update() / b.draw() を呼ぶ
step4. is_alive が False になった弾をリストから取り除く
         alive_bullets を別リストに用意し、is_alive の弾だけ追加して入れ替える
```

<details>
<summary>コードを見る</summary>

```python
bullets = []

# A キーで弾を発射
if key[pg.K_a]:
    bullets.append(Bullet(player.rect))

# 全発まとめて更新・描画
for b in bullets:
    b.update()
    b.draw(screen)

# 画面外に出た弾をリストから除く
alive_bullets = []
for b in bullets:
    if b.is_alive:
        alive_bullets.append(b)
bullets = alive_bullets
```

</details>

---

# Enemy クラスと継承

サンプル: [game/enemy.py](game/enemy.py)

敵も `Enemy` クラスにまとめる。種類の違う敵は `Enemy` を**継承**して差分だけを上書きする。

## やること

```
step1. Enemy クラスを定義する
         __init__(self) でランダムな初期座標・速度を設定する
         update(self) で移動・画面外チェック（is_alive = False）を行う
         draw(self, screen) でキャラ画像と HP バーを描画する

step2. FlameEnemy(Enemy) を継承で作る
         super().__init__() で親の初期化を呼ぶ
         image と vy だけ上書きする（速く落ちる敵）

step3. IceEnemy(Enemy) を継承で作る
         super().__init__() で親の初期化を呼ぶ
         maxhp と hp だけ上書きする（HP が多い敵）

step4. EnemyFactory クラスを作る
         random_create() でランダムに Enemy / FlameEnemy / IceEnemy を生成して返す
```

<details>
<summary>コードを見る</summary>

```python
class Enemy():
    def __init__(self):
        x = random.randint(100, 500)
        y = -100
        self.image    = pg.image.load(IMG_DIR / "enemy1.png")
        self.rect     = pg.Rect(x, y, 50, 50)
        self.vx       = random.uniform(-4, 4)
        self.vy       = random.uniform(1, 4)
        self.maxhp    = 100
        self.hp       = 100
        self.is_alive = True

    def update(self):
        if self.rect.x < 0 or self.rect.x > 550:
            self.vx = -self.vx
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.y > 650:
            self.is_alive = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        ...  # HP バー描画
```

```python
class FlameEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(IMG_DIR / "enemy2.png")
        self.vy    = random.uniform(5, 7)  # 速く落ちる

class IceEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(IMG_DIR / "enemy3.png")
        self.maxhp = 150
        self.hp    = 150  # HP が多い
```

```python
class EnemyFactory():
    def random_create(self):
        etype = random.choice(["normal", "flame", "ice"])
        if etype == "flame":
            return FlameEnemy()
        elif etype == "ice":
            return IceEnemy()
        else:
            return Enemy()
```

</details>

---

# GameManager にまとめる

サンプル: [game/gamecontrol.py](game/gamecontrol.py)

クラスが増えてくると、メインループも複雑になる。  
`GameManager` クラスがすべてのインスタンスを持ち、まとめて管理する。

## やること

```
step1. GameManager クラスを定義する
         __init__ で player / enemies / bullets / status を初期化する
step2. update(self) メソッドを作る
         player.update() を呼ぶ
         enemies と bullets のリストを for でまわして update() を呼ぶ
         一定フレームごとに factory.random_create() で敵を生成する
         弾と敵の衝突・敵とプレイヤーの衝突を判定する
         死んだ敵・弾をリストから取り除く
step3. draw(self, screen) メソッドを作る
         bullets / enemies / player / status をまとめて draw() する
step4. main.py からは game.update() と game.draw(screen) を呼ぶだけにする
```

<details>
<summary>コードを見る</summary>

```python
class GameManager():
    def __init__(self):
        self.player  = Player()
        self.enemies = []
        self.bullets = []
        self.status  = Status()

    def update(self):
        self.player.update()
        for e in self.enemies:
            e.update()
        for b in self.bullets:
            b.update()
        # 衝突判定・リスト整理 ...

    def draw(self, screen):
        for b in self.bullets:
            b.draw(screen)
        self.player.draw(screen)
        for e in self.enemies:
            e.draw(screen)
        self.status.draw(screen)
```

```python
# main.py: GameManager を呼ぶだけになる
game = GameManager()

while running:
    game.update()
    game.draw(screen)
```

</details>

---

# Q1. 敵クラスを自分で作る

## ステップ1 — 関数で書く

`practice/q1_func.py` を新規作成して、敵の処理を**関数**で実装しよう。

```
step1. enemy_x / enemy_y / enemy_vy / enemy_alive 変数を定義する
step2. create_enemy() 関数を作る
         enemy_x をランダムに決め、enemy_y = -50 で画面外からスタートする
         enemy_alive = True にする
step3. update_enemy() 関数を作る
         enemy_y += enemy_vy で毎フレーム下へ移動する
         enemy_y > 650 になったら enemy_alive = False にする
step4. draw_enemy(screen) 関数を作る
         pg.draw.rect() で四角形として描画する（画像は不要）
step5. メインループで create_enemy() → update_enemy() → draw_enemy() を呼ぶ
```

<details>
<summary>コードを見る</summary>

```python
import pygame as pg
import sys
import random

pg.init()
screen = pg.display.set_mode((600, 650))
clock  = pg.time.Clock()

enemy_x     = 0
enemy_y     = 0
enemy_vy    = 3
enemy_alive = False

def create_enemy():
    global enemy_x, enemy_y, enemy_alive
    enemy_x     = random.randint(50, 550)
    enemy_y     = -50
    enemy_alive = True

def update_enemy():
    global enemy_y, enemy_alive
    enemy_y += enemy_vy
    if enemy_y > 650:
        enemy_alive = False

def draw_enemy():
    if enemy_alive:
        pg.draw.rect(screen, pg.Color("RED"), pg.Rect(enemy_x, enemy_y, 50, 50))

create_enemy()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    screen.fill(pg.Color("NAVY"))
    update_enemy()
    draw_enemy()
    if not enemy_alive:
        create_enemy()
    pg.display.update()
    clock.tick(60)
```

</details>

## ステップ2 — クラスに書き直す

`practice/q1_class.py` を新規作成して、ステップ1 を `Enemy` クラスに書き直そう。

```
step1. Enemy クラスを定義する
         __init__(self) でランダムな x / y / vy / is_alive を設定する
         update(self) で移動・画面外チェックを行う
         draw(self, screen) で四角形を描画する
step2. enemies = [] リストを用意する
step3. メインループの最初に enemies.append(Enemy()) で敵を1体追加する
step4. for e in enemies: で update() と draw() を呼ぶ
step5. is_alive が False の敵をリストから取り除く
         alive_enemies を別リストに用意し is_alive の敵だけ追加して入れ替える
```

<details>
<summary>コードを見る</summary>

```python
import pygame as pg
import sys
import random

pg.init()
screen = pg.display.set_mode((600, 650))
clock  = pg.time.Clock()


class Enemy():
    def __init__(self):
        self.x        = random.randint(50, 550)
        self.y        = -50
        self.vy       = random.randint(2, 5)
        self.is_alive = True

    def update(self):
        self.y += self.vy
        if self.y > 650:
            self.is_alive = False

    def draw(self, screen):
        pg.draw.rect(screen, pg.Color("RED"), pg.Rect(self.x, self.y, 50, 50))


enemies = []

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    screen.fill(pg.Color("NAVY"))

    enemies.append(Enemy())

    for e in enemies:
        e.update()
        e.draw(screen)

    alive_enemies = []
    for e in enemies:
        if e.is_alive:
            alive_enemies.append(e)
    enemies = alive_enemies

    pg.display.update()
    clock.tick(60)
```

</details>

---

# Q2. Status に経過時間を追加する

`game/status.py` を開いて、`Status` クラスに**経過時間の表示**を追加しよう。

```
step1. reset(self) に self.time = 0 を追加する
step2. update(self, ntype) で毎フレーム self.time += 1 する
         60 カウントで 1 秒になる
step3. draw(self, screen) に経過秒数を表示する行を追加する
         self.time // 60 で秒数に変換する
         f"TIME : {self.time // 60}" を font.render() でテキストにして描画する
```

<details>
<summary>コードを見る</summary>

```python
def reset(self):
    self.distance = 0
    self.score    = 0
    self.time     = 0    # 追加

def update(self, ntype):
    if ntype == "distance":
        self.distance += 2
        self.time += 1   # 追加
    if ntype == "score":
        self.score += 1

def draw(self, screen):
    ...
    info3 = self.font.render(f"TIME : {self.time // 60}", True, pg.Color("WHITE"))
    screen.blit(info3, (250, 10))   # 追加
```

</details>
