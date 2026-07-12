```text
クラスを使ってバトルゲームを段階的に作りましょう
```

# 目次
- [ステップ1: サンプルプログラムを確認する](#ステップ1-サンプルプログラムを確認する)
- [ステップ2: Player クラスにまとめる](#ステップ2-player-クラスにまとめる)
- [ステップ3: Character 基底クラスを作る](#ステップ3-character-基底クラスを作る)
- [ステップ4: Enemy を派生させ、パーティーをリストで管理する](#ステップ4-enemy-を派生させパーティーをリストで管理する)
- [ステップ5: 攻撃ターンを追加して完成させる](#ステップ5-攻撃ターンを追加して完成させる)
- [ステップ6: 複数の敵と連戦する](#ステップ6-複数の敵と連戦する)


---

# ステップ1: サンプルプログラムを確認する

サンプル: [example/ex01.py](example/ex01.py)

プレイヤーを**関数**だけで管理すると、人数が増えるほど変数がどんどん増えていく。  
関数版のサンプルを確認して、この問題を体感しよう。  
実装はステップ2から始める。

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

4人目が加わったら？ → 変数と呼び出しがさらに増える。

→ 「1人分のデータと処理」をひとまとめにできれば、何人でも同じコードで扱えるはず。

---

# ステップ2: Player クラスにまとめる

サンプル: [example/ex02.py](example/ex02.py)

ここから実装していく。ステップ1の変数と関数を `Player` クラスに集約する。  
→ 勇者1人分のデータと処理を1つのオブジェクトにまとめて描画する。

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

step4. 勇者のインスタンスを1つ作る
         hero = Player("勇者", 300, pg.Color("ROYALBLUE"), hp=100)

step5. SPACE キーが押されたら hero に 10 ダメージを与える
         hero.take_damage(10)

step6. hero を描画する
         hero.draw()
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


hero = Player("勇者", 300, pg.Color("ROYALBLUE"), hp=100)

while True:
    ...
    if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
        hero.take_damage(10)

    hero.draw()
```

</details>

---

# ステップ3: Character 基底クラスを作る

サンプル: [example/ex03.py](example/ex03.py)

`Player` の中身を先に `Character` 基底クラスとしてまとめ、`Player(Character)` として派生させる。  
→ 次のステップで `Enemy` も同じ `Character` から派生させる準備をする。

## やること

```
step1. Character 基底クラスを定義する
         __init__(self, name, hp)
           self.name = name
           self.hp   = hp
         is_alive(self): return self.hp > 0
         take_damage(self, amount): self.hp -= amount（0未満にはならないようにする）

step2. Player(Character) に書き直す
         super().__init__(name, hp) で親の初期化を呼ぶ
         Player 固有の属性だけを __init__ に追加する
           self.rect  = pg.Rect(cx - 30, 200, 60, 60)
           self.color = color
         is_alive() / take_damage() は Character から継承されるので削除する

step3. draw(self) メソッドを直す
         is_alive() が False なら GRAY で描画するようにする

step4. 勇者のインスタンスを1つ作る
         hero = Player("勇者", 300, pg.Color("ROYALBLUE"), hp=100)
         SPACE キーで hero.take_damage(10) を呼び、ステップ2と同じ挙動になることを確認する
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

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0


class Player(Character):
    def __init__(self, name, cx, color, hp):
        super().__init__(name, hp)   # ← Character の __init__ を呼ぶ
        self.rect  = pg.Rect(cx - 30, 200, 60, 60)
        self.color = color

    # is_alive() / take_damage() は Character から継承 → 書かなくてよい

    def draw(self):
        if self.is_alive():
            color = self.color
        else:
            color = pg.Color("GRAY")
        pg.draw.rect(screen, color, self.rect)
        name_s = font.render(self.name, True, WHITE)
        screen.blit(name_s, name_s.get_rect(centerx=self.rect.centerx, bottom=self.rect.top - 6))
        hp_s = font_s.render(f"HP: {self.hp}", True, WHITE)
        screen.blit(hp_s, hp_s.get_rect(centerx=self.rect.centerx, top=self.rect.bottom + 6))


hero = Player("勇者", 300, pg.Color("ROYALBLUE"), hp=100)

while True:
    ...
    if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
        hero.take_damage(10)

    hero.draw()
```

</details>

---

# ステップ4: Enemy を派生させ、パーティーをリストで管理する

サンプル: [example/ex04.py](example/ex04.py)

ステップ3の `Character` から `Enemy` も派生させ、`Player` と共通の基底クラスを持たせる。  
→ 基底クラス → 複数の派生クラスという構造を身につける。  
また、ステップ3では勇者1人だけだったプレイヤーを、パーティー（複数人）のリストにする。

## やること

```
step1. Player(Character) に attack 属性を追加する
         __init__ に self.attack = attack を追加する

step2. パーティーをリストで作る
         party = [Player("勇者", 100, ..., attack=25),
                  Player("魔法使い", 300, ..., attack=35),
                  Player("戦士", 500, ..., attack=20)]
         勇者1人だけだったステップ3から、複数人をリストで管理できるようにする

step3. Enemy(Character) を定義する
         super().__init__(name, hp) で親の初期化を呼ぶ
         Enemy 固有の属性だけを __init__ に追加する
           self.rect  = pg.Rect(270, 50, 60, 60)
           self.color = pg.Color("DARKGREEN")
         is_alive() は Character から継承されるので書かなくてよい
         draw(self): 四角・名前・HP を描画する（倒れたら GRAY）

step4. SPACE キーが押されたときの攻撃処理を実装する
         生存しているプレイヤーを alive リストに集める（for p in party: if p.is_alive(): ...）
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
        if self.is_alive():
            color = self.color
        else:
            color = pg.Color("GRAY")
        pg.draw.rect(screen, color, self.rect)
        ...


class Enemy(Character):
    def __init__(self, name, hp):
        super().__init__(name, hp)   # ← Character の __init__ を呼ぶ
        self.rect  = pg.Rect(270, 50, 60, 60)
        self.color = pg.Color("DARKGREEN")

    # is_alive() は Character から継承 → 書かなくてよい

    def draw(self):
        if self.is_alive():
            color = self.color
        else:
            color = pg.Color("GRAY")
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

# ステップ5: 攻撃ターンを追加して完成させる

サンプル: [example/ex05.py](example/ex05.py)

ステップ4に**敵の反撃**と**全滅チェック**を追加して完成。  
メッセージをリストで管理して複数行を表示できるようにする。  
また、`max_hp` と `take_damage()` を `Character` に移し、`Enemy` も `Player` と同じ基底クラスから継承する形に直す。

## やること

```
step1. Character に max_hp と take_damage() を追加する
         __init__ に self.max_hp = hp を追加する
         take_damage(self, amount): self.hp -= amount（0未満にはならないようにする）
         → Enemy・Player 共通のダメージ処理として使えるようにする

step2. Player・Enemy の draw() を "HP: xx / max_hp" 形式に変える
         hp_s = font_s.render(f"HP: {self.hp} / {self.max_hp}", ...)

step3. Enemy(Character) に attack を追加する
         __init__ に self.attack = attack を追加する
         is_alive() / take_damage() は Character から継承されるので書かなくてよい

step4. 敵の反撃を実装する
         パーティーの攻撃後、enemy が生存していたら反撃する
         random.choice(alive) でランダムなプレイヤーを選ぶ
         edm = random.randint(enemy.attack-3, enemy.attack+3) でダメージ計算
         target.take_damage(edm) で HP を減らす（Character から継承したメソッド）

step5. 全滅チェックを実装する
         全員 is_alive() が False なら "パーティーは全滅した…" を表示して game_over = True

step6. メッセージをリストで管理する
         messages = [] に append() で追加する
         messages[-3:] を画面下部に for 文で表示する
```

<details>
<summary>コードを見る</summary>

```python
class Character():
    def __init__(self, name, hp):
        self.name   = name
        self.hp     = hp
        self.max_hp = hp

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0


class Player(Character):
    def __init__(self, name, cx, color, hp, attack):
        super().__init__(name, hp)   # ← Character の __init__ を呼ぶ
        self.attack = attack
        self.rect   = pg.Rect(cx - 30, 230, 60, 60)
        self.color  = color

    # is_alive() / take_damage() は Character から継承 → 書かなくてよい

    def draw(self):
        if self.is_alive():
            color = self.color
        else:
            color = pg.Color("GRAY")
        pg.draw.rect(screen, color, self.rect)
        ...
        hp_s = font_s.render(f"HP: {self.hp} / {self.max_hp}", True, WHITE)
        ...


# ── ex04 との違い: Enemy も Character(Player と同じ基底クラス)から派生させた ──
class Enemy(Character):
    def __init__(self, name, hp, attack):
        super().__init__(name, hp)   # ← Character の __init__ を呼ぶ
        self.attack = attack
        self.rect   = pg.Rect(0, 40, 70, 70)
        self.rect.centerx = 300
        self.color  = pg.Color("DARKGREEN")

    # is_alive() / take_damage() は Character から継承 → 書かなくてよい

    def draw(self):
        if self.is_alive():
            color = self.color
        else:
            color = pg.Color("GRAY")
        pg.draw.rect(screen, color, self.rect)
        ...
        hp_s = font_s.render(f"HP: {self.hp} / {self.max_hp}", True, WHITE)
        ...


if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and not game_over:
    messages = []

    # パーティーの攻撃
    alive = []
    for p in party:
        if p.is_alive():
            alive.append(p)
    attacker = random.choice(alive)
    dmg = random.randint(attacker.attack - 5, attacker.attack + 5)
    enemy.take_damage(dmg)   # ← Character から継承したメソッドを使う
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

# ステップ6: 複数の敵と連戦する

サンプル: [example/ex06.py](example/ex06.py)

スライムを倒したら**ドラゴン**が現れる連戦システムを追加する。  
`enemy_queue` で戦う順序を管理し、Enemy クラスに `color` と `size` を追加して見た目を変える。

## やること

```
step1. Enemy に color と size 引数を追加する
         __init__(self, name, hp, attack, color="DARKGREEN", size=70)
           self.color = pg.Color(color)
           self.rect  = pg.Rect(0, 40, size, size)
         draw(self) はそのまま self.color を使う（変更不要）

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
# ── ex05 との違い: color / size を引数で受け取れるようにした ──
class Enemy(Character):
    def __init__(self, name, hp, attack, color="DARKGREEN", size=70):
        super().__init__(name, hp)   # ← Character の __init__ を呼ぶ
        self.attack = attack
        self.color  = pg.Color(color)
        self.rect   = pg.Rect(0, 40, size, size)
        self.rect.centerx = 300

    # is_alive() / take_damage() は Character から継承 → 書かなくてよい

    def draw(self):
        if self.is_alive():
            color = self.color
        else:
            color = pg.Color("GRAY")
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

