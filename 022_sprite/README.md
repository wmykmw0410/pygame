```text
pygame の Sprite / Group を使って、敵キャラを画面内でランダムに動かしてみましょう
```

# pygame.sprite で複数の画像を動かす

複数の画像を持つオブジェクト（敵キャラなど）は、自分でリストを回して更新・描画・衝突判定するのが基本だった。  
pygame には `pg.sprite.Sprite` と `pg.sprite.Group` という専用の仕組みがあり、これを使うとそのループの多くを任せられる。  
このレッスンでは、敵キャラが画面内をランダムに動き回り、壁や敵同士にぶつかったら跳ね返るだけのシンプルなプログラムで Sprite / Group の使い方を練習する。  
最後にキーボード操作で `Group` に敵を追加・削除する練習もする。

| ファイル | 内容 | ポイント |
| --- | --- | --- |
| [ex01.py](example/ex01.py) | 敵1体を `Sprite` として動かす | `image` / `rect` を持つのがお約束になる |
| [ex02.py](example/ex02.py) | `Group` で複数の敵をまとめて動かす | `update()` / `draw()` が1行で済む |
| [ex03.py](example/ex03.py) | 敵同士がぶつかったら跳ね返る | `Group` をリストに変換して総当たりで判定する |
| [ex04.py](example/ex04.py) | キーボードで敵を増やす・減らす・全部消す（完成） | `Group` の `add()` / `remove()` / `empty()` を使い分ける |

---

# ex01: Sprite クラスで1体を動かす

サンプル: [example/ex01.py](example/ex01.py)

`pg.sprite.Sprite` を継承すると、`image`（描画する画像）と `rect`（位置とサイズ）を持つのが「お約束」になる。  
まずは1体だけ、ランダムな向きに動かして壁で跳ね返るようにする。

## やること

```
step1. class Enemy(pg.sprite.Sprite): にする
step2. __init__ の最初で super().__init__() を呼ぶ
step3. self.image に画像、self.rect に位置とサイズを持たせる
         self.rect = self.image.get_rect(topleft=(x, y))
step4. vx・vy にランダムな速度を設定する
         random.choice([-3, -2, 2, 3]) のように、0にならない値から選ぶ
step5. update(self) で移動と壁での跳ね返りを実装する
         self.rect.x += self.vx / self.rect.y += self.vy で移動する
         rect.left < 0 や rect.right > WIDTH なら vx = -vx にする
         rect.top / rect.bottom も同様に vy = -vy にする
```

<details>
<summary>コードを見る</summary>

```python
class Enemy(pg.sprite.Sprite):
    def __init__(self, img, x, y):
        super().__init__()          # ← Sprite の __init__ を呼ぶ
        self.image = img            # ← Sprite のお約束: self.image を持つ
        self.rect  = self.image.get_rect(topleft=(x, y))  # ← Sprite のお約束: self.rect を持つ
        self.vx    = random.choice([-3, -2, 2, 3])
        self.vy    = random.choice([-3, -2, 2, 3])

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        # 壁に当たったら跳ね返る
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.vx = -self.vx
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.vy = -self.vy


enemy_img = pg.image.load(IMG_DIR / "enemy1.png")
enemy = Enemy(enemy_img, 100, 100)

while True:
    ...
    enemy.update()
    screen.blit(enemy.image, enemy.rect)
```

</details>

---

# ex02: Group で複数の敵を動かす

サンプル: [example/ex02.py](example/ex02.py)

`pg.sprite.Group` にまとめると、更新も描画も1行ずつで済む。

## やること

```
step1. enemies = pg.sprite.Group() でリストの代わりに Group を作る
step2. enemy1〜3.png を使って3体の Enemy インスタンスを作る
step3. enemies.add(Enemy(...)) で Group に追加する
step4. enemies.update() で全員の update() をまとめて呼ぶ
step5. enemies.draw(screen) で全員を image と rect の位置にまとめて描画する
         for ループが不要になる
```

<details>
<summary>コードを見る</summary>

```python
enemy_imgs = [
    pg.image.load(IMG_DIR / "enemy1.png"),
    pg.image.load(IMG_DIR / "enemy2.png"),
    pg.image.load(IMG_DIR / "enemy3.png"),
]

# ── ex01 との違い: リストの代わりに Group を使う ──
enemies = pg.sprite.Group()
for i, img in enumerate(enemy_imgs):
    x = 100 + i * 150
    y = 100
    enemies.add(Enemy(img, x, y))   # ← Group に追加する

while True:
    ...
    # ── ex01 との違い: for ループが不要になった ──
    enemies.update()        # ← 全員の update() をまとめて呼ぶ
    enemies.draw(screen)    # ← 全員の image を rect の位置にまとめて描画する
```

</details>

---

# ex03: 敵同士がぶつかったら跳ね返る

サンプル: [example/ex03.py](example/ex03.py)

`Group` の中身を `sprites()` でリストに変換し、総当たりで衝突をチェックして跳ね返らせる。

## やること

