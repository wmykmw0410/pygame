```text
クラスを活用したゲーム設計を学びましょう
```

# 目次
- [ゲームを体験する](#ゲームを体験する)
- [ファイル構成](#ファイル構成)
- [設計の全体像](#設計の全体像)
- [ステップ1. ウィンドウ表示を確認する](#ステップ1-ウィンドウ表示を確認する)
- [ステップ2. Player クラスを作る](#ステップ2-player-クラスを作る)
- [ステップ3. Bullet クラスを作る](#ステップ3-bullet-クラスを作る)
- [ステップ4. リストで複数の弾を管理する](#ステップ4-リストで複数の弾を管理する)
- [ステップ5. Enemy クラスを作る](#ステップ5-enemy-クラスを作る)
- [ステップ6. FlameEnemy と IceEnemy を継承で作る](#ステップ6-flameenemy-と-iceenemy-を継承で作る)
- [ステップ7. EnemyFactory を作る](#ステップ7-enemyfactory-を作る)
- [ステップ8. BombEffect クラスを作る](#ステップ8-bombeffect-クラスを作る)
- [ステップ9. PlayerState と IdleState を作る](#ステップ9-playerstate-と-idlestate-を作る)
- [ステップ10. MovingState を追加する](#ステップ10-movingstate-を追加する)
- [ステップ11. DamageState を追加し、Player を State パターンに書き換える](#ステップ11-damagestate-を追加しplayer-を-state-パターンに書き換える)
- [ステップ12. SoundManager を作る](#ステップ12-soundmanager-を作る)
- [ステップ13. Observer パターンで Status を作る](#ステップ13-observer-パターンで-status-を作る)
- [ステップ14. GameManager の骨組みを作る](#ステップ14-gamemanager-の骨組みを作る)
- [ステップ15. GameManager で弾の発射とオブジェクトを更新する](#ステップ15-gamemanager-で弾の発射とオブジェクトを更新する)
- [ステップ16. GameManager で衝突判定と勝敗を判定する](#ステップ16-gamemanager-で衝突判定と勝敗を判定する)
- [ステップ17. GameManager の生存リスト整理と描画をまとめる](#ステップ17-gamemanager-の生存リスト整理と描画をまとめる)
- [ステップ18. ResultScene を作る](#ステップ18-resultscene-を作る)
- [ステップ19. main.py を完成させる](#ステップ19-mainpy-を完成させる)
- [ステップ20. Status に経過時間を追加する](#ステップ20-status-に経過時間を追加する)

---

# ゲームを体験する

`main.py` を実行してゲームを体験しよう。

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
| `game/__init__.py` | `GameManager`・`ResultScene` をパッケージ外へエクスポート |
| `game/player.py` | プレイヤーの動き・状態管理 |
| `game/enemy.py` | 敵の動き・種類・爆発エフェクト |
| `game/bullet.py` | 弾の動き |
| `game/gamecontrol.py` | ゲーム全体の進行管理・衝突判定 |
| `game/status.py` | スコア・移動距離の表示 |
| `game/sound.py` | BGM・効果音の管理 |
| `game/resultscene.py` | ゲームオーバー・クリア画面 |

数値の設定（速度・HP・座標など）は共通の設定ファイルにまとめず、それぞれの値を使うファイルの先頭に直接定数として書く。1つのファイルを開くだけで、そのファイルが使っている値がすべてわかるようにするためだ。

各ファイルを開いてコードを確認しながら読み進めよう。

---

# 設計の全体像

このゲームは `GameManager` を司令塔として、役割ごとのクラスが協調して動く構成になっている。

```
main.py
 ├─ GameManager  ……… プレイヤー・敵・弾・エフェクト・スコアをまとめて管理する
 │    ├─ Player       状態（State）で見た目と動きを切り替える
 │    ├─ Enemy 系      継承で3種類に分かれる敵。EnemyFactory が生成を担当する
 │    ├─ Bullet        プレイヤーが発射する弾
 │    ├─ BombEffect    敵を倒したときの爆発エフェクト
 │    └─ Status        GameManager からの通知でスコア・距離・時間を更新する
 └─ ResultScene  ……… GameManager の状態を見てゲームオーバー・クリア画面を出す

SoundManager ……… どこから呼んでも同じ1つのインスタンスでBGM・効果音を鳴らす
```

`GameManager` は毎フレーム `update()` で全オブジェクトを動かし衝突判定を行い、`draw()` でまとめて描画する。`main.py` はこの `GameManager` と `ResultScene` を呼ぶだけのシンプルな形になる（[ステップ19](#ステップ19-mainpy-を完成させる)）。

まず素の `Player`・`Bullet`・`Enemy`・`GameManager` を組み上げてゲームを一通り動くようにしてから（ステップ2〜8）、その後で見た目や演出に関わるクラス設計パターンを1つずつ追加していく（ステップ9〜13）。

このレッスンには、次の5つのクラス設計パターンが登場する。1つずつ、ステップの中で実際に手を動かしながら組み立てていく。

| パターン | 使われている場所 | 目的 |
| --- | --- | --- |
| 継承 | `Enemy` 系（ステップ5〜6） | 共通処理を親クラスにまとめ、差分だけを子クラスで上書きする |
| Factory（生成） | `EnemyFactory`（ステップ7） | オブジェクトの生成ロジックを1箇所にまとめる |
| State（状態） | `Player`（ステップ9〜11） | 状態ごとに見た目・動きの処理を切り替える |
| Singleton | `SoundManager`（ステップ12） | アプリ内で常に同じ1つのインスタンスを共有する |
| Observer（通知） | `Subject` / `Status`（ステップ13） | 通知する側と受け取る側を疎結合にする |

## 動作確認のタイミング

ほとんどのステップはクラスの一部分だけを作るので、その場では実行できない。  
実際に `main.py` を動かして目で確認できるのは、次の5か所だけ。

| チェックポイント | 確認できること |
| --- | --- |
| [ステップ1](#ステップ1-ウィンドウ表示を確認する) | 空のウィンドウが表示される |
| [ステップ2](#ステップ2-player-クラスを作る) | カエルが表示され、← → で動かせる（まだ静止画のまま） |
| [ステップ4](#ステップ4-リストで複数の弾を管理する) | A キーで弾を発射できる（まだ敵はいない） |
| [ステップ11](#ステップ11-damagestate-を追加しplayer-を-state-パターンに書き換える) | 動いている間は歩行アニメーションに切り替わる |
| [ステップ19](#ステップ19-mainpy-を完成させる) | 敵・衝突判定・スコア・BGMまで含めて最初から最後まで通しで遊べる（被弾の見た目もここで確認できる） |

それ以外のステップ（3, 5〜10, 12〜18, 20）は「まだ実行できないパーツを作っている」段階。焦らず、次のチェックポイントまで組み立てを進めよう。

---

## ステップ1. ウィンドウ表示を確認する

記載先: [main.py](main.py)

pygame でゲームを動かす基本の骨格を確認しよう。まだキャラクターは出さず、空のウィンドウを表示するだけにする。

## やること

```
step1. pg.init() で pygame を初期化する
step2. pg.display.set_mode((600, 650)) でウィンドウを作る
step3. running = True でループ管理フラグを用意する
step4. for event in pg.event.get(): で毎フレームイベントを処理する
         pg.QUIT が来たら running = False にして終了する
step5. screen.fill() で背景を塗りつぶす
step6. pg.display.update() で画面を更新し、clock.tick(60) で FPS を制御する
step7. ループを抜けたら pg.quit() で終了する
```

<details>
<summary>コードを見る</summary>

**step1.** pygame を初期化する

```python
import pygame as pg

def main():
    pg.init()
```

**step2.** ウィンドウを作る

```python
    screen = pg.display.set_mode((600, 650))
    pg.display.set_caption("Frog Blaster")
    clock = pg.time.Clock()
```

**step3.** ループ管理フラグを用意する

```python
    running = True
    while running:
```

**step4.** イベントを処理する

```python
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
```

**step5.** 背景を塗りつぶす

```python
        screen.fill(pg.Color("NAVY"))
```

**step6.** 画面を更新し FPS を制御する

```python
        pg.display.update()
        clock.tick(60)
```

**step7.** ループを抜けたら終了する

```python
    pg.quit()

if __name__ == "__main__":
    main()
```

</details>

▶ **動作確認**: ここまでで実行し、空のウィンドウ（NAVY色の背景）が表示されることを確認しよう。

※ ここから先のステップで、このループにキャラクターや弾・敵を1つずつ追加していく。

---

## ステップ2. Player クラスを作る

記載先: [game/player.py](game/player.py), [main.py](main.py)

`Player` 本体を作り、ステップ1の仮の main.py に組み込んで動かしてみよう。状態（State）による見た目の切り替えはまだ使わず、待機中の画像をそのまま表示するだけのシンプルな形にする。  
プレイヤーのサイズ・初期位置・速度・HP・HPバーの見た目・画面幅は、`game/player.py` の先頭に定数としてまとめて定義する。

## やること

```
step1. ファイルの先頭に必要な定数を定義する
         WIDTH（画面幅。左右移動の上限に使う）
         PLAYER_SIZE / PLAYER_START / PLAYER_SPEED / PLAYER_MAX_HP
         HP_BAR_WIDTH / HP_BAR_HEIGHT / HP_BAR_OFFSET

step2. Player クラスを作る
         __init__ で self.reset() を呼ぶ
         reset() で待機中のカエル画像を self.image に直接読み込み、
           rect / speed / maxhp / hp をステップ1の定数から設定する
         update() でキー入力で左右移動する
           左右の移動範囲は WIDTH - PLAYER_SIZE を上限にする
         draw(self, screen) でキャラ画像と HP バーを描画する
           HPバーのサイズは HP_BAR_* を使う
         damage() はまだ何もしない（ステップ11で状態パターンに書き換える）

step3. main.py に Player を追加する
         player = Player() でインスタンスを作る
         ループ内で player.update() と player.draw(screen) を呼ぶ
```

<details>
<summary>コードを見る</summary>

**step1.** 必要な定数を定義する（`game/player.py`）

```python
WIDTH = 600

PLAYER_SIZE   = 50
PLAYER_START  = (250, 550)
PLAYER_SPEED  = 10
PLAYER_MAX_HP = 150

HP_BAR_WIDTH  = 4
HP_BAR_HEIGHT = 20
HP_BAR_OFFSET = 20
```

**step2.** Player クラスを作る（`game/player.py`）

```python
class Player():
    def __init__(self):
        self.reset()

    def reset(self):
        self.image = pg.image.load(IMG_DIR / "kaeru1.png")
        self.rect  = pg.Rect(*PLAYER_START, PLAYER_SIZE, PLAYER_SIZE)
        self.speed = PLAYER_SPEED
        self.maxhp = PLAYER_MAX_HP
        self.hp    = PLAYER_MAX_HP

    def update(self):
        key = pg.key.get_pressed()
        vx = 0
        if key[pg.K_RIGHT]:
            vx =  self.speed
        if key[pg.K_LEFT]:
            vx = -self.speed
        if self.rect.x + vx < 0 or self.rect.x + vx > WIDTH - PLAYER_SIZE:
            vx = 0
        self.rect.x += vx

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        # HP バー
        rect1 = pg.Rect(self.rect.x, self.rect.y - HP_BAR_OFFSET, HP_BAR_WIDTH, HP_BAR_HEIGHT)
        h     = (self.hp / self.maxhp) * HP_BAR_HEIGHT
        rect2 = pg.Rect(self.rect.x, self.rect.y - h, HP_BAR_WIDTH, h)
        pg.draw.rect(screen, pg.Color("RED"),   rect1)
        pg.draw.rect(screen, pg.Color("GREEN"), rect2)

    def damage(self):
        pass   # 見た目を変える処理はステップ11で追加する
```

**step3.** main.py に Player を追加する（`main.py`）

```python
import pygame as pg
from game.player import Player

WIDTH, HEIGHT = 600, 650
FPS = 60

def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Frog Blaster")
    clock = pg.time.Clock()

    player = Player()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill(pg.Color("NAVY"))

        player.update()
        player.draw(screen)

        pg.display.update()
        clock.tick(FPS)

    pg.quit()
```

</details>

▶ **動作確認**: ここまでで実行し、カエルが表示されて ← → キーで動かせることを確認しよう（まだ静止画のままで、歩行アニメーションや被弾の見た目はステップ11で追加する）。

※ この main.py はまだ仮の形。この後 Bullet・Enemy を追加し、最終的に `GameManager` を使う完成版に書き換える（[ステップ19](#ステップ19-mainpy-を完成させる)）。

---

## ステップ3. Bullet クラスを作る

記載先: [game/bullet.py](game/bullet.py)

弾に必要な「データ（座標・生存フラグ）」と「処理（update・draw）」を1つのクラスにまとめる。  
発射位置のズレ・速度・画面外とみなす座標は `game/bullet.py` の先頭に定数として定義する。

## やること

```
step1. ファイルの先頭に BULLET_OFFSET / BULLET_SPEED / OFFSCREEN_Y を定義する

step2. Bullet クラスを定義する
         __init__(self, rect) でプレイヤーの rect を受け取る
           self.rect     プレイヤーの位置に BULLET_OFFSET を足して初期座標を計算する
           self.vy       BULLET_SPEED を使って上向きの速度を設定する
           self.is_alive True で初期化する（画面外に出たら False にする）

step3. update(self) メソッドを作る
         self.rect.y += self.vy で毎フレーム上へ移動させる
         self.rect.y < OFFSCREEN_Y になったら self.is_alive = False にする

step4. draw(self, screen) メソッドを作る
         screen.blit(self.image, self.rect) で描画する
```

<details>
<summary>コードを見る</summary>

**step1.** 定数を定義する

```python
BULLET_OFFSET = (17, -10)   # プレイヤーの rect から見た発射位置のズレ
BULLET_SPEED  = 8
OFFSCREEN_Y   = -100        # これより上に出たら画面外とみなす
```

**step2.** Bullet クラスを定義する

```python
class Bullet():
    def __init__(self, rect):
        x = rect.x + BULLET_OFFSET[0]
        y = rect.y + BULLET_OFFSET[1]
        self.image        = pg.image.load(IMG_DIR / "bullet.png")
        self.rect         = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.vy           = -BULLET_SPEED
        self.is_alive     = True
```

**step3.** update(self) メソッドを作る

```python
    def update(self):
        self.rect.y += self.vy
        if self.rect.y < OFFSCREEN_Y:
            self.is_alive = False
```

**step4.** draw(self, screen) メソッドを作る

```python
    def draw(self, screen):
        screen.blit(self.image, self.rect)
```

</details>

---

## ステップ4. リストで複数の弾を管理する

記載先: [main.py](main.py)（ステップ2の仮の main.py に追記する）

`Bullet()` を呼ぶたびに**独立した弾のインスタンス**が作られる。  
リストに入れてループで処理すれば、何発でも同じコードで扱える。  
※ この処理は後でステップ15の `GameManager.update()` に移す。ここでは簡略化のため毎フレーム発射できる版にしているが、実際の `GameManager` では連射を防ぐためのクールダウンを追加する（ステップ15）。

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

**step1.** リストを用意する

```python
bullets = []
```

**step2.** A キーで弾を追加する

```python
if key[pg.K_a]:
    bullets.append(Bullet(player.rect))
```

**step3.** 全弾をまとめて更新・描画する

```python
for b in bullets:
    b.update()
    b.draw(screen)
```

**step4.** 画面外に出た弾をリストから除く

```python
alive_bullets = []
for b in bullets:
    if b.is_alive:
        alive_bullets.append(b)
bullets = alive_bullets
```

</details>

▶ **動作確認**: ここまでで実行し、A キーで弾を連続して発射できることを確認しよう（まだ敵がいないので当たり判定は次のステップ以降で確認する）。

---

## ステップ5. Enemy クラスを作る

記載先: [game/enemy.py](game/enemy.py)

敵も `Enemy` クラスにまとめる。まずは種類分けをしない基本の敵から作る。  
出現位置・速度の範囲・HP・HPバーの見た目・画面サイズは `game/enemy.py` の先頭に定数として定義する。

## やること

```
step1. ファイルの先頭に必要な定数を定義する
         WIDTH, HEIGHT（画面サイズ。移動範囲のチェックに使う）
         ENEMY_SIZE / ENEMY_SPAWN_X_RANGE / ENEMY_SPAWN_Y / ENEMY_VX_RANGE / ENEMY_VY_RANGE / ENEMY_MAX_HP
         HP_BAR_WIDTH / HP_BAR_HEIGHT / HP_BAR_OFFSET（Player と同じ見た目にする）

step2. Enemy クラスを定義する
         __init__(self) で ENEMY_SPAWN_X_RANGE / ENEMY_SPAWN_Y から
           ランダムな初期座標を決め、ENEMY_VX_RANGE / ENEMY_VY_RANGE から速度を決める
         update(self) で移動・画面外チェック（is_alive = False）を行う
           左右の壁は WIDTH - ENEMY_SIZE、下端は HEIGHT を使う
         draw(self, screen) でキャラ画像と HP バーを描画する
```

<details>
<summary>コードを見る</summary>

**step1.** 必要な定数を定義する

```python
WIDTH, HEIGHT = 600, 650

ENEMY_SIZE          = 50
ENEMY_SPAWN_X_RANGE = (100, 500)
ENEMY_SPAWN_Y       = -100
ENEMY_VX_RANGE      = (-4, 4)
ENEMY_VY_RANGE      = (1, 4)
ENEMY_MAX_HP        = 100

HP_BAR_WIDTH  = 4
HP_BAR_HEIGHT = 20
HP_BAR_OFFSET = 20   # キャラクターの上端からバーまでの距離
```

**step2.** Enemy クラスを定義する

```python
class Enemy():
    def __init__(self):
        x = random.randint(*ENEMY_SPAWN_X_RANGE)
        y = ENEMY_SPAWN_Y
        self.image    = pg.image.load(IMG_DIR / "enemy1.png")
        self.rect     = pg.Rect(x, y, ENEMY_SIZE, ENEMY_SIZE)
        self.vx       = random.uniform(*ENEMY_VX_RANGE)
        self.vy       = random.uniform(*ENEMY_VY_RANGE)
        self.maxhp    = ENEMY_MAX_HP
        self.hp       = ENEMY_MAX_HP
        self.is_alive = True

    def update(self):
        if self.rect.x < 0 or self.rect.x > WIDTH - ENEMY_SIZE:
            self.vx = -self.vx
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.y > HEIGHT:
            self.is_alive = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        # HP バー
        rect1 = pg.Rect(self.rect.x, self.rect.y - HP_BAR_OFFSET, HP_BAR_WIDTH, HP_BAR_HEIGHT)
        h     = (self.hp / self.maxhp) * HP_BAR_HEIGHT
        rect2 = pg.Rect(self.rect.x, self.rect.y - h, HP_BAR_WIDTH, h)
        pg.draw.rect(screen, pg.Color("RED"),   rect1)
        pg.draw.rect(screen, pg.Color("GREEN"), rect2)
```

</details>

---

## ステップ6. FlameEnemy と IceEnemy を継承で作る

記載先: [game/enemy.py](game/enemy.py)

種類の違う敵は `Enemy` を**継承**して差分だけを上書きする。  
上書きに使う値も `game/enemy.py` の先頭に定数として追加する。

## やること

```
step1. ファイルの先頭に FLAME_VX_RANGE / FLAME_VY_RANGE / ICE_MAX_HP を定義する

step2. FlameEnemy(Enemy) を継承で作る
         super().__init__() で親の初期化を呼ぶ
         image と vy だけ、FLAME_VX_RANGE / FLAME_VY_RANGE で上書きする（速く落ちる敵）

step3. IceEnemy(Enemy) を継承で作る
         super().__init__() で親の初期化を呼ぶ
         maxhp と hp だけ、ICE_MAX_HP で上書きする（HP が多い敵）
```

<details>
<summary>コードを見る</summary>

**step1.** 定数を定義する

```python
FLAME_VX_RANGE = (-2, 2)
FLAME_VY_RANGE = (5, 7)

ICE_MAX_HP = 150
```

**step2.** FlameEnemy(Enemy) を継承で作る

```python
class FlameEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(IMG_DIR / "enemy2.png")
        self.vx    = random.uniform(*FLAME_VX_RANGE)
        self.vy    = random.uniform(*FLAME_VY_RANGE)   # 速く落ちる
```

**step3.** IceEnemy(Enemy) を継承で作る

```python
class IceEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(IMG_DIR / "enemy3.png")
        self.maxhp = ICE_MAX_HP
        self.hp    = ICE_MAX_HP                    # HP が多い
```

</details>

---

## ステップ7. EnemyFactory を作る

記載先: [game/enemy.py](game/enemy.py)

3種類の敵をランダムに生成する `EnemyFactory` を作る。

## やること

```
step1. EnemyFactory クラスを作る
         random_create() でランダムに Enemy / FlameEnemy / IceEnemy を生成して返す
```

<details>
<summary>コードを見る</summary>

**step1.** EnemyFactory クラスを作る

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

## ステップ8. BombEffect クラスを作る

記載先: [game/enemy.py](game/enemy.py)

敵を倒したときに再生する爆発エフェクトを作る。画像を連番で切り替え、最後まで再生したら自分自身をリストから取り除く。  
爆発画像のコマ数は `game/enemy.py` の先頭に定数として追加する（アニメーションの切り替え間隔 `ANIM_FRAME_DELAY` も同様に定義する）。

## やること

```
step1. ファイルの先頭に BOMB_FRAME_COUNT / ANIM_FRAME_DELAY を定義する

step2. BombEffect クラスを定義する
         __init__(self, rect, effects) で BOMB_FRAME_COUNT 枚分の
           爆発画像リスト・表示位置・自分を消すための effects リスト（GameManager が持つリスト）への参照を持つ

step3. update(self) メソッドを作る
         ANIM_FRAME_DELAY ごとにカウントを進め、画像を順番に切り替える
         最後の画像まで進んだら self._effects.remove(self) で自分自身をリストから取り除く

step4. draw(self, screen) メソッドを作る
         screen.blit(self._image, self._rect) で描画する
```

<details>
<summary>コードを見る</summary>

**step1.** 定数を定義する

```python
BOMB_FRAME_COUNT = 6

ANIM_FRAME_DELAY = 5    # 何フレームごとに次のコマに切り替えるか
```

**step2.** BombEffect クラスを定義する

```python
class BombEffect():
    def __init__(self, rect, effects):
        self.images = []
        for i in range(BOMB_FRAME_COUNT):
            self.images.append(pg.image.load(IMG_DIR / f"bomb_{i}.png"))
        self.image   = self.images[0]
        self.effects = effects
        self.rect    = rect
        self.cnt     = 0
```

**step3.** update(self) メソッドを作る

```python
    def update(self):
        self.cnt += 1
        idx = self.cnt // ANIM_FRAME_DELAY
        if idx <= BOMB_FRAME_COUNT - 1:
            self.image = self.images[idx]
        else:
            self.effects.remove(self)
```

**step4.** draw(self, screen) メソッドを作る

```python
    def draw(self, screen):
        screen.blit(self.image, self.rect)
```

</details>

※ `BombEffect` は自分では生成されない。誰が・いつ生成するかはステップ16（衝突判定）で扱う。

---

## ステップ9. PlayerState と IdleState を作る

記載先: [game/player.py](game/player.py)

`Player` は「状態（ステート）」によって画像や動きを切り替える。  
まず土台となる `PlayerState` 基底クラスと、待機中の `IdleState` から作ろう。

## やること

```
step1. PlayerState 基底クラスを定義する
         __init__(self, player) で player への参照と image を持つ
         update(self) は派生クラスで上書きする（何もしない版を定義しておく）

step2. IdleState(PlayerState) を作る
         __init__ で待機中のカエル画像を読み込む
         update() でキーが押されていたら MovingState を返す（次のステップで作る）
         押されていなければ self を返す（状態を維持）
```

<details>
<summary>コードを見る</summary>

**step1.** PlayerState 基底クラスを定義する

```python
class PlayerState():
    def __init__(self, player):
        self.player = player
        self.image  = None

    def update(self):
        pass
```

**step2.** IdleState(PlayerState) を作る

```python
class IdleState(PlayerState):
    def __init__(self, player):
        super().__init__(player)
        self.image = pg.image.load(IMG_DIR / "kaeru1.png")

    def update(self):
        key = pg.key.get_pressed()
        if key[pg.K_LEFT] or key[pg.K_RIGHT]:
            return MovingState(self.player)
        return self
```

</details>

---

## ステップ10. MovingState を追加する

記載先: [game/player.py](game/player.py)

左右キーが押されている間、歩行アニメーションをする `MovingState` を作る。  
アニメーションの切り替え間隔は `ANIM_FRAME_DELAY` という定数として `game/player.py` の先頭に定義する。

## やること

```
step1. ファイルの先頭に ANIM_FRAME_DELAY を定義する
         何フレームごとに次のコマに切り替えるかを表す

step2. MovingState(PlayerState) を作る
         __init__ で歩行アニメーション用の画像リストを読み込む
         update() で ANIM_FRAME_DELAY を使ってアニメーション画像を切り替える
         キーが離されたら IdleState を返す
```

<details>
<summary>コードを見る</summary>

**step1.** ANIM_FRAME_DELAY を定義する

```python
ANIM_FRAME_DELAY = 5
```

**step2.** MovingState(PlayerState) を作る

```python
class MovingState(PlayerState):
    def __init__(self, player):
        super().__init__(player)
        self.images = [
            pg.image.load(IMG_DIR / "kaeru1.png"),
            pg.image.load(IMG_DIR / "kaeru2.png"),
            pg.image.load(IMG_DIR / "kaeru3.png"),
            pg.image.load(IMG_DIR / "kaeru4.png"),
        ]
        self.cnt    = 0
        self.image  = self.images[0]

    def update(self):
        self.cnt  += 1
        self.image = self.images[self.cnt // ANIM_FRAME_DELAY % len(self.images)]
        key = pg.key.get_pressed()
        if not (key[pg.K_LEFT] or key[pg.K_RIGHT]):
            return IdleState(self.player)
        return self
```

</details>

※ `self.cnt // ANIM_FRAME_DELAY % len(self.images)` の `len(self.images)`（画像の枚数）は定数化していない。画像リストの長さそのものを使えば自動的に正しい枚数になるため、あえて `4` のような固定値にしていない。

---

## ステップ11. DamageState を追加し、Player を State パターンに書き換える

記載先: [game/player.py](game/player.py)

敵に当たったときの被弾状態 `DamageState` を作り、ステップ2で作った素の `Player` を、`PlayerState`（ステップ9〜10で作った状態クラス）を使う形に書き換える。ここで初めて `Player` が「状態（ステート）」で見た目と動きを切り替えるようになる。

## やること

```
step1. ファイルの先頭に DAMAGE_DURATION を定義する
         被弾状態が続くフレーム数

step2. DamageState(PlayerState) を作る
         __init__ で被弾時の画像リストを読み込み、timeout に DAMAGE_DURATION を設定する
         update() でタイムアウトカウントを減らす
         0 になったら IdleState に戻る

step3. Player をステップ2のシンプル版から State パターンを使う形に書き換える
         reset() で self.image の代わりに self.state = IdleState(self) を持つ
         update() の先頭で self.state = self.state.update() を呼ぶ
         draw(self, screen) は self.image の代わりに self.state.image を描画する
         damage()（ステップ2ではまだ何もしていなかった）で self.state = DamageState(self) に切り替える
```

<details>
<summary>コードを見る</summary>

**step1.** DAMAGE_DURATION を定義する

```python
DAMAGE_DURATION = 20
```

**step2.** DamageState(PlayerState) を作る

```python
class DamageState(PlayerState):
    def __init__(self, player):
        super().__init__(player)
        self.images  = [pg.image.load(IMG_DIR / "kaeru5.png"),
                        pg.image.load(IMG_DIR / "kaeru6.png")]
        self.cnt     = 0
        self.image   = self.images[0]
        self.timeout = DAMAGE_DURATION

    def update(self):
        self.cnt    += 1
        self.image   = self.images[self.cnt // ANIM_FRAME_DELAY % len(self.images)]
        self.timeout -= 1
        if self.timeout < 0:
            return IdleState(self.player)
        return self
```

**step3.** Player を State パターンを使う形に書き換える

```python
class Player():
    def __init__(self):
        self.reset()

    def reset(self):
        self.state = IdleState(self)
        self.rect  = pg.Rect(*PLAYER_START, PLAYER_SIZE, PLAYER_SIZE)
        self.speed = PLAYER_SPEED
        self.maxhp = PLAYER_MAX_HP
        self.hp    = PLAYER_MAX_HP

    def update(self):
        self.state = self.state.update()
        key = pg.key.get_pressed()
        vx = 0
        if key[pg.K_RIGHT]:
            vx =  self.speed
        if key[pg.K_LEFT]:
            vx = -self.speed
        if self.rect.x + vx < 0 or self.rect.x + vx > WIDTH - PLAYER_SIZE:
            vx = 0
        self.rect.x += vx

    def draw(self, screen):
        screen.blit(self.state.image, self.rect)
        # HP バー
        rect1 = pg.Rect(self.rect.x, self.rect.y - HP_BAR_OFFSET, HP_BAR_WIDTH, HP_BAR_HEIGHT)
        h     = (self.hp / self.maxhp) * HP_BAR_HEIGHT
        rect2 = pg.Rect(self.rect.x, self.rect.y - h, HP_BAR_WIDTH, h)
        pg.draw.rect(screen, pg.Color("RED"),   rect1)
        pg.draw.rect(screen, pg.Color("GREEN"), rect2)

    def damage(self):
        self.state = DamageState(self)
```

</details>

▶ **動作確認**: ここまでで実行し、← → キーで動いている間は歩行アニメーションに切り替わることを確認しよう（被弾状態はまだ `GameManager` が無く呼び出す手段が無いため、最後の通しプレイ（[ステップ19](#ステップ19-mainpy-を完成させる)）で確認する）。

---

## ステップ12. SoundManager を作る

記載先: [game/sound.py](game/sound.py)

BGM や効果音は、アプリの中でただ1つだけ存在すれば十分。  
`SoundManager` は**Singletonパターン**で作り、どこから呼んでも必ず同じインスタンスを使い回すようにする。

## やること

```
step1. SoundManager クラスを定義する
         クラス変数 _instance = None を用意する
         get_instance() を作り、
           _instance がまだ無ければ新しく作って保存し、あれば保存済みのものを返す

step2. __init__ で BGM・各種効果音ファイルを読み込む

step3. bgmstart() / bgmstop() で BGM を再生・停止する

step4. playover() / playclear() / playattack() / playblast() / playbomb() で
         各効果音を再生する
         playattack() は複数の音からランダムに1つ選んで再生する
```

<details>
<summary>コードを見る</summary>

**step1.** SoundManager クラスと Singleton の仕組みを作る

```python
class SoundManager():
    instance = None

    def get_instance():
        if SoundManager.instance is None:
            SoundManager.instance = SoundManager()
        return SoundManager.instance
```

**step2.** BGM・効果音ファイルを読み込む

```python
    def __init__(self):
        pg.mixer.music.load(SND_DIR / "bgm.wav")
        self.over  = pg.mixer.Sound(SND_DIR / "over.wav")
        self.clear = pg.mixer.Sound(SND_DIR / "clear.wav")
        self.clap1 = pg.mixer.Sound(SND_DIR / "clap1.wav")
        self.clap2 = pg.mixer.Sound(SND_DIR / "clap2.wav")
        self.clap3 = pg.mixer.Sound(SND_DIR / "clap3.wav")
        self.blast = pg.mixer.Sound(SND_DIR / "blast.wav")
        self.bomb  = pg.mixer.Sound(SND_DIR / "bomb.wav")
```

**step3.** BGM を再生・停止する

```python
    def bgmstart(self):
        pg.mixer.music.play(-1)

    def bgmstop(self):
        pg.mixer.music.stop()
```

**step4.** 効果音を再生する

```python
    def playover(self):
        self.over.play()

    def playclear(self):
        self.clear.play()

    def playattack(self):
        random.choice([self.clap1, self.clap2, self.clap3]).play()

    def playblast(self):
        self.blast.play()

    def playbomb(self):
        self.bomb.play()
```

</details>

※ 使うときは `SoundManager()` ではなく必ず `SoundManager.get_instance()` を呼ぶ。こうすることで、どこから呼んでも同じ1つのインスタンス（＝同じ音源）を共有できる。

---

## ステップ13. Observer パターンで Status を作る

記載先: [game/status.py](game/status.py), [game/gamecontrol.py](game/gamecontrol.py)

`GameManager` は「敵を倒した」「進んだ」といった出来事のたびに `Status` を直接書き換えるのではなく、**Observer パターン**で疎結合にする。  
`GameManager`（通知する側 = Subject）が `notify()` を呼ぶと、登録された `Status`（通知を受け取る側 = Observer）の `update()` が呼ばれる。  
表示に関する定数（フォントサイズ・位置など）は `game/status.py` の先頭に定義する。

## やること

```
step1. game/status.py に Observer 基底クラスを作る
         update(self, ntype) は派生クラスで上書きする（何もしない版を定義しておく）

step2. game/status.py の先頭に必要な定数を定義する
         WIDTH（画面幅。表示用の Surface の幅に使う）
         STATUS_FONT_SIZE / STATUS_BAR_HEIGHT / STATUS_BG_ALPHA
         DISTANCE_PER_TICK / STATUS_DISTANCE_POS / STATUS_SCORE_POS

step3. Status(Observer) を作る
         __init__ で STATUS_FONT_SIZE / STATUS_BAR_HEIGHT を使って
           フォントと表示用の Surface を用意し、reset() を呼ぶ
         reset(self) で distance / score を初期化する
         update(self, ntype) で ntype が "distance" なら DISTANCE_PER_TICK を、
           "score" なら 1 を増やす
         draw(self, screen) で DISTANCE と SCORE を、定数で指定した位置に表示する

step4. game/gamecontrol.py に Subject クラスを作る
         __init__ で observers = [] を持つ
         attach(observer) で observers に追加する
         notify(ntype) で登録された全observerの update(ntype) を呼ぶ
```

<details>
<summary>コードを見る</summary>

**step1.** Observer 基底クラスを作る（`game/status.py`）

```python
class Observer:
    def update(self, ntype):
        pass
```

**step2.** 必要な定数を定義する（`game/status.py`）

```python
WIDTH = 600

STATUS_FONT_SIZE    = 32
STATUS_BAR_HEIGHT   = 36
STATUS_BG_ALPHA     = 128
DISTANCE_PER_TICK   = 2
STATUS_DISTANCE_POS = (20, 10)
STATUS_SCORE_POS    = (380, 10)
```

**step3.** Status(Observer) を作る（`game/status.py`）

```python
class Status(Observer):
    def __init__(self):
        self.font  = pg.font.Font(None, STATUS_FONT_SIZE)
        self.board = pg.Surface((WIDTH, STATUS_BAR_HEIGHT), pg.SRCALPHA)
        self.reset()

    def reset(self):
        self.distance = 0
        self.score    = 0

    def update(self, ntype):
        if ntype == "distance":
            self.distance += DISTANCE_PER_TICK
        if ntype == "score":
            self.score += 1

    def draw(self, screen):
        pg.draw.rect(self.board, (0, 0, 0, STATUS_BG_ALPHA), pg.Rect(0, 0, WIDTH, STATUS_BAR_HEIGHT))
        screen.blit(self.board, (0, 0))
        info1 = self.font.render(f"DISTANCE : {self.distance}", True, pg.Color("WHITE"))
        info2 = self.font.render(f"SCORE : {self.score}",      True, pg.Color("WHITE"))
        screen.blit(info1, STATUS_DISTANCE_POS)
        screen.blit(info2, STATUS_SCORE_POS)
```

**step4.** Subject クラスを作る（`game/gamecontrol.py`）

```python
class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, ntype):
        for observer in self.observers:
            observer.update(ntype)
```

</details>

※ `Subject` と `Status` をどうつなげる（`attach`）かはステップ14で `GameManager` を作るときに扱う。

---

## ステップ14. GameManager の骨組みを作る

記載先: [game/gamecontrol.py](game/gamecontrol.py)

クラスが増えてくると、メインループも複雑になる。  
`GameManager` は `Subject` を継承し、すべてのインスタンスを持ってまとめて管理する。

## やること

```
step1. GameManager(Subject) クラスを定義する
         __init__ で super().__init__() を呼ぶ
         player / enemies / effects / bullets / factory / status を用意する
         self.attach(self.status) で Status を通知先として登録する
         最後に self.reset() を呼ぶ

step2. reset(self) メソッドを作る
         is_playing / is_cleared フラグを設定する
         player.reset() を呼び、enemies / bullets をクリアする
         spawn_count / bullet_count（タイミング用カウンタ）を 0 にする
         status.reset() を呼び、SoundManager.get_instance().bgmstart() で BGM を開始する
```

<details>
<summary>コードを見る</summary>

**step1.** GameManager(Subject) クラスを定義する

```python
import pygame as pg
import random
from . import player, enemy, bullet, status, sound


class GameManager(Subject):
    def __init__(self):
        super().__init__()
        self.player  = player.Player()
        self.enemies = []
        self.effects = []
        self.bullets = []
        self.factory = enemy.EnemyFactory()
        self.status  = status.Status()
        self.attach(self.status)
        self.reset()
```

**step2.** reset(self) メソッドを作る

```python
    def reset(self):
        self.is_playing  = True
        self.is_cleared  = False
        self.player.reset()
        self.enemies.clear()
        self.bullets.clear()
        self.spawn_count  = 0
        self.bullet_count = 0
        self.status.reset()
        sound.SoundManager.get_instance().bgmstart()
```

</details>

---

## ステップ15. GameManager で弾の発射とオブジェクトを更新する

記載先: [game/gamecontrol.py](game/gamecontrol.py)

`update()` の前半を作る。弾の発射にクールダウンをつけ、既存のオブジェクトを更新し、一定間隔で敵を生成する。  
クールダウンや出現間隔は `game/gamecontrol.py` の先頭に定数として定義する。

## やること

```
step1. ファイルの先頭に BULLET_COOLDOWN / ENEMY_SPAWN_INTERVAL を定義する

step2. update(self) の先頭で self.notify("distance") を呼び、
         進んだ距離を Status に通知する

step3. bullet_count を毎フレーム増やし、BULLET_COOLDOWN を超えたときだけ
         A キーで弾を発射できるようにする（連射を防ぐクールダウン）

step4. effects / bullets / player をそれぞれ update() する

step5. spawn_count を毎フレーム増やし、ENEMY_SPAWN_INTERVAL ごとに
         factory.random_create() で敵を生成する
```

<details>
<summary>コードを見る</summary>

**step1.** 定数を定義する

```python
BULLET_COOLDOWN      = 10
ENEMY_SPAWN_INTERVAL = 15
```

**step2.** 進んだ距離を通知する

```python
    def update(self):
        self.notify("distance")
```

**step3.** クールダウン付きで弾を発射する

```python
        self.bullet_count += 1
        if self.bullet_count > BULLET_COOLDOWN:
            key = pg.key.get_pressed()
            if key[pg.K_a]:
                self.bullets.append(bullet.Bullet(self.player.rect))
                self.bullet_count = 0
```

**step4.** 既存のオブジェクトを更新する

```python
        for eff in self.effects:
            eff.update()
        for b in self.bullets:
            b.update()
        self.player.update()
```

**step5.** 一定間隔で敵を生成する

```python
        self.spawn_count += 1
        if self.spawn_count > ENEMY_SPAWN_INTERVAL:
            self.spawn_count = 0
            self.enemies.append(self.factory.random_create())
```

</details>

---

## ステップ16. GameManager で衝突判定と勝敗を判定する

記載先: [game/gamecontrol.py](game/gamecontrol.py)

`update()` の後半を作る。敵ごとに「弾との衝突」「画面外に出たか」「プレイヤーとの衝突」をチェックし、消す対象を集めていく。  
ダメージ量やクリア条件も `game/gamecontrol.py` の先頭に定数として定義する。

## やること

```
step1. ファイルの先頭に BULLET_DAMAGE / ENEMY_COLLISION_DAMAGE / CLEAR_SCORE を定義する

step2. dead_enemies / dead_bullets という空の set を用意する
         （このフレームで消す対象を、リストを書き換えずに集めるため）

step3. for e in self.enemies: で敵ごとに e.update() を呼ぶ

step4. 敵と弾の衝突をチェックする
         衝突していたら playattack() を鳴らし、弾を dead_bullets に加え、
           敵の hp を BULLET_DAMAGE だけ減らす
         hp が 0 以下になったら
           notify("score") でスコアを加算する
           BombEffect を生成して effects に追加し、playblast() を鳴らす
           敵を dead_enemies に加える
           スコアが CLEAR_SCORE になったらクリア扱いにし、
             BGM を止めて playclear() を鳴らす

step5. 画面外に出た敵（is_alive が False）を dead_enemies に加える

step6. 敵とプレイヤーの衝突をチェックする
         衝突していたら敵を dead_enemies に加え、player.damage() でダメージ状態にし、
           プレイヤーの hp を ENEMY_COLLISION_DAMAGE だけ減らして playbomb() を鳴らす
         プレイヤーの hp が 0 以下になったら
           ゲームオーバーにし、BGM を止めて playover() を鳴らす
```

<details>
<summary>コードを見る</summary>

**step1.** 定数を定義する

```python
BULLET_DAMAGE          = 50
ENEMY_COLLISION_DAMAGE = 50
CLEAR_SCORE            = 30
```

**step2.** 消す対象を集める set を用意する

```python
        dead_enemies = set()
        dead_bullets = set()
```

**step3.** 敵ごとに更新する

```python
        for e in self.enemies:
            e.update()
```

**step4.** 敵と弾の衝突をチェックする

```python
            for b in self.bullets:
                if b in dead_bullets:
                    continue
                if e.rect.colliderect(b.rect):
                    sound.SoundManager.get_instance().playattack()
                    dead_bullets.add(b)
                    e.hp -= BULLET_DAMAGE
                    if e.hp <= 0:
                        self.notify("score")
                        effect = enemy.BombEffect(e.rect, self.effects)
                        sound.SoundManager.get_instance().playblast()
                        self.effects.append(effect)
                        dead_enemies.add(e)
                        if self.status.score == CLEAR_SCORE:
                            self.is_playing = False
                            self.is_cleared = True
                            sound.SoundManager.get_instance().bgmstop()
                            sound.SoundManager.get_instance().playclear()
                    break
```

**step5.** 画面外に出た敵を消す対象にする

```python
            if not e.is_alive:
                dead_enemies.add(e)
                continue
```

**step6.** 敵とプレイヤーの衝突をチェックする

```python
            if e not in dead_enemies and e.rect.colliderect(self.player.rect):
                dead_enemies.add(e)
                self.player.damage()
                self.player.hp -= ENEMY_COLLISION_DAMAGE
                sound.SoundManager.get_instance().playbomb()
                if self.player.hp <= 0:
                    self.is_playing = False
                    sound.SoundManager.get_instance().bgmstop()
                    sound.SoundManager.get_instance().playover()
```

</details>

※ `is_cleared` はここで `True` になる。`ResultScene`（ステップ18）はこの値を見て、クリア画面かゲームオーバー画面かを切り替える。

---

## ステップ17. GameManager の生存リスト整理と描画をまとめる

記載先: [game/gamecontrol.py](game/gamecontrol.py)

`update()` の最後に、消す対象に入っていないものだけでリストを作り直す。最後に `draw()` をまとめる。

## やること

```
step1. dead_enemies / dead_bullets に入っていないものだけを残して
         enemies / bullets を作り直す（Bullet だけは画面外チェックの is_alive も見る）

step2. draw(self, screen) メソッドを作る
         bullets → effects → player → enemies → status の順に draw() する
```

<details>
<summary>コードを見る</summary>

**step1.** 生き残ったものだけでリストを作り直す

```python
        alive_enemies = []
        for e in self.enemies:
            if e not in dead_enemies:
                alive_enemies.append(e)
        self.enemies = alive_enemies

        alive_bullets = []
        for b in self.bullets:
            if b not in dead_bullets and b.is_alive:
                alive_bullets.append(b)
        self.bullets = alive_bullets
```

**step2.** draw(self, screen) メソッドを作る

```python
    def draw(self, screen):
        for b in self.bullets:
            b.draw(screen)
        for eff in self.effects:
            eff.draw(screen)
        self.player.draw(screen)
        for e in self.enemies:
            e.draw(screen)
        self.status.draw(screen)
```

</details>

---

## ステップ18. ResultScene を作る

記載先: [game/resultscene.py](game/resultscene.py)

ゲームオーバー・クリア画面は `ResultScene` クラスが担当する。`is_cleared`（ステップ16で `GameManager` が設定する）を見て表示を切り替える。  
フォントサイズや表示位置は `game/resultscene.py` の先頭に定数として定義する。

## やること

```
step1. ファイルの先頭に RESULT_FONT_SIZE / RESULT_MSG_POS / RESULT_IMG_POS を定義する

step2. ResultScene クラスを作る
         __init__(self, game) で GameManager への参照を持ち、
           RESULT_FONT_SIZE でメッセージ用のフォントを作る
         update(self) で SPACE キーが押されたら game.reset() を呼ぶ
         draw(self, screen) で is_cleared を見て、RESULT_MSG_POS / RESULT_IMG_POS の位置に
           ゲームオーバー・クリア画像を出し分ける
```

<details>
<summary>コードを見る</summary>

**step1.** 定数を定義する

```python
RESULT_FONT_SIZE = 50
RESULT_MSG_POS   = (120, 380)
RESULT_IMG_POS   = (50, 200)
```

**step2.** ResultScene クラスを作る

```python
class ResultScene():
    def __init__(self, game):
        font = pg.font.Font(None, RESULT_FONT_SIZE)
        self.game      = game
        self.msg       = font.render("Press SPACE to replay.", True, pg.Color("WHITE"))
        self.gameover  = pg.image.load(IMG_DIR / "gameover.png")
        self.gameclear = pg.image.load(IMG_DIR / "gameclear.png")

    def update(self):
        key = pg.key.get_pressed()
        if key[pg.K_SPACE]:
            self.game.reset()

    def draw(self, screen):
        screen.blit(self.msg, RESULT_MSG_POS)
        if self.game.is_cleared:
            screen.blit(self.gameclear, RESULT_IMG_POS)
        else:
            screen.blit(self.gameover, RESULT_IMG_POS)
```

</details>

---

## ステップ19. main.py を完成させる

記載先: [main.py](main.py)

ステップ1・2で作った仮の main.py を、`GameManager` と `ResultScene` を使う完成版に書き換える。  
画面サイズと FPS は `main.py` の先頭に定数として定義する。

## やること

```
step1. ファイルの先頭に WIDTH, HEIGHT / FPS を定義する
step2. GameManager と ResultScene を生成する
step3. game.is_playing で分岐し、プレイ中は game.update()、そうでなければ result.update() を呼ぶ
step4. draw() も同様に、プレイ中でなければ result.draw(screen) も呼ぶ
```

<details>
<summary>コードを見る</summary>

**step1.** 定数を定義する

```python
WIDTH, HEIGHT = 600, 650
FPS = 60
```

**step2.** GameManager と ResultScene を生成する

```python
from game import GameManager, ResultScene

game   = GameManager()
result = ResultScene(game)
```

**step3.** is_playing で分岐して update() を呼ぶ

```python
if game.is_playing:
    game.update()
else:
    result.update()
```

**step4.** draw() も同様に呼び分ける

```python
game.draw(screen)
if not game.is_playing:
    result.draw(screen)
```

**組み上げた完成形**

```python
import pygame as pg
from game import GameManager, ResultScene

WIDTH, HEIGHT = 600, 650
FPS = 60

def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Frog Blaster")
    clock = pg.time.Clock()

    game   = GameManager()
    result = ResultScene(game)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill(pg.Color("NAVY"))

        if game.is_playing:
            game.update()
        else:
            result.update()

        game.draw(screen)
        if not game.is_playing:
            result.draw(screen)

        pg.display.update()
        clock.tick(FPS)

    pg.quit()

if __name__ == "__main__":
    main()
```

</details>

▶ **動作確認**: ここまでで実行し、敵の出現・弾での撃破・爆発エフェクト・スコア/距離表示・BGMと効果音・被弾やゲームオーバー・SPACEでのリトライまで、ゲームを最初から最後まで通しで遊べることを確認しよう。

---

## ステップ20. Status に経過時間を追加する

記載先: [game/status.py](game/status.py)

ステップ13で作った `Status` クラスに**経過時間の表示**を追加しよう。

## やること

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

**step1.** reset(self) に time を追加する

```python
def reset(self):
    self.distance = 0
    self.score    = 0
    self.time     = 0       # 追加
```

**step2.** update(self, ntype) で time を増やす

```python
def update(self, ntype):
    if ntype == "distance":
        self.distance += DISTANCE_PER_TICK
        self.time     += 1  # 追加
    if ntype == "score":
        self.score += 1
```

**step3.** draw(self, screen) に経過秒数を表示する

```python
def draw(self, screen):
    ...
    info3 = self.font.render(f"TIME : {self.time // 60}", True, pg.Color("WHITE"))
    screen.blit(info3, (250, 10))   # 追加
```

</details>

※ この `60`（1秒あたりのフレーム数）は `main.py` の `FPS` と同じ値だが、あえて別の定数にはしていない。`FPS` を変えると見た目の滑らかさが変わるのに対し、ここでの `60` は「時間の計算方法」を表しているだけなので、意味が異なるため。
