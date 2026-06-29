```text
クラスを使ってバトルゲームを段階的に作りましょう
```

# 目次
- [関数で書く問題点](#関数で書く問題点)
- [ステップ1: 関数で書く](#ステップ1-関数で書く)
- [ステップ2: Player クラスにまとめる](#ステップ2-player-クラスにまとめる)
- [ステップ3: Character 基底クラスを作り、Player・Enemy を派生させる](#ステップ3-character-基底クラスを作りplayerenemy-を派生させる)
- [ステップ4: 攻撃ターンを追加して完成させる](#ステップ4-攻撃ターンを追加して完成させる)
- [ステップ5: 複数の敵と連戦する](#ステップ5-複数の敵と連戦する)


---

# 関数で書く問題点

プレイヤーを**関数**だけで管理すると、人数が増えるほど変数がどんどん増えていく。

```python
# プレイヤー3人分を変数で管理
name1, hp1, color1 = "勇者",    100, pg.Color("ROYALBLUE")
name2, hp2, color2 = "魔法使い",  70, pg.Color("PURPLE")
name3, hp3, color3 = "戦士",    130, pg.Color("FIREBRICK")

# 描画するたびに3回呼ぶ必要がある
draw_player(name1, 100, color1, hp1)
draw_player(name2, 300, color2, hp2)
draw_player(name3, 500, color3, hp3)
```

4人目が加わったら？ → 変数と呼び出しがさらに増える。

→ 「1人分のデータと処理」をひとまとめにできれば、何人でも同じコードで扱えるはず。

---

# ステップ1: 関数で書く

サンプル: [example/ex01.py](example/ex01.py)

まず関数版を動かして、変数が増えていく問題を体感しよう。

## やること

```
step1. プレイヤー3人分のデータを変数で定義する
         name1, hp1, color1 = "勇者", 100, pg.Color("ROYALBLUE")  など

step2. draw_player(name, cx, color, hp) 関数を定義する
         四角 pg.Rect(cx-30, 200, 60, 60) を描く
         名前を四角の上に、HP を四角の下に表示する

step3. メインループで SPACE キーが押されたら全員の hp を 10 減らす
         hp1 -= 10 / hp2 -= 10 / hp3 -= 10

step4. draw_player を3回呼んで全員を描画する
```

<details>
<summary>コードを見る</summary>

```python
name1, hp1, color1 = "勇者",    100, pg.Color("ROYALBLUE")
name2, hp2, color2 = "魔法使い",  70, pg.Color("PURPLE")
name3, hp3, color3 = "戦士",    130, pg.Color("FIREBRICK")


def draw_player(name, cx, color, hp):
    rect = pg.Rect(cx - 30, 200, 60, 60)
    pg.draw.rect(screen, color, rect)
    name_s = font.render(name, True, WHITE)
    screen.blit(name_s, name_s.get_rect(centerx=cx, bottom=194))
    hp_s = font_s.render(f"HP: {hp}", True, WHITE)
    screen.blit(hp_s, hp_s.get_rect(centerx=cx, top=266))


while True:
    ...
    if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
        hp1 -= 10
        hp2 -= 10
        hp3 -= 10

    draw_player(name1, 100, color1, hp1)
    draw_player(name2, 300, color2, hp2)
    draw_player(name3, 500, color3, hp3)
```

</details>

---

# ステップ2: Player クラスにまとめる

サンプル: [example/ex02.py](example/ex02.py)

ステップ1の変数と関数を `Player` クラスに集約する。  
→ リストに入れて for 文でまとめて処理できるようになることを確認する。

## やること

```
step1. Player クラスを定義する
         __init__(self, name, cx, color, hp)
           self.name  = name
           self.hp    = hp
           self.rect  = pg.Rect(cx - 30, 200, 60, 60)
           self.color = color

step2. take_damage(self, amount) メソッドを作る
         self.hp -= amount
         0 未満にはならないようにする

step3. draw(self) メソッドを作る
         四角・名前・HP を描画する（ステップ1の draw_player と同じ内容）

step4. パーティーをリストで作る
         party = [Player("勇者", 100, ...), Player("魔法使い", 300, ...), ...]

step5. SPACE キーで for 文を使って全員に 10 ダメージを与える
         for p in party: p.take_damage(10)

step6. for 文で全員を描画する
         for p in party: p.draw()
```

<details>
<summary>コードを見る</summary>

```python
class Player():
    def __init__(self, name, cx, color, hp):
        self.name  = name
        self.hp    = hp
        self.rect  = pg.Rect(cx - 30, 200, 60, 60)
        self.color = color

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def draw(self):
        pg.draw.rect(screen, self.color, self.rect)
        name_s = font.render(self.name, True, WHITE)
        screen.blit(name_s, name_s.get_rect(centerx=self.rect.centerx, bottom=self.rect.top - 6))
        hp_s = font_s.render(f"HP: {self.hp}", True, WHITE)
        screen.blit(hp_s, hp_s.get_rect(centerx=self.rect.centerx, top=self.rect.bottom + 6))


party = [
    Player("勇者",    100, pg.Color("ROYALBLUE"), hp=100),
    Player("魔法使い", 300, pg.Color("PURPLE"),    hp=70),
    Player("戦士",    500, pg.Color("FIREBRICK"), hp=130),
]

while True:
    ...
    if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
        for p in party:
            p.take_damage(10)   # まとめて処理できる

    for p in party:
        p.draw()
```

</details>

---

# ステップ3: Character 基底クラスを作り、Player・Enemy を派生させる

サンプル: [example/ex03.py](example/ex03.py)

`Player` と `Enemy` の共通部分（名前・HP・生死判定）を先に `Character` としてまとめ、  
`Player(Character)` → `Enemy(Character)` の順に派生させる。  
→ 基底クラス → 派生クラスの順で考える流れを身につける。

## やること

```
step1. Character 基底クラスを定義する
         __init__(self, name, hp)
           self.name = name
           self.hp   = hp
         is_alive(self): return self.hp > 0

step2. Player(Character) に書き直す
         super().__init__(name, hp) で親の初期化を呼ぶ
         Player 固有の属性だけを __init__ に追加する
           self.attack = attack
           self.rect   = pg.Rect(cx - 30, 230, 60, 60)
           self.color  = color
         is_alive() は Character から継承されるので削除する

step3. Enemy(Character) を定義する
         super().__init__(name, hp) で親の初期化を呼ぶ
         Enemy 固有の属性だけを __init__ に追加する
           self.rect  = pg.Rect(270, 50, 60, 60)
           self.color = pg.Color("DARKGREEN")
         is_alive() は Character から継承されるので書かなくてよい
         draw(self): 四角・名前・HP を描画する（倒れたら GRAY）

step4. SPACE キーが押されたときの攻撃処理を実装する
         生存しているプレイヤーを alive リストに集める
         random.choice(alive) でランダムに1人選ぶ
         dmg = random.randint(attack-5, attack+5) でダメージを計算する
         enemy.hp -= dmg で HP を減らす
         message を更新する
```

<details>
<summary>コードを見る</summary>

```python
class Character():
    def __init__(self, name, hp):
        self.name = name
        self.hp   = hp

    def is_alive(self):
        return self.hp > 0


class Player(Character):
    def __init__(self, name, cx, color, hp, attack):
        super().__init__(name, hp)   # ← Character の __init__ を呼ぶ
        self.attack = attack
        self.rect   = pg.Rect(cx - 30, 230, 60, 60)
        self.color  = color

    # is_alive() は Character から継承 → 書かなくてよい

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def draw(self):
        color = self.color if self.is_alive() else pg.Color("GRAY")
        pg.draw.rect(screen, color, self.rect)
        ...


class Enemy(Character):
    def __init__(self, name, hp):
        super().__init__(name, hp)   # ← Character の __init__ を呼ぶ
        self.rect  = pg.Rect(270, 50, 60, 60)
        self.color = pg.Color("DARKGREEN")

    # is_alive() は Character から継承 → 書かなくてよい

    def draw(self):
        color = self.color if self.is_alive() else pg.Color("GRAY")
        pg.draw.rect(screen, color, self.rect)
        ...


# SPACE キーで攻撃
alive = []
for p in party:
    if p.is_alive():
        alive.append(p)

attacker = random.choice(alive)
dmg = random.randint(attacker.attack - 5, attacker.attack + 5)
enemy.hp -= dmg
if enemy.hp < 0:
    enemy.hp = 0
message = f"{attacker.name}の攻撃! {dmg}ダメージ!"
```

</details>

---

# ステップ4: 攻撃ターンを追加して完成させる

サンプル: [example/ex04.py](example/ex04.py)

ステップ3に**敵の反撃**と**全滅チェック**を追加して完成。  
メッセージをリストで管理して複数行を表示できるようにする。

## やること

```
step1. Enemy に attack と max_hp を追加する
         __init__ に self.attack = attack / self.max_hp = hp を追加する
         draw(self) で "HP: xx / max_hp" 形式で表示する

step2. Player に max_hp を追加する
         __init__ に self.max_hp = hp を追加する

step3. 敵の反撃を実装する
         パーティーの攻撃後、enemy が生存していたら反撃する
         random.choice(alive) でランダムなプレイヤーを選ぶ
         edm = random.randint(enemy.attack-3, enemy.attack+3) でダメージ計算
         target.take_damage(edm) で HP を減らす

step4. 全滅チェックを実装する
         全員 is_alive() が False なら "パーティーは全滅した…" を表示して game_over = True

step5. メッセージをリストで管理する
         messages = [] に append() で追加する
         messages[-3:] を画面下部に for 文で表示する
```

<details>
<summary>コードを見る</summary>

```python
if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and not game_over:
    messages = []

    # パーティーの攻撃
    alive = [p for p in party if p.is_alive()]  # ← リスト内包表記でも書ける
    attacker = random.choice(alive)
    dmg = random.randint(attacker.attack - 5, attacker.attack + 5)
    enemy.hp = max(0, enemy.hp - dmg)
    messages.append(f"{attacker.name}の攻撃! {dmg}ダメージ!")

    if not enemy.is_alive():
        messages.append("スライムをたおした!")
        game_over = True
    else:
        # 敵の反撃
        target = random.choice(alive)
        edm = random.randint(enemy.attack - 3, enemy.attack + 3)
        target.take_damage(edm)
        messages.append(f"スライムの反撃! {target.name}に{edm}ダメージ!")

        # 全滅チェック
        if not any(p.is_alive() for p in party):
            messages.append("パーティーは全滅した…")
            game_over = True
        else:
            messages.append("SPACE: 攻撃")

# メッセージ表示
show_msgs = messages[-3:]
line_h  = font_s.get_linesize()
start_y = 400 - line_h * len(show_msgs) - 4
for i, msg in enumerate(show_msgs):
    s = font_s.render(msg, True, pg.Color("WHITE"))
    screen.blit(s, s.get_rect(centerx=300, top=start_y + i * line_h))
```

</details>

---

# ステップ5: 複数の敵と連戦する

サンプル: [example/ex05.py](example/ex05.py)

スライムを倒したら**ドラゴン**が現れる連戦システムを追加する。  
`enemy_queue` で戦う順序を管理し、Enemy クラスに `color` と `size` を追加して見た目を変える。

## やること

```
step1. Enemy に color と size 引数を追加する
         __init__(self, name, hp, attack, color="DARKGREEN", size=70)
           self.color_alive = pg.Color(color)
           self.rect        = pg.Rect(0, 40, size, size)
         draw(self) で self.color_alive を使うように変更する

step2. enemy_queue を用意する
         enemy_queue = [Enemy("ドラゴン", 200, 20, color="DARKRED", size=90)]
         enemy = Enemy("スライム", 80, 12)  ← 最初の敵はこれまで通り

step3. 敵を倒したときの処理を変更する
         enemy.is_alive() が False になったら f"{enemy.name}をたおした！" と表示する
         enemy_queue が空でなければ pop(0) で次の敵を取り出して enemy に代入する
         次の敵の名前で "〇〇が現れた！" を表示する
         enemy_queue が空なら "全ての敵をたおした！" を表示して game_over = True

step4. メッセージ内の敵名をハードコードから enemy.name に変える
         "スライムの反撃!" → f"{enemy.name}の反撃!"
```

<details>
<summary>コードを見る</summary>

```python
class Enemy():
    def __init__(self, name, hp, attack, color="DARKGREEN", size=70):
        ...
        self.color_alive = pg.Color(color)
        self.rect        = pg.Rect(0, 40, size, size)
        self.rect.centerx = 300

    def draw(self):
        color = self.color_alive if self.is_alive() else pg.Color("GRAY")
        ...


enemy_queue = [
    Enemy("ドラゴン", 200, 20, color="DARKRED", size=90),
]
enemy = Enemy("スライム", 80, 12)

# 敵を倒したとき
if not enemy.is_alive():
    messages.append(f"{enemy.name}をたおした!")
    if enemy_queue:
        enemy = enemy_queue.pop(0)
        messages.append(f"{enemy.name}が現れた！")
        messages.append("SPACE: 攻撃")
    else:
        messages.append("全ての敵をたおした！")
        game_over = True
```

</details>

