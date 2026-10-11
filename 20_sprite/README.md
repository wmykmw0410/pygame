```text
pygame の Sprite / Group を使って、敵キャラを画面内でランダムに動かしてみましょう
以下のサンプルファイルを見ながら実際に動かしてみよう
```

# 目次
- [Sprite で1体を動かす](#sprite-で1体を動かす)
- [Group で複数の敵をまとめて動かす](#group-で複数の敵をまとめて動かす)
- [敵同士の衝突判定](#敵同士の衝突判定)
- [キー操作で Group を操作する](#キー操作で-group-を操作する)
- [まとめ](#まとめ)

---

# Sprite で1体を動かす

サンプル: [example/ex01.py](example/ex01.py)

複数の画像を持つオブジェクト（敵キャラなど）は、自分でリストを回して更新・描画・衝突判定するのが基本だった。  
pygame には `pg.sprite.Sprite` と `pg.sprite.Group` という専用の仕組みがあり、これを使うとそのループの多くを任せられる。

`pg.sprite.Sprite` を継承すると、`image`（描画する画像）と `rect`（位置とサイズ）を持つのが「お約束」になる。  
まずは1体だけ、ランダムな向きに動かして壁で跳ね返るようにする。

```python
FPS = 60

ENEMY_SPEED_CHOICES = [-3, -2, 2, 3]
ENEMY_START_POS     = (100, 100)


class Enemy(pg.sprite.Sprite):
    def __init__(self, img, x, y):
        super().__init__()          # ← Sprite の __init__ を呼ぶ
        self.image = img            # ← Sprite のお約束: self.image を持つ
        self.rect  = self.image.get_rect(topleft=(x, y))  # ← Sprite のお約束: self.rect を持つ
        self.vx    = random.choice(ENEMY_SPEED_CHOICES)
        self.vy    = random.choice(ENEMY_SPEED_CHOICES)

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        # 壁に当たったら跳ね返る
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.vx = -self.vx
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.vy = -self.vy
```

`vx`・`vy` は `ENEMY_SPEED_CHOICES`（0にならない値のリスト）から `random.choice()` で選ぶ。

```python
enemy_img = pg.image.load(IMG_DIR / "enemy1.png")
enemy = Enemy(enemy_img, *ENEMY_START_POS)

while True:
    ...
    enemy.update()
    screen.blit(enemy.image, enemy.rect)
    clock.tick(FPS)
```

---

# Group で複数の敵をまとめて動かす

サンプル: [example/ex02.py](example/ex02.py)

`pg.sprite.Group` にまとめると、更新も描画も1行ずつで済む。

```python
ENEMY_START_X = 100
ENEMY_START_Y = 100
ENEMY_X_GAP   = 150

enemy_imgs = [
    pg.image.load(IMG_DIR / "enemy1.png"),
    pg.image.load(IMG_DIR / "enemy2.png"),
    pg.image.load(IMG_DIR / "enemy3.png"),
]

# ── 1体のときとの違い: リストの代わりに Group を使う ──
enemies = pg.sprite.Group()
for i, img in enumerate(enemy_imgs):
    x = ENEMY_START_X + i * ENEMY_X_GAP
    y = ENEMY_START_Y
    enemies.add(Enemy(img, x, y))   # ← Group に追加する

while True:
    ...
    # ── 1体のときとの違い: for ループが不要になった ──
    enemies.update()        # ← 全員の update() をまとめて呼ぶ
    enemies.draw(screen)    # ← 全員の image を rect の位置にまとめて描画する
```

`Group` に `add()` しておけば、`update()` / `draw(screen)` の呼び出し1行で登録した全員に処理を回してくれる。

---

# 敵同士の衝突判定

サンプル: [example/ex03.py](example/ex03.py)

`Group` の中身を `sprites()` でリストに変換し、総当たりで衝突をチェックして跳ね返らせる。

```python
def bounce(self):
    self.vx = -self.vx
    self.vy = -self.vy
```

```python
enemies.update()

# ── Group をまとめて動かすだけとの違い: 敵同士の総当たりで衝突をチェックする ──
enemy_list = enemies.sprites()   # ← Group の中身をリストとして取り出す
for i in range(len(enemy_list)):
    for j in range(i + 1, len(enemy_list)):
        if enemy_list[i].rect.colliderect(enemy_list[j].rect):
            enemy_list[i].bounce()
            enemy_list[j].bounce()

enemies.draw(screen)
```

`i` より後ろの `j` だけを見ることで、同じ組み合わせを2回チェックしたり自分自身との衝突を判定したりしないようにしている。

---

# キー操作で Group を操作する

サンプル: [example/ex04.py](example/ex04.py)

自機は削除し、キー入力で直接 `Group` を操作する練習にする。  
↑キーで `Group.add()` して敵を1体増やし、↓キーで `Group.remove()` してランダムに1体減らし、  
SPACE キーで `Group.empty()` して一気に全部消す。

```python
FONT_SIZE = 28
font      = pg.font.Font(None, FONT_SIZE)
COUNT_POS = (10, 10)

MAX_ENEMIES = 20   # 増えすぎないように上限を決めておく
ENEMY_SIZE  = 50


def spawn_enemy():
    if len(enemies) >= MAX_ENEMIES:
        return
    img = random.choice(enemy_imgs)
    x   = random.randint(0, WIDTH - ENEMY_SIZE)
    y   = random.randint(0, HEIGHT - ENEMY_SIZE)
    enemies.add(Enemy(img, x, y))   # ← Group に1体追加する
```

`len(enemies) >= MAX_ENEMIES` で上限を超えないようにしてから、ランダムな画像・位置（`ENEMY_SIZE` を使って画面内に収まる範囲）で新しい `Enemy` を追加する。

```python
# ── これまでとの違い: 自機の代わりにキー入力で直接 Group を操作する ──
if event.type == pg.KEYDOWN:
    if event.key == pg.K_UP:
        spawn_enemy()
    if event.key == pg.K_DOWN:
        if len(enemies) > 0:
            enemies.remove(random.choice(enemies.sprites()))   # ← Group からランダムに1体取り除く
    if event.key == pg.K_SPACE:
        enemies.empty()   # ← Group の中身を1回で全部取り除く
```

`Group` 自体はランダムアクセスできないので、`sprites()` でいったんリストにしてから `random.choice()` でランダムに1体選ぶ。

```python
count_s = font.render(f"Enemies: {len(enemies)}", True, pg.Color("WHITE"))
screen.blit(count_s, COUNT_POS)
```

現在の敵の数を `len(enemies)` で取得し、画面に表示する。

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
