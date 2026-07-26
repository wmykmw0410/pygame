```text
クラスを使ってバトルゲームを段階的に作りましょう
```

[015_class](../015_class/README.md) の Q3 で作った `Character` → `Enemy` の継承・攻撃システムを、ここでは pygame の画面上で動かしながら拡張していく。

# 目次
- [フォントについて](#フォントについて)
  - [Webからフォントを探す](#webからフォントを探す)
- [ステップ1: CLI版をpygame化する](#ステップ1-cli版をpygame化する)
- [ステップ2: パーティー化する](#ステップ2-パーティー化する)
- [ステップ3: 攻撃ターンを追加して完成させる](#ステップ3-攻撃ターンを追加して完成させる)
- [ステップ4: 複数の敵と連戦する](#ステップ4-複数の敵と連戦する)

---

# フォントについて

`pg.font.Font(None, size)`（これまでのレッスンで使っていた既定フォント）は日本語のグリフを持っておらず、`"勇者"` のような日本語の名前を描画すると文字化けしてしまう。  
そこでこのレッスンでは、日本語対応フォント（Noto Sans CJK JP）を [fonts/NotoSansCJKjp-Regular.otf](fonts/NotoSansCJKjp-Regular.otf) として同梱し、各サンプルの冒頭で読み込んでいる。

```python
from pathlib import Path

FONT   = Path(__file__).resolve().parent.parent / "fonts" / "NotoSansCJKjp-Regular.otf"
font   = pg.font.Font(FONT, 24)   # 名前など少し大きめの文字用
font_s = pg.font.Font(FONT, 20)   # HP・メッセージなど小さめの文字用
```

| 項目 | 内容 |
| --- | --- |
| `Path(__file__).resolve().parent.parent` | サンプル自身（`example/exNN.py`）から見て1つ上の `016_battle_game/` フォルダ |
| `pg.font.Font(FONT, size)` | ファイルパスを指定してフォントを読み込む（`None` を渡すと既定フォントになる） |
| `font` / `font_s` | 同じフォントファイルからサイズ違いの2つの Font オブジェクトを作って使い分けている |

## Webからフォントを探す

自分のゲームで別のフォントを使いたいときは、無料で商用利用もできるフォント配布サイトから探すとよい。

| サイト | 特徴 |
| --- | --- |
| [Google Fonts](https://fonts.google.com/) | 無料フォントが探せる定番サイト。ほとんどが OFL（オープンフォントライセンス）で商用利用も可能 |

**日本語フォントを探すときの注意点**

```
1. Google Fonts の言語フィルタで「Japanese」を選ぶ
     → 日本語のグリフ（文字の形状データ）を持つフォントだけに絞り込める
2. 欧文フォント（Roboto など）は日本語のグリフを持っていないことが多い
     → 日本語を表示すると文字化け（豆腐（□）や表示なし）になるので注意する
```

**ダウンロードしてから使うまでの手順**

```
step1. サイトから .ttf または .otf ファイルをダウンロードする
step2. プロジェクトの fonts フォルダに置く（このレッスンでは 016_battle_game/fonts/）
step3. Path(__file__).resolve().parent.parent / "fonts" / "ファイル名" でパスを指定する
step4. pg.font.Font(FONT, サイズ) で読み込む
```

> フォントには著作権があるため、配布・商用利用が可能かライセンスを必ず確認すること。


# ステップ1: CLI版をpygame化する

サンプル: [example/ex01.py](example/ex01.py)

[015_class](../015_class/README.md) の Q3 で作った `Character`・`Enemy` クラスを、そのまま pygame の画面に表示してみよう。  
クラスの中身は変えず、`print()` の代わりに画面へ描画する。SPACE キーを押すたびに1ターン進む。

## やること

```
step1. Character・Enemy クラスは Q3 と同じものを使う
         attack(self, target) は print() の代わりにメッセージを return する
         （画面に表示するために文字列として受け取れるようにする）

step2. hero = Character("勇者", attack_power=30)
       boss = Enemy("ラスボス", attack_power=15)
         Q3 と同じ2体で戦わせる

step3. SPACE キーが押されたら1ターン進める
         hero.attack(boss) を実行し、boss が倒れていなければ boss.attack(hero) を実行する
         勝敗がついたら game_over = True にする

step4. 名前・HP・メッセージをテキストとして画面に描画する
```

<details>
<summary>コードを見る</summary>

```python
# 015_class の Q3 とまったく同じクラス（print の代わりにメッセージを返す）
class Character():
    def __init__(self, name, attack_power):
        self.name         = name
        self.hp           = 100
        self.attack_power = attack_power

    def attack(self, target):
        target.hp -= self.attack_power
        return f"{self.name}の攻撃! {target.name}に{self.attack_power}ダメージ!"

    def is_alive(self):
        return self.hp > 0


class Enemy(Character):
    def __init__(self, name, attack_power):
        super().__init__(name, attack_power)
        self.hp = 150

    def attack(self, target):
        dmg = int(self.attack_power * 1.5)
        target.hp -= dmg
        return f"{self.name}の攻撃! {target.name}に{dmg}ダメージ!"


hero = Character("勇者", attack_power=30)
boss = Enemy("ラスボス", attack_power=15)

message   = "SPACE: 攻撃"
game_over = False

while True:
    ...
    if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and not game_over:
        message = hero.attack(boss)
        if not boss.is_alive():
            message = f"{boss.name}をたおした! {hero.name}の勝利!"
            game_over = True
        else:
            message = boss.attack(hero)
            if not hero.is_alive():
                message = f"{hero.name}は倒れた… {boss.name}の勝利!"
                game_over = True
```

</details>

---

# ステップ2: パーティー化する

サンプル: [example/ex02.py](example/ex02.py)

勇者1人 vs ラスボス1体だった戦いを、3人のパーティー vs 敵1体に拡張する。  
見た目（四角形・色）を持たせるため、ステップ1では `Character` をそのまま使っていた勇者を `Player(Character)` として新しく定義し、`rect`・`color` を追加する。  
攻撃も `character.attack(target)` メソッドは使わず、メインループ側でダメージを計算して `take_damage()` を呼ぶ形に変える。ダメージにはランダムな幅も持たせる。

## やること

```
step1. Character に take_damage(self, amount) を追加する
         self.hp -= amount（0未満にはならないようにする）
         → attack(self, target) メソッドは使わず、メインループ側でダメージを計算して take_damage() を呼ぶ形に変える

step2. Player(Character) を作る
         __init__ に rect・color・attack（攻撃力）を追加する
         draw(self) でキャラ画像の代わりに四角形・名前・HPを描画する（倒れたら GRAY）

step3. Enemy(Character) にも rect・color を追加し、draw(self) を作る

step4. パーティーをリストで作る
         party = [Player("勇者", 100, ..., attack=25),
                  Player("魔法使い", 300, ..., attack=35),
                  Player("戦士", 500, ..., attack=20)]

step5. SPACE キーが押されたときの攻撃処理を実装する
         生存しているプレイヤーを alive リストに集める（for p in party: if p.is_alive(): ...）
         random.choice(alive) でランダムに1人選ぶ
         dmg = random.randint(attack-5, attack+5) でダメージを計算する
         enemy.take_damage(dmg) で HP を減らす
         message を更新する
```

<details>
<summary>コードを見る</summary>

```python
# ── ex01 との違い: Character に take_damage() を追加し、Player/Enemy は見た目(rect/color)を持つ ──
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
    def __init__(self, name, cx, color, hp, attack):
        super().__init__(name, hp)
        self.attack = attack
        self.rect   = pg.Rect(cx - 30, 230, 60, 60)
        self.color  = color

    # is_alive() / take_damage() は Character から継承

    def draw(self):
        if self.is_alive():
            color = self.color
        else:
            color = pg.Color("GRAY")
        pg.draw.rect(screen, color, self.rect)
        ...


class Enemy(Character):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.rect  = pg.Rect(270, 50, 60, 60)
        self.color = pg.Color("DARKGREEN")

    # is_alive() / take_damage() は Character から継承

    def draw(self):
        ...


enemy = Enemy("スライム", 80)
party = [
    Player("勇者",    100, pg.Color("ROYALBLUE"), hp=100, attack=25),
    Player("魔法使い", 300, pg.Color("PURPLE"),    hp=70,  attack=35),
    Player("戦士",    500, pg.Color("FIREBRICK"), hp=130, attack=20),
]

# SPACE キーで攻撃
alive = []
for p in party:
    if p.is_alive():
        alive.append(p)

attacker = random.choice(alive)
dmg = random.randint(attacker.attack - 5, attacker.attack + 5)
enemy.take_damage(dmg)   # ← Character から継承したメソッドを使う
message = f"{attacker.name}の攻撃! {dmg}ダメージ!"
```

</details>

---

# ステップ3: 攻撃ターンを追加して完成させる

サンプル: [example/ex03.py](example/ex03.py)

ステップ2に**敵の反撃**と**全滅チェック**を追加して完成。  
メッセージをリストで管理して複数行を表示できるようにする。  
また、`max_hp` を `Character` に追加し、`Enemy` にも `attack` を持たせて反撃できるようにする。

## やること

```
step1. Character に max_hp を追加する
         __init__ に self.max_hp = hp を追加する
         → is_alive() / take_damage() と同様、Enemy・Player 共通の属性として使えるようにする

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


# ── ex02 との違い: attack を追加して反撃できるようにした ──
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

# ステップ4: 複数の敵と連戦する

サンプル: [example/ex04.py](example/ex04.py)

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
# ── ex03 との違い: color / size を引数で受け取れるようにした ──
class Enemy(Character):
    def __init__(self, name, hp, attack, color="DARKGREEN", size=70):
        super().__init__(name, hp)   # ← Character の __init__ を呼ぶ
        self.attack = attack
        self.color  = pg.Color(color)
        self.rect   = pg.Rect(0, 40, size, size)
        self.rect.centerx = 300

    # is_alive() / take_damage() は Character から継承 → 書かなくてよい

    def draw(self):
        color = self.color if self.is_alive() else pg.Color("GRAY")
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
