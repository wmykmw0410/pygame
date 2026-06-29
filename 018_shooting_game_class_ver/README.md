```text
014_shooting_game の関数ベースのコードを、クラスを使って段階的に書き直します
```

# pygame で段階的にクラス化する（シューティングゲーム）

[014_shooting_game](../014_shooting_game/) の完成コード（関数ベース）を出発点に、  
自機・UFO・弾を順番にクラスに変換していく。

| ファイル | 追加するクラス | ポイント |
| --- | --- | --- |
| [ex01.py](example/ex01.py) | なし（関数ベースの出発点） | `myrect` / `ufos` / `bulletrect` がバラバラに存在する |
| [ex02.py](example/ex02.py) | `MyShip` | 1つのインスタンス・一番シンプル |
| [ex03.py](example/ex03.py) | `MyShip` + `UFO` | リストで複数インスタンスを管理 |
| [ex04.py](example/ex04.py) | `MyShip` + `UFO` + `Bullet` | `is_active()` で発射状態を管理 |
| [ex05.py](example/ex05.py) | `MyShip` + `UFO` + `Bullet` | UFO に `speed` 属性を追加してインスタンスごとに速さを変える完成形 |

---

# ex01 → ex02: MyShip クラスに書き直す

サンプル: [ex02.py](example/ex02.py)

`myimg` と `myrect` がバラバラに存在していた自機のデータと処理を `MyShip` クラスに集約する。

## やること

```
step1. MyShip クラスを作る
         __init__(self, img) で self.img と self.rect を持たせる
         self.rect = pg.Rect(400, 500, 50, 50) で初期位置を設定する

step2. update(self, mx) を追加する
         self.rect.x = mx - 25 でマウスの X 座標に追随する

step3. draw(self) を追加する
         screen.blit(self.img, self.rect) で描画する

step4. reset(self) を追加する
         gamereset() から呼ぶ用に初期位置に戻す処理をまとめる

step5. ゲームループと gamereset() を書き直す
         myrect.x = mx - 25 → myship.update(mx)
         screen.blit(myimg, myrect) → myship.draw()
         myrect.x = 400; myrect.y = 500 → myship.reset()
```

<details>
<summary>コードを見る</summary>

```python
class MyShip():
    def __init__(self, img):
        self.img  = img
        self.rect = pg.Rect(400, 500, 50, 50)

    def update(self, mx):
        self.rect.x = mx - 25

    def draw(self):
        screen.blit(self.img, self.rect)

    def reset(self):
        self.rect.x = 400
        self.rect.y = 500


myimg  = pg.image.load(IMG_DIR / "myship.png")
myimg  = pg.transform.scale(myimg, (50, 50))
myship = MyShip(myimg)
```

```python
# gamestage() 内
myship.update(mx)
myship.draw()
```

```python
# gamereset() 内
myship.reset()
```

</details>

---

# ex02 → ex03: UFO クラスに書き直す

サンプル: [ex03.py](example/ex03.py)

`ufos` リストの中が `pg.Rect` だったものを `UFO` インスタンスに変える。  
複数インスタンスをリストで管理するパターンを確認する。

## やること

```
step1. UFO クラスを作る
         __init__(self, img, x, y) で self.img と self.rect を持たせる

step2. update(self) を追加する
         self.rect.y += 10 で下に移動する
         画面外に出たら self.rect.x / y をリセットして再登場させる

step3. draw(self) を追加する
         screen.blit(self.img, self.rect) で描画する

step4. respawn(self) を追加する
         撃墜されたときや gamereset() から呼ぶ用にランダム位置に戻す処理をまとめる

step5. ufos リストの作り方を変える
         pg.Rect(ux, uy, 50, 50) の代わりに UFO(ufoimg, x, y) を append する

step6. ゲームループと gamereset() を書き直す
         ufo.y += 10; screen.blit(ufoimg, ufo) → ufo.update(); ufo.draw()
         ufo.y = -100; ufo.x = ... → ufo.respawn()
         衝突判定: ufo.colliderect(...) → ufo.rect.colliderect(...)
```

<details>
<summary>コードを見る</summary>

```python
class UFO():
    def __init__(self, img, x, y):
        self.img  = img
        self.rect = pg.Rect(x, y, 50, 50)

    def update(self):
        self.rect.y += 10
        if self.rect.y > 600:
            self.rect.x = random.randint(0, 800)
            self.rect.y = -100

    def draw(self):
        screen.blit(self.img, self.rect)

    def respawn(self):
        self.rect.x = random.randint(0, 800)
        self.rect.y = -100


ufoimg = pg.image.load(IMG_DIR / "UFO.png")
ufoimg = pg.transform.scale(ufoimg, (50, 50))
ufos   = []
for i in range(10):
    ufos.append(UFO(ufoimg, random.randint(0, 800), -100 * i))
```

