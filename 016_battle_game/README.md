```text
クラスを使ってバトルゲームを段階的に作りましょう
```

[015_class](../015_class/README.md) の Q3 で作った `Character` → `Enemy` の継承・攻撃システムを、ここでは pygame の画面上で動かしながら拡張していく。

# 目次
- [フォントについて](#フォントについて)
  - [Webからフォントを探す](#webからフォントを探す)
- [テキストの位置合わせ（get_rect）](#テキストの位置合わせ（get_rect）)
- [ステップ1: CLI版をpygame化する](#ステップ1-cli版をpygame化する)
- [ステップ2: パーティー化して完成させる](#ステップ2-パーティー化して完成させる)
- [ステップ3: 複数の敵と連戦する](#ステップ3-複数の敵と連戦する)

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


# テキストの位置合わせ（get_rect）

`font.render()` で作った文字列の Surface をそのまま `screen.blit(text_s, (x, y))` すると、`(x, y)` は Surface の**左上**の座標になる。  
しかし HP やメッセージは表示するたびに文字数が変わるため、`(x, y)` を決め打ちすると文字数が変わるたびに見た目の中心がずれてしまう。

**具体例: 座標を決め打ちすると起きる問題**

```python
# ❌ 左上の座標を決め打ちしている
hp_s = font.render(f"HP: {self.hp}", True, WHITE)
screen.blit(hp_s, (270, 300))
```

`"HP: 100"` と `"HP: 8"` では横幅が違う（Surface のサイズが変わる）。左上の座標を固定しているので、HP が減って桁数が減ると、テキストの見た目の中心が左にずれて見える。

**解決策: get_rect()**

`Surface.get_rect(**kwargs)` は、その Surface と同じサイズの `Rect` を返すメソッド。キーワード引数で `centerx` や `top` などを指定すると、その位置に合わせて配置された `Rect` を返してくれる。

```python
name_s = font.render(self.name, True, WHITE)
screen.blit(name_s, name_s.get_rect(centerx=self.rect.centerx, bottom=self.rect.top - 6))
```

これは、実質的に次のコードを1行にまとめたものと同じ。

```python
rect = name_s.get_rect()          # Surface と同じサイズの Rect を作る（位置は (0, 0)）
rect.centerx = self.rect.centerx  # centerx だけ書き換える
rect.bottom  = self.rect.top - 6  # bottom だけ書き換える
screen.blit(name_s, rect)
```

| キーワード引数 | 意味 |
| --- | --- |
| `centerx=x` | Rect の水平方向の中心を x に合わせる |
| `centery=y` | Rect の垂直方向の中心を y に合わせる |
| `top=y` / `bottom=y` | Rect の上端 / 下端を y に合わせる |
| `left=x` / `right=x` | Rect の左端 / 右端を x に合わせる |
| `center=(x, y)` | 中心を (x, y) に合わせる |
| `topleft=(x, y)` など | `bottomleft` / `topright` / `bottomright` のように角の座標をペアで指定することもできる |

`centerx`（横方向）と `bottom`（縦方向）のように**別の軸**のキーワードなら自由に組み合わせられる。  
逆に `center` と `centerx` のように**同じ軸**を重ねて指定すると、後から適用された方が優先されて意図しない結果になるため、同じ軸は1つだけ指定する。

このレッスンでは、キャラクターの `rect`（四角形）を基準にして、名前は `rect` の少し上（`bottom=self.rect.top - 6`）、HPは少し下（`top=self.rect.bottom + 6`）に、横方向は中心を揃えて（`centerx=self.rect.centerx`）表示している。  
`get_rect()` に座標を渡しているだけで、名前や HP の文字列の長さそのものは意識しなくてよい。


# ステップ1: CLI版をpygame化する

サンプル: [example/ex01.py](example/ex01.py)

[015_class](../015_class/README.md) の Q3 で作った `Character`・`Enemy` クラスを、そのまま pygame の画面に表示してみよう。  
ダメージ計算や HP 判定のロジックは Q3 と同じまま、`print()` の代わりにメッセージを `return` して画面へ描画する。  
画面には HP を別途テキストで表示するため、メッセージ内の `(残りHP: ...)` の表記は省略している。  
画面に描画するために `rect`・`color` を `Character` に追加し、名前・HP のテキストに加えて `pg.draw.rect()` で四角形も表示する。  
SPACE キーを押すたびに1ターン進む。

## やること

```
step1. Character に rect・color を追加する
         __init__(self, name, attack_power, rect, color) にする
         attack(self, target) はダメージ計算はそのまま、print() の代わりにメッセージを return する
         （残りHPは画面に別表示するので、メッセージ文からは省く）
         is_alive(self) は Q3 と同じまま変えない

step2. Enemy(Character) の __init__ も rect・color を受け取り、super() に渡す
         super().__init__(name, attack_power, rect, color)

step3. player_rect = pg.Rect(270, 230, 60, 60)
       enemy_rect = pg.Rect(0, 40, 70, 70) → centerx を 300 にする
         player = Character("勇者", attack_power=30, rect=player_rect, color=pg.Color("ROYALBLUE"))
         enemy = Enemy("スライム", attack_power=15, rect=enemy_rect, color=pg.Color("DARKGREEN"))
         → 敵の名前は次のステップ以降も「スライム」で登場するので、ここで合わせておく

step4. SPACE キーが押されたら1ターン進める
         player.attack(enemy) を実行し、enemy が倒れていなければ enemy.attack(player) を実行する
         勝敗がついたら game_over = True にする
         → 1ターンで player と enemy 両方が攻撃するので、message とは別に sub_message も用意し、
           2つの攻撃結果を両方とも受け取れるようにする（片方だけ書き換えると、もう片方の攻撃が
           画面に表示されないまま消えてしまう）

step5. 名前・HP・メッセージをテキストとして画面に描画する
         message・sub_message をそれぞれ font_s.render() し、2行に分けて表示する

step6. player.rect・enemy.rect を使って pg.draw.rect() で四角形を描画する
         is_alive() が False なら GRAY、生きていれば self.color で描く
```

<details>
<summary>コードを見る</summary>

```python
# ── 015_class の Q3 との違い: 画面に描画するため rect・color を追加した ──
class Character():
    def __init__(self, name, attack_power, rect, color):
        self.name         = name
        self.hp           = 100
        self.attack_power = attack_power
        self.rect         = rect
        self.color        = color

    def attack(self, target):
        target.hp -= self.attack_power
        return f"{self.name}の攻撃! {target.name}に{self.attack_power}ダメージ!"

    def is_alive(self):
        return self.hp > 0


class Enemy(Character):
    def __init__(self, name, attack_power, rect, color):
        super().__init__(name, attack_power, rect, color)
        self.hp = 150

    def attack(self, target):
        dmg = int(self.attack_power * 1.5)
        target.hp -= dmg
        return f"{self.name}の攻撃! {target.name}に{dmg}ダメージ!"


player_rect = pg.Rect(270, 230, 60, 60)
enemy_rect  = pg.Rect(0, 40, 70, 70)
enemy_rect.centerx = 300

player = Character("勇者", attack_power=30, rect=player_rect, color=pg.Color("ROYALBLUE"))
enemy  = Enemy("スライム", attack_power=15, rect=enemy_rect, color=pg.Color("DARKGREEN"))

message     = "SPACE: 攻撃"
sub_message = ""   # 1ターンで player と enemy 両方が攻撃するので、2行に分けて表示する
game_over   = False

while True:
    ...
    if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and not game_over:
        sub_message = player.attack(enemy)
        if not enemy.is_alive():
            message     = f"{enemy.name}をたおした! {player.name}の勝利!"
            sub_message = ""
            game_over   = True
        else:
            message = enemy.attack(player)
            if not player.is_alive():
                message     = f"{player.name}は倒れた… {enemy.name}の勝利!"
                sub_message = ""
                game_over   = True

    if player.is_alive():
        color = player.color
    else:
        color = pg.Color("GRAY")
    pg.draw.rect(screen, color, player.rect)
```

</details>

---

# ステップ2: パーティー化して完成させる

サンプル: [example/ex02.py](example/ex02.py)

勇者1人 vs スライム1体だった戦いを、3人のパーティー vs 敵1体に拡張し、反撃・全滅チェック・メッセージ履歴を備えた完成形のバトルゲームに仕上げる。  
`Character` は `rect`・`color` を `__init__` の引数で受け取る形をそのまま使う。共通の `attack()` は一旦なくし、代わりに `take_damage()`・`draw()`・`max_hp` を追加する。  
攻撃はダメージにランダムな幅を持たせたいので、`Player`・`Enemy` それぞれに `attack(target)` メソッドを持たせ、その中で `random.randint()` でダメージを計算して `target.take_damage()` を呼ぶ形にする（ex01 と同じく `Enemy` も反撃する）。  
描画処理 `draw()` は `Player`・`Enemy` どちらも中身が同じになるため、`take_damage()` と同様に `Character` にまとめて書き、両方に継承させる。  
`attack` という名前は攻撃力(`attack_power`)とメソッド名(`attack()`)がかぶってしまうため、属性のほうは `attack_power` という名前にする。  
1ターンで player・enemy・全滅チェックと複数の出来事が起こりうるので、メッセージは `messages` リストで管理し、直近3件を画面下部に表示する。

## やること

```
step1. Character から attack(self, target) を取り除き、take_damage(self, amount) / max_hp を追加する
         self.hp -= amount（0未満にはならないようにする）
         self.max_hp = hp を __init__ に追加する
         rect・color を __init__ で受け取る形はステップ1のまま変えない

step2. Character に draw(self) も追加する
         self.rect・self.color・self.name・self.hp・self.max_hp を使って
         キャラ画像の代わりに四角形・名前・"HP: xx / max_hp" を描画する（倒れたら GRAY）
         → draw() を Character に1つ書くだけで、Player・Enemy 両方が継承して使える

step3. Player(Character) を作る
         __init__ で rect を組み立て、super().__init__(name, hp, rect, color) で Character に渡す
         attack_power（攻撃力）は Player 独自の属性として追加する
         → self.attack という名前にすると、後で追加する attack() メソッドと名前がかぶってしまうので注意
         is_alive() / take_damage() / draw() は Character から継承するので書かなくてよい

step4. Player に attack(self, target) を追加する
         dmg = random.randint(self.attack_power - 5, self.attack_power + 5) でダメージを計算する
         target.take_damage(dmg) で相手の HP を減らす（Character から継承したメソッド）
         メッセージ文字列を return する（ex01 の Character.attack() と同じ形）

step5. Enemy(Character) にも attack_power と attack(self, target) を追加する
         考え方は Player と同じだが、ダメージの幅は ±3 と Player（±5）より小さくする
         → ex01 の Enemy と同じく反撃できるようにする

step6. パーティーをリストで作る
         party = [Player("勇者", 100, ..., attack_power=25),
                  Player("魔法使い", 300, ..., attack_power=35),
                  Player("戦士", 500, ..., attack_power=20)]

step7. SPACE キーが押されたときの攻撃処理を実装する
         messages = [] にして、生存しているプレイヤーを alive リストに集める
         random.choice(alive) でランダムに1人選び、attacker.attack(enemy) の結果を messages に追加する
         enemy が倒れたら "たおした!" を追加して game_over = True
         enemy が生存していれば、別のランダムなプレイヤーを選んで enemy.attack(target) を呼び、結果を追加する

step8. 全滅チェックを実装する
         enemy の反撃で全員 is_alive() が False になったら、次に alive が空になって
         random.choice(alive) がエラーになってしまう
         → not any(p.is_alive() for p in party) で全滅を確認し、"パーティーは全滅した…" を追加して game_over = True
         全滅していなければ "SPACE: 攻撃" を追加する

step9. メッセージをリストで管理する
         messages[-3:] を画面下部に for 文で表示する（直近3件だけ表示する）
```

<details>
<summary>コードを見る</summary>

```python
# ── ex01 との違い: Character 共通の attack() をやめ、take_damage() / draw() / max_hp を追加した ──
class Character():
    def __init__(self, name, hp, rect, color):
        self.name   = name
        self.hp     = hp
        self.max_hp = hp
        self.rect   = rect
        self.color  = color

    def is_alive(self):
        return self.hp > 0

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
        hp_s = font_s.render(f"HP: {self.hp} / {self.max_hp}", True, WHITE)
        ...


class Player(Character):
    def __init__(self, name, cx, color, hp, attack_power):
        rect = pg.Rect(cx - 30, 200, 60, 60)
        super().__init__(name, hp, rect, color)   # ← Character の __init__ を呼ぶ
        self.attack_power = attack_power

    # is_alive() / take_damage() / draw() は Character から継承

    def attack(self, target):
        dmg = random.randint(self.attack_power - 5, self.attack_power + 5)
        target.take_damage(dmg)   # ← Character から継承したメソッドを使う
        return f"{self.name}の攻撃! {dmg}ダメージ!"


# ── ex01 との違い: attack_power / attack() を追加して反撃できるようにした ──
class Enemy(Character):
    def __init__(self, name, hp, attack_power):
        rect = pg.Rect(0, 40, 70, 70)
        rect.centerx = 300
        super().__init__(name, hp, rect, pg.Color("DARKGREEN"))   # ← Character の __init__ を呼ぶ
        self.attack_power = attack_power

    # is_alive() / take_damage() / draw() は Character から継承

    def attack(self, target):
        dmg = random.randint(self.attack_power - 3, self.attack_power + 3)
        target.take_damage(dmg)
        return f"{self.name}の反撃! {target.name}に{dmg}ダメージ!"


enemy = Enemy("スライム", 80, 12)
party = [
    Player("勇者",    100, pg.Color("ROYALBLUE"), hp=100, attack_power=25),
    Player("魔法使い", 300, pg.Color("PURPLE"),    hp=70,  attack_power=35),
    Player("戦士",    500, pg.Color("FIREBRICK"), hp=130, attack_power=20),
]

messages  = ["スライムが現れた！", "SPACE: 攻撃"]
game_over = False

# SPACE キーで攻撃
messages = []

alive = []
for p in party:
    if p.is_alive():
        alive.append(p)

attacker = random.choice(alive)
messages.append(attacker.attack(enemy))   # ← Player の attack() を呼ぶ

if not enemy.is_alive():
    messages.append("スライムをたおした!")
    game_over = True
else:
    # 敵の反撃
    target = random.choice(alive)
    messages.append(enemy.attack(target))   # ← Enemy の attack() を呼ぶ

    # 全滅チェック（enemy の反撃で全員倒れたら、次の alive が空になってしまうため）
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

# ステップ3: 複数の敵と連戦する

サンプル: [example/ex03.py](example/ex03.py)

スライムを倒したら**ドラゴン**が現れる連戦システムを追加する。  
`enemy_queue` で戦う順序を管理し、Enemy クラスに `color` と `size` を追加して見た目を変える。

## やること

```
step1. Enemy に color と size 引数を追加する
         __init__(self, name, hp, attack_power, color="DARKGREEN", size=70)
           rect = pg.Rect(0, 40, size, size) を組み立てて super() に渡す
           super().__init__(name, hp, rect, pg.Color(color))
         draw(self) / attack(self, target) はそのまま self.color・self.name を使う（変更不要）
         → attack() のメッセージはすでに self.name から組み立てているので、
           ドラゴンに交代しても自動的に「ドラゴンの反撃!」になる

step2. enemy_queue を用意する
         enemy_queue = [Enemy("ドラゴン", 200, 20, color="DARKRED", size=90)]
         enemy = Enemy("スライム", 80, 12)  ← 最初の敵はこれまで通り

step3. 敵を倒したときの処理を変更する
         enemy.is_alive() が False になったら f"{enemy.name}をたおした!" と表示する
         enemy_queue が空でなければ pop(0) で次の敵を取り出して enemy に代入する
         次の敵の名前で "〇〇が現れた！" を表示する
         enemy_queue が空なら "全ての敵をたおした!" を表示して game_over = True
```

<details>
<summary>コードを見る</summary>

```python
# ── ex02 との違い: color / size を引数で受け取れるようにした ──
class Enemy(Character):
    def __init__(self, name, hp, attack_power, color="DARKGREEN", size=70):
        rect = pg.Rect(0, 40, size, size)
        rect.centerx = 300
        super().__init__(name, hp, rect, pg.Color(color))   # ← Character の __init__ を呼ぶ
        self.attack_power = attack_power

    # is_alive() / take_damage() / draw() は Character から継承 → 書かなくてよい

    def attack(self, target):
        dmg = random.randint(self.attack_power - 3, self.attack_power + 3)
        target.take_damage(dmg)
        return f"{self.name}の反撃! {target.name}に{dmg}ダメージ!"   # ← self.name なので敵が変わっても自動で対応


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
        messages.append("全ての敵をたおした!")
        game_over = True
```

</details>