```
step1. Enemy に bounce(self) メソッドを追加する
         self.vx = -self.vx / self.vy = -self.vy で向きを反転する

step2. enemy_list = enemies.sprites() で Group の中身をリストとして取り出す

step3. 二重ループで全ての組み合わせを総当たりでチェックする
         for i in range(len(enemy_list)):
             for j in range(i + 1, len(enemy_list)):
         → i より後ろの j だけを見ることで、同じ組み合わせを2回・自分同士の衝突を判定しないようにする

step4. enemy_list[i].rect.colliderect(enemy_list[j].rect) が True なら
         両方の bounce() を呼んで跳ね返す
```

<details>
<summary>コードを見る</summary>

```python
def bounce(self):
    self.vx = -self.vx
    self.vy = -self.vy


while True:
    ...
    enemies.update()

    # ── ex02 との違い: 敵同士の総当たりで衝突をチェックする ──
    enemy_list = enemies.sprites()   # ← Group の中身をリストとして取り出す
    for i in range(len(enemy_list)):
        for j in range(i + 1, len(enemy_list)):
            if enemy_list[i].rect.colliderect(enemy_list[j].rect):
                enemy_list[i].bounce()
                enemy_list[j].bounce()

    enemies.draw(screen)
```

</details>

---

# ex04: キーボードで敵を増やす・減らす・全部消す（完成）

サンプル: [example/ex04.py](example/ex04.py)

自機は削除し、キー入力で直接 `Group` を操作する練習にする。  
↑キーで `Group.add()` して敵を1体増やし、↓キーで `Group.remove()` してランダムに1体減らし、  
SPACE キーで `Group.empty()` して一気に全部消す。

## やること

```
step1. Player クラスを削除する
        （自機や衝突判定は使わず、キー入力から直接 Group を操作する）

step2. spawn_enemy() 関数を作る
         len(enemies) が MAX_ENEMIES 以上なら何もせず return する（上限を超えないようにする）
         ランダムな画像・位置で新しい Enemy を作り enemies.add() で追加する

step3. Enemy.update() は壁で跳ね返るだけにする
         → ex01〜ex03 と同じシンプルな跳ね返りに戻す（spawn_enemy() は呼ばない）

step4. KEYDOWN イベントで ↑ / ↓ / SPACE を判定する
         ↑キー: spawn_enemy() を呼んで1体追加する
         ↓キー: enemies が空でなければ、enemies.sprites() でリスト化してから
                 random.choice() でランダムに1体選び、enemies.remove() で取り除く
                 → Group 自体はランダムアクセスできないので、いったんリストにする必要がある
         SPACE キー: enemies.empty() で Group の中身を一度に全部空にする

step5. 現在の敵の数を画面に表示する
         font.render(f"Enemies: {len(enemies)}", ...) で len(group) の値を確認できるようにする
```

<details>
<summary>コードを見る</summary>

```python
MAX_ENEMIES = 20   # 増えすぎないように上限を決めておく


class Enemy(pg.sprite.Sprite):
    def __init__(self, img, x, y):
        super().__init__()
        self.image = img
        self.rect  = self.image.get_rect(topleft=(x, y))
        self.vx    = random.choice([-3, -2, 2, 3])
        self.vy    = random.choice([-3, -2, 2, 3])

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        # 壁に当たったら跳ね返る（このステップでは spawn_enemy() は呼ばない）
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.vx = -self.vx
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.vy = -self.vy


def spawn_enemy():
    if len(enemies) >= MAX_ENEMIES:
        return
    img = random.choice(enemy_imgs)
    x   = random.randint(0, WIDTH - 50)
    y   = random.randint(0, HEIGHT - 50)
    enemies.add(Enemy(img, x, y))   # ← Group に1体追加する
```

```python
# ── ex03 との違い: 自機の代わりにキー入力で直接 Group を操作する ──
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                spawn_enemy()
            if event.key == pg.K_DOWN:
                if len(enemies) > 0:
                    enemies.remove(random.choice(enemies.sprites()))   # ← Group からランダムに1体取り除く
            if event.key == pg.K_SPACE:
                enemies.empty()   # ← Group の中身を1回で全部取り除く

    screen.fill(pg.Color("NAVY"))

    enemies.update()
    enemies.draw(screen)

    count_s = font.render(f"Enemies: {len(enemies)}", True, pg.Color("WHITE"))
    screen.blit(count_s, (10, 10))
```

</details>

---

# まとめ

| 機能 | 自分でリスト管理 | pygame.sprite |
| --- | --- | --- |
| 複数インスタンスの管理 | `[]` に自分で `append()` | `pg.sprite.Group()` に `add()` |
| 全員の更新 | `for` ループで `update()` を呼ぶ | `group.update()` |
| 全員の描画 | `for` ループで `blit()` する | `group.draw(screen)` |
| Group の中身をリストで扱いたい | — | `group.sprites()` |
| Group から1つ取り除く | `list.remove()` | `group.remove(sprite)` |
| Group を空にする | `list.clear()` | `group.empty()` |