```python
# gamestage() 内
for ufo in ufos:
    ufo.update()
    ufo.draw()
    if ufo.rect.colliderect(myship.rect):
        page = 2
        pg.mixer.Sound(SOUND_DIR / "down.wav").play()
    if ufo.rect.colliderect(bulletrect):
        ufo.respawn()
        bulletrect.y = -100
        pg.mixer.Sound(SOUND_DIR / "piko.wav").play()
```

```python
# gamereset() 内
for i in range(10):
    ufos[i].respawn()
```

</details>

---

# ex03 → ex04: Bullet クラスに書き直す

サンプル: [ex04.py](example/ex04.py)

`bulletrect` と発射ロジックをバラバラに書いていたものを `Bullet` クラスに集約する。  
`is_active()` で「発射中かどうか」の状態を管理するのがポイント。

## やること

```
step1. Bullet クラスを作る
         __init__(self, img) で self.img と self.rect を持たせる
         初期位置は self.rect = pg.Rect(0, -100, 16, 16)（画面外＝待機状態）

step2. is_active(self) を追加する
         self.rect.y >= 0 のとき True（発射中）を返す

step3. shoot(self, x, y) を追加する
         is_active() が False のときだけ発射位置をセットして効果音を鳴らす
         すでに発射中は何もしない（2連射できない）

step4. update(self) を追加する
         is_active() のときだけ self.rect.y -= 15 で上に移動する

step5. draw(self) を追加する
         is_active() のときだけ描画する

step6. deactivate(self) と reset(self) を追加する
         deactivate: 撃墜したとき → self.rect.y = -100 で待機状態に戻す
         reset: gamereset() から呼ぶ用

step7. ゲームループと gamereset() を書き直す
         発射判定: if mdown[0] and bulletrect.y < 0: ... → bullet.shoot(...)
         移動・描画: バラバラな処理 → bullet.update(); bullet.draw()
         待機に戻す: bulletrect.y = -100 → bullet.deactivate()
```

<details>
<summary>コードを見る</summary>

```python
class Bullet():
    def __init__(self, img):
        self.img  = img
        self.rect = pg.Rect(0, -100, 16, 16)

    def shoot(self, x, y):
        if not self.is_active():
            self.rect.x = x
            self.rect.y = y
            pg.mixer.Sound(SOUND_DIR / "pi.wav").play()

    def update(self):
        if self.is_active():
            self.rect.y -= 15

    def draw(self):
        if self.is_active():
            screen.blit(self.img, self.rect)

    def is_active(self):
        return self.rect.y >= 0

    def deactivate(self):
        self.rect.y = -100

    def reset(self):
        self.rect.y = -100
```

```python
# gamestage() 内
if mdown[0]:
    bullet.shoot(myship.rect.x + 25 - 8, myship.rect.y)
bullet.update()
bullet.draw()

for ufo in ufos:
    ...
    if ufo.rect.colliderect(bullet.rect) and bullet.is_active():
        ufo.respawn()
        bullet.deactivate()
        pg.mixer.Sound(SOUND_DIR / "piko.wav").play()
```

</details>

---

# ex04 → ex05: UFO の速さをインスタンスごとに変える（完成）

サンプル: [ex05.py](example/ex05.py)

UFO クラスに `speed` 属性を追加して、インスタンスによって落下速度が違うようにする。

## やること

```
step1. UFO.__init__ に speed 引数を追加する
         __init__(self, img, x, y, speed) にする
         self.speed = speed で保持する

step2. update() の移動量を speed に変える
         self.rect.y += 10 → self.rect.y += self.speed にする

step3. UFO を生成するときに速さを渡す
         random.randint(5, 15) などを speed に渡すと UFO ごとに速さが変わる
```

<details>
<summary>コードを見る</summary>

```python
class UFO():
    def __init__(self, img, x, y, speed):
        self.img   = img
        self.rect  = pg.Rect(x, y, 50, 50)
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 600:
            self.rect.x = random.randint(0, 800)
            self.rect.y = -100
```

```python
ufos = []
for i in range(10):
    ufos.append(UFO(ufoimg, random.randint(0, 800), -100 * i, random.randint(5, 15)))
```

</details>

---

# 発展

`advanced/` フォルダに得点ごとに難易度が変化するバージョンがある。  
`python advanced/main.py` で起動できる。

| スコア | レベル | 移動パターン |
| --- | --- | --- |
| 0〜99 | NORMAL | 真下に落下 |
| 100〜199 | FAST | 速度アップ |
| 200〜299 | ZIGZAG | サイン波で左右に揺れながら落下 |
| 300〜 | CHASE | 自機を追尾しながら落下 |

実装の詳細は [advanced/README.md](advanced/README.md) を参照。
