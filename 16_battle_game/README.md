```text
クラスを使ってバトルゲームを段階的に作りましょう
```

[15_class](../15_class/README.md) の Q3 で作った `Character` → `Enemy` の継承・攻撃システムを、ここでは pygame の画面上で動かしながら拡張していく。

# 目次
- [フォントについて](#フォントについて)
  - [Webからフォントを探す](#webからフォントを探す)
- [テキストの位置合わせ（get_rect）](#テキストの位置合わせget_rect)
- [キャラクターを画像で表示する](#キャラクターを画像で表示する)
- [ex01 — CLI版をpygame化する](#ex01--cli版をpygame化する)
  - [ステップ1. ライブラリを読み込んで初期化する](#ステップ1-ライブラリを読み込んで初期化する)
  - [ステップ2. ウィンドウを作る](#ステップ2-ウィンドウを作る)
  - [ステップ3. 日本語フォントを読み込む](#ステップ3-日本語フォントを読み込む)
  - [ステップ4. 画像を読み込む](#ステップ4-画像を読み込む)
  - [ステップ5. Character クラスを作る](#ステップ5-character-クラスを作る)
  - [ステップ6. attack() と is_alive() を書く](#ステップ6-attack-と-is_alive-を書く)
  - [ステップ7. Enemy クラスを作る](#ステップ7-enemy-クラスを作る)
  - [ステップ8. キャラクターを作る](#ステップ8-キャラクターを作る)
  - [ステップ9. メッセージとゲーム終了の変数を作る](#ステップ9-メッセージとゲーム終了の変数を作る)
  - [ステップ10. メインループを作る](#ステップ10-メインループを作る)
  - [ステップ11. SPACEキーで1ターン進める](#ステップ11-spaceキーで1ターン進める)
  - [ステップ12. 背景を塗りつぶす](#ステップ12-背景を塗りつぶす)
  - [ステップ13. 勇者を描く](#ステップ13-勇者を描く)
  - [ステップ14. 敵を描く](#ステップ14-敵を描く)
  - [ステップ15. メッセージを描く](#ステップ15-メッセージを描く)
  - [ステップ16. 画面を更新する](#ステップ16-画面を更新する)
- [ex02 — パーティー化して完成させる](#ex02--パーティー化して完成させる)
  - [ステップ17. random を読み込み、タイトルを変える](#ステップ17-random-を読み込みタイトルを変える)
  - [ステップ18. 仲間の画像を足す](#ステップ18-仲間の画像を足す)
  - [ステップ19. Character の __init__ を書き換える](#ステップ19-character-の-__init__-を書き換える)
  - [ステップ20. attack() を消して、take_damage() を足す](#ステップ20-attack-を消してtake_damage-を足す)
  - [ステップ21. draw() を足す](#ステップ21-draw-を足す)
  - [ステップ22. Player クラスを作る](#ステップ22-player-クラスを作る)
  - [ステップ23. Player の attack() を書く](#ステップ23-player-の-attack-を書く)
  - [ステップ24. Enemy クラスを書き換える](#ステップ24-enemy-クラスを書き換える)
  - [ステップ25. Enemy の attack() を書く](#ステップ25-enemy-の-attack-を書く)
  - [ステップ26. 敵とパーティーを作る](#ステップ26-敵とパーティーを作る)
  - [ステップ27. メッセージをリストにする](#ステップ27-メッセージをリストにする)
  - [ステップ28. 生き残っている仲間から、攻撃する人を選ぶ](#ステップ28-生き残っている仲間から攻撃する人を選ぶ)
  - [ステップ29. 敵を倒したときの処理](#ステップ29-敵を倒したときの処理)
  - [ステップ30. 敵が反撃する](#ステップ30-敵が反撃する)
  - [ステップ31. 全滅したか調べる](#ステップ31-全滅したか調べる)
  - [ステップ32. キャラクターを描く](#ステップ32-キャラクターを描く)
  - [ステップ33. メッセージを描く](#ステップ33-メッセージを描く)
- [ex03 — 複数の敵と連戦する](#ex03--複数の敵と連戦する)
  - [ステップ34. ドラゴンの画像を読み込む](#ステップ34-ドラゴンの画像を読み込む)
  - [ステップ35. Enemy に image と size を足す](#ステップ35-enemy-に-image-と-size-を足す)
  - [ステップ36. 次の敵を enemy_queue に入れる](#ステップ36-次の敵を-enemy_queue-に入れる)
  - [ステップ37. 敵を倒したら、次の敵に交代する](#ステップ37-敵を倒したら次の敵に交代する)

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
| `Path(__file__).resolve().parent.parent` | サンプル自身（`example/exNN.py`）から見て1つ上の `16_battle_game/` フォルダ |
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
step2. プロジェクトの fonts フォルダに置く（このレッスンでは 16_battle_game/fonts/）
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


# キャラクターを画像で表示する

ここまでは `pg.draw.rect()` で四角形を描く想定で話を進めてきたが、このレッスンでは勇者・魔法使い・戦士・スライム・ドラゴンをイラスト画像で表示する。

| ファイル | 内容 |
| --- | --- |
| `images/yuusya_game.png` | 勇者 |
| `images/mahoutsukai_white_man.png` | 魔法使い |
| `images/game_yuusya_woman.png` | 戦士（流用） |
| `images/fantasy_game_character_slime.png` | スライム |
| `images/fantasy_dragon_red.png` | ドラゴン |

いずれもフリー素材サイトから取得した画像を使っている。

> フリー素材を使うときは、配布サイトの利用規約（商用利用・再配布の可否、公開リポジトリに置いてよいかなど）を必ず確認すること。キャラクターのデザインが特定の作品を強く連想させる場合は、著作権・商標の観点から使って問題ないか事前に検討する。

```python
IMG_DIR  = Path(__file__).resolve().parent.parent / "images"
hero_img = pg.image.load(IMG_DIR / "yuusya_game.png").convert_alpha()
```

画像のサイズは正方形とは限らないため、縦横比を保ったまま `rect`（表示したいサイズ）に収まる大きさまで `pg.transform.smoothscale()` で縮小する。縦横比を無視して `rect.w` × `rect.h` にそのまま合わせると、画像が縦横につぶれて歪んでしまう。

```python
iw, ih = image.get_size()
scale  = min(rect.w / iw, rect.h / ih)
self.image = pg.transform.smoothscale(image, (int(iw * scale), int(ih * scale)))
```

縮小した画像は `rect` より小さくなることがあるため、描画するときは `rect` の中心に合わせる。

```python
img_rect = self.image.get_rect(center=self.rect.center)
```

倒れたときは、これまでの `GRAY` の四角形の代わりに `pg.transform.grayscale()` で色を落として表示する。

```python
if self.is_alive():
    screen.blit(self.image, img_rect)
else:
    screen.blit(pg.transform.grayscale(self.image), img_rect)
```

---

# ex01 — CLI版をpygame化する

[15_class](../15_class/README.md) の Q3 で作った `Character`・`Enemy` を、そのまま pygame の画面に表示する。ダメージ計算や HP 判定は Q3 と同じで、`print()` の代わりにメッセージを `return` して画面に描く。SPACE キーを押すたびに1ターン進む（完成形は [example/ex01.py](example/ex01.py)）。

## ステップ1. ライブラリを読み込んで初期化する

新しい `.py` ファイルの1行目から、次の順に書く。

- `from pathlib import Path` で、フォントや画像のパスを組み立てる `Path` を読み込む
- `import pygame as pg`、`import sys` で、ライブラリを読み込む
- 1行空けて、`pg.init()` で、pygame を初期化する

<details>
<summary>コードを見る</summary>

```python
from pathlib import Path
import pygame as pg
import sys

pg.init()
```

</details>

## ステップ2. ウィンドウを作る

`pg.init()` の下に書く。

- `WIDTH, HEIGHT = 600, 400` で、ウィンドウの幅と高さを決める
- `FPS = 60` で、1秒間に更新する回数を決める
- `screen = pg.display.set_mode((WIDTH, HEIGHT))` で、ウィンドウを作る
- `pg.display.set_caption("ex01: CLI版をpygame化する")` で、タイトルバーの文字を設定する
- `clock = pg.time.Clock()` で、FPSを管理する `clock` を作る

<details>
<summary>コードを見る</summary>

```python
WIDTH, HEIGHT = 600, 400
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("ex01: CLI版をpygame化する")
clock  = pg.time.Clock()
```

</details>

## ステップ3. 日本語フォントを読み込む

日本語の名前を表示するので、同梱のフォントを読み込む（理由は上の「[フォントについて](#フォントについて)」を参照）。`clock` の下に書く。

- `FONT = Path(__file__).resolve().parent.parent / "fonts" / "NotoSansCJKjp-Regular.otf"` で、フォントファイルのパスを求める
- `font = pg.font.Font(FONT, 24)` で、名前用の大きめのフォントを作る
- `font_s = pg.font.Font(FONT, 20)` で、HP・メッセージ用の小さめのフォントを作る
- `WHITE = pg.Color("WHITE")` で、文字の色を変数にしておく

<details>
<summary>コードを見る</summary>

```python
FONT   = Path(__file__).resolve().parent.parent / "fonts" / "NotoSansCJKjp-Regular.otf"
font   = pg.font.Font(FONT, 24)
font_s = pg.font.Font(FONT, 20)
WHITE  = pg.Color("WHITE")
```

</details>

## ステップ4. 画像を読み込む

フォントの設定の下に、1行空けて書く（画像については上の「[キャラクターを画像で表示する](#キャラクターを画像で表示する)」を参照）。

- `IMG_DIR = Path(__file__).resolve().parent.parent / "images"` で、画像フォルダのパスを求める
- `hero_img` に `yuusya_game.png` を、`slime_img` に `fantasy_game_character_slime.png` を、`pg.image.load(...).convert_alpha()` で読み込む

<details>
<summary>コードを見る</summary>

```python
IMG_DIR   = Path(__file__).resolve().parent.parent / "images"
hero_img  = pg.image.load(IMG_DIR / "yuusya_game.png").convert_alpha()
slime_img = pg.image.load(IMG_DIR / "fantasy_game_character_slime.png").convert_alpha()
```

</details>

## ステップ5. Character クラスを作る

2行空けて、キャラクターの共通クラスを書く。[15_class](../15_class/README.md) の Q3 の `Character` に、画面に描くための `rect` と `image` を足す。

- `class Character():` を定義する
- `def __init__(self, name, attack_power, rect, image):` で、名前・攻撃力・表示する範囲 `rect`・画像を受け取る
- `self.name`、`self.attack_power`、`self.rect` に、受け取った値を入れる。`self.hp = 100` で、HP の初期値を決める
- 画像の縦横比を保ったまま `rect` に収まる大きさに縮小して、`self.image` に入れる（理由は「[キャラクターを画像で表示する](#キャラクターを画像で表示する)」を参照）
  - `iw, ih = image.get_size()` で、元の画像の幅と高さを求める
  - `scale = min(rect.w / iw, rect.h / ih)` で、幅と高さのどちらにも収まる倍率を求める
  - `self.image = pg.transform.smoothscale(image, (int(iw * scale), int(ih * scale)))` で縮小する

<details>
<summary>コードを見る</summary>

```python
class Character():
    def __init__(self, name, attack_power, rect, image):
        self.name         = name
        self.hp           = 100
        self.attack_power = attack_power
        self.rect         = rect
        # 画像の縦横比を保ったまま rect に収まるサイズへ縮小する（画像が正方形とは限らないため）
        iw, ih = image.get_size()
        scale  = min(rect.w / iw, rect.h / ih)
        self.image = pg.transform.smoothscale(image, (int(iw * scale), int(ih * scale)))
```

</details>

## ステップ6. attack() と is_alive() を書く

`__init__` の下に、1行空けて2つのメソッドを書く（Q3 と同じ計算）。

- `def attack(self, target):` で、`target.hp -= self.attack_power` と、相手の HP を減らす
  - `print()` の代わりに、`return f"{self.name}の攻撃! {target.name}に{self.attack_power}ダメージ!"` で、メッセージを返す（画面に描くため）
- `def is_alive(self):` で、`return self.hp > 0` と、生きているかを返す

<details>
<summary>コードを見る</summary>

```python
    def attack(self, target):
        target.hp -= self.attack_power
        return f"{self.name}の攻撃! {target.name}に{self.attack_power}ダメージ!"

    def is_alive(self):
        return self.hp > 0
```

</details>

## ステップ7. Enemy クラスを作る

`Character` の下に、2行空けて書く。

- `class Enemy(Character):` で、`Character` を継承する
- `__init__(self, name, attack_power, rect, image)` で、`super().__init__(name, attack_power, rect, image)` を呼び、そのあと `self.hp = 150` と、HP を上書きする
- `attack(self, target)` を上書きする。`dmg = int(self.attack_power * 1.5)` で、攻撃力を1.5倍にして整数にする。`target.hp -= dmg` で HP を減らし、`return` でメッセージを返す

<details>
<summary>コードを見る</summary>

```python
class Enemy(Character):
    def __init__(self, name, attack_power, rect, image):
        super().__init__(name, attack_power, rect, image)
        self.hp = 150

    def attack(self, target):
        dmg = int(self.attack_power * 1.5)
        target.hp -= dmg
        return f"{self.name}の攻撃! {target.name}に{dmg}ダメージ!"
```

</details>

## ステップ8. キャラクターを作る

`Enemy` の下に、2行空けて書く。

- `PLAYER_SIZE = 60`、`ENEMY_SIZE = 70` で、表示する大きさを決める
- `player_rect = pg.Rect(270, 230, PLAYER_SIZE, PLAYER_SIZE)` で、勇者の位置と大きさを決める
- `enemy_rect = pg.Rect(0, 40, ENEMY_SIZE, ENEMY_SIZE)` で、敵の `Rect` を作り、次の行で `enemy_rect.centerx = WIDTH // 2` と、画面の横の中央に合わせる
- 1行空けて、`player = Character("勇者", attack_power=30, rect=player_rect, image=hero_img)` で、勇者を作る
- `enemy = Enemy("スライム", attack_power=15, rect=enemy_rect, image=slime_img)` で、敵を作る（以降のステップでも「スライム」なので、ここで名前を合わせておく）

<details>
<summary>コードを見る</summary>

```python
PLAYER_SIZE = 60
ENEMY_SIZE  = 70
player_rect = pg.Rect(270, 230, PLAYER_SIZE, PLAYER_SIZE)
enemy_rect  = pg.Rect(0, 40, ENEMY_SIZE, ENEMY_SIZE)
enemy_rect.centerx = WIDTH // 2

player = Character("勇者", attack_power=30, rect=player_rect, image=hero_img)
enemy  = Enemy("スライム", attack_power=15, rect=enemy_rect, image=slime_img)
```

</details>

## ステップ9. メッセージとゲーム終了の変数を作る

キャラクターの下に、1行空けて書く。

- `message = "SPACE: 攻撃"` で、表示するメッセージの最初の文を決める
- `sub_message = ""` で、2行目のメッセージを空にしておく。1ターンで勇者と敵の2回攻撃するので、2つのメッセージを2行に分けて表示する（片方だけだと、もう片方の攻撃が表示されないまま消えてしまう）
- `game_over = False` で、決着がついたかを覚える

<details>
<summary>コードを見る</summary>

```python
message     = "SPACE: 攻撃"
sub_message = ""   # 1ターンで player と enemy 両方が攻撃するので、2行に分けて表示する
game_over   = False
```

</details>

## ステップ10. メインループを作る

1行空けて、関数の外（字下げなし）に書く。

- `while True:` で、くり返しを作る
- `for event in pg.event.get():` で、イベントを1つずつ調べる
- `event.type == pg.QUIT`（閉じるボタン）なら、`pg.quit()` と `sys.exit()` で終了する

<details>
<summary>コードを見る</summary>

```python
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
```

</details>

## ステップ11. SPACEキーで1ターン進める

`for event` の中の、`QUIT` の処理の下に書く（`for` の中なので、字下げは1段深い）。SPACEキーを押すたびに、勇者→敵の順に攻撃する。

- `if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and not game_over:` で、SPACEキーが押されて、まだ決着がついていないときだけ処理する
- `sub_message = player.attack(enemy)` で、勇者が攻撃して、返ってきたメッセージを `sub_message` に入れる
- `if not enemy.is_alive():`（敵が倒れた）なら、`message` に勝利の文、`sub_message = ""`、`game_over = True`
- `else:`（敵が生きている）なら、`message = enemy.attack(player)` で、敵が反撃する
  - その中で `if not player.is_alive():`（勇者が倒れた）なら、`message` に敗北の文、`sub_message = ""`、`game_over = True`

<details>
<summary>コードを見る</summary>

```python
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
```

</details>

## ステップ12. 背景を塗りつぶす

`for event` のループが終わったあと（`for` と同じ字下げ）に、1行空けて書く。

- `screen.fill(pg.Color("DARKSLATEGRAY"))` で、背景を暗い灰色で塗りつぶす

<details>
<summary>コードを見る</summary>

```python
    screen.fill(pg.Color("DARKSLATEGRAY"))
```

</details>

## ステップ13. 勇者を描く

背景の下に、1行空けて書く。

- `if player.is_alive():` なら、`screen.blit(player.image, player.image.get_rect(center=player.rect.center))` で、画像を `rect` の中心に合わせて描く（縮小した画像は `rect` より小さいことがあるため）
- `else:`（倒れた）なら、`pg.transform.grayscale(player.image)` で色を落とした画像を、同じ位置に描く
- `player_s = font.render(f"{player.name}  HP:{player.hp}", True, WHITE)` で、名前とHPの文字の画像を作る
- `screen.blit(player_s, player_s.get_rect(centerx=player.rect.centerx, bottom=player.rect.top - 6))` で、`rect` の少し上に、中心をそろえて描く（`get_rect()` の使い方は「[テキストの位置合わせ（get_rect）](#テキストの位置合わせget_rect)」を参照）

<details>
<summary>コードを見る</summary>

```python
    if player.is_alive():
        screen.blit(player.image, player.image.get_rect(center=player.rect.center))
    else:
        screen.blit(pg.transform.grayscale(player.image), player.image.get_rect(center=player.rect.center))
    player_s = font.render(f"{player.name}  HP:{player.hp}", True, WHITE)
    screen.blit(player_s, player_s.get_rect(centerx=player.rect.centerx, bottom=player.rect.top - 6))
```

</details>

## ステップ14. 敵を描く

勇者を描く処理の下に、1行空けて書く。勇者と同じ形で、`player` を `enemy` に変える。

- `if enemy.is_alive():` なら通常の画像、`else:` ならグレーの画像を描く
- `enemy_s = font.render(f"{enemy.name}  HP:{enemy.hp}", True, WHITE)` で文字の画像を作り、`enemy.rect` の少し上に描く

<details>
<summary>コードを見る</summary>

```python
    if enemy.is_alive():
        screen.blit(enemy.image, enemy.image.get_rect(center=enemy.rect.center))
    else:
        screen.blit(pg.transform.grayscale(enemy.image), enemy.image.get_rect(center=enemy.rect.center))
    enemy_s = font.render(f"{enemy.name}  HP:{enemy.hp}", True, WHITE)
    screen.blit(enemy_s, enemy_s.get_rect(centerx=enemy.rect.centerx, bottom=enemy.rect.top - 6))
```

</details>

## ステップ15. メッセージを描く

敵を描く処理の下に、1行空けて書く。

- `msg = font_s.render(message, True, WHITE)` で、メッセージの文字の画像を作る
- `msg_rect = msg.get_rect(centerx=WIDTH // 2, top=345)` で、横の中央、上端が `345` の位置の `Rect` を求める
- `screen.blit(msg, msg_rect)` で描く
- `sub_s = font_s.render(sub_message, True, WHITE)` で、2行目の文字の画像を作り、`screen.blit(sub_s, sub_s.get_rect(centerx=WIDTH // 2, bottom=msg_rect.top - 2))` で、1行目のすぐ上に描く

<details>
<summary>コードを見る</summary>

```python
    msg = font_s.render(message, True, WHITE)
    msg_rect = msg.get_rect(centerx=WIDTH // 2, top=345)
    screen.blit(msg, msg_rect)
    sub_s = font_s.render(sub_message, True, WHITE)
    screen.blit(sub_s, sub_s.get_rect(centerx=WIDTH // 2, bottom=msg_rect.top - 2))
```

</details>

## ステップ16. 画面を更新する

メッセージを描く処理の下に、1行空けて書く（`while` の中）。

- `pg.display.update()` で、画面を更新する
- `clock.tick(FPS)` で、FPSを一定にする

<details>
<summary>コードを見る</summary>

```python
    pg.display.update()
    clock.tick(FPS)
```

</details>

ここまでで、`example/ex01.py` と同じ動きになる。SPACEキーを押すたびに、勇者と敵が交互に攻撃し、どちらかが倒れると終わる。

### 実行する

ターミナルで、リポジトリのルートから実行する（自分のファイルなら、ファイル名を置き換える）。

```bash
python 16_battle_game/example/ex01.py
```

---

# ex02 — パーティー化して完成させる

勇者1人 vs スライム1体を、3人のパーティー vs 敵1体に拡張する。ダメージにランダムな幅を持たせ、反撃・全滅チェック・メッセージ履歴も加えて、バトルゲームとして完成させる（完成形は [example/ex02.py](example/ex02.py)）。

## ステップ17. random を読み込み、タイトルを変える

ここから、ex01 のコードを書き換えて、パーティー戦にしていく。同じファイルを書き換えてもよいし、`ex01.py` をコピーして `ex02.py` として書き換えてもよい。

- `import sys` の下に、`import random` を足す（ダメージのランダムな幅と、攻撃する人の選択に使う）
- `pg.display.set_caption(...)` の文字を、`"ex02: バトルゲーム（完成）"` に変える

読み込み:

<details>
<summary>コードを見る</summary>

```python
import random
```

</details>

タイトル:

<details>
<summary>コードを見る</summary>

```python
pg.display.set_caption("ex02: バトルゲーム（完成）")
```

</details>

## ステップ18. 仲間の画像を足す

画像の読み込みの下に、2行足す。

- `mage_img` に `mahoutsukai_white_man.png`（魔法使い）を読み込む
- `warrior_img` に `game_yuusya_woman.png`（戦士）を読み込む
- 読み込み方は、`hero_img` と同じ（`.convert_alpha()` を付ける）

<details>
<summary>コードを見る</summary>

```python
IMG_DIR     = Path(__file__).resolve().parent.parent / "images"
hero_img    = pg.image.load(IMG_DIR / "yuusya_game.png").convert_alpha()
mage_img    = pg.image.load(IMG_DIR / "mahoutsukai_white_man.png").convert_alpha()
warrior_img = pg.image.load(IMG_DIR / "game_yuusya_woman.png").convert_alpha()
slime_img   = pg.image.load(IMG_DIR / "fantasy_game_character_slime.png").convert_alpha()
```

</details>

## ステップ19. Character の __init__ を書き換える

パーティーの全員と敵を同じ形で扱うため、`Character` を書き換える。攻撃力は、`Player` と `Enemy` に分けて持たせる。

- 引数を `(self, name, hp, rect, image)` に変える（`attack_power` をやめて、`hp` を受け取る）
- `self.hp = 100` を `self.hp = hp` に変える
- `self.max_hp = hp` を足す（「HP: 70 / 100」のように、最大HPも表示するため）
- `self.attack_power = attack_power` の行は消す
- 画像を縮小する部分は、そのまま

<details>
<summary>コードを見る</summary>

```python
class Character():
    def __init__(self, name, hp, rect, image):
        self.name   = name
        self.hp     = hp
        self.max_hp = hp
        self.rect   = rect
        # 画像の縦横比を保ったまま rect に収まるサイズへ縮小する（画像が正方形とは限らないため）
        iw, ih = image.get_size()
        scale  = min(rect.w / iw, rect.h / ih)
        self.image = pg.transform.smoothscale(image, (int(iw * scale), int(ih * scale)))
```

</details>

## ステップ20. attack() を消して、take_damage() を足す

- `Character` の `attack()` を、消す（攻撃は `Player` と `Enemy` のそれぞれで書く）
- `is_alive()` の下に、1行空けて `take_damage(self, amount)` を足す
  - `self.hp -= amount` で、HP を減らす
  - `if self.hp < 0:` なら、`self.hp = 0` にする（HP がマイナスにならないようにする）

<details>
<summary>コードを見る</summary>

```python
    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
```

</details>

## ステップ21. draw() を足す

`take_damage()` の下に、1行空けて足す。画面への描画を `Character` にまとめるので、`Player` も `Enemy` も、継承して使える。ex01 の「勇者を描く」と同じ内容を、`player` の代わりに `self` で書く。

- `img_rect = self.image.get_rect(center=self.rect.center)` で、画像の描く位置を求める
- `self.is_alive()` なら `self.image` を、倒れていたら `pg.transform.grayscale(self.image)` を、`screen.blit(..., img_rect)` で描く
- `name_s = font.render(self.name, True, WHITE)` で名前の文字を作り、`rect` の少し上（`bottom=self.rect.top - 6`）に描く
- `hp_s = font_s.render(f"HP: {self.hp} / {self.max_hp}", True, WHITE)` でHPの文字を作り、`rect` の少し下（`top=self.rect.bottom + 6`）に描く

<details>
<summary>コードを見る</summary>

```python
    def draw(self):
        img_rect = self.image.get_rect(center=self.rect.center)
        if self.is_alive():
            screen.blit(self.image, img_rect)
        else:
            screen.blit(pg.transform.grayscale(self.image), img_rect)
        name_s = font.render(self.name, True, WHITE)
        screen.blit(name_s, name_s.get_rect(centerx=self.rect.centerx, bottom=self.rect.top - 6))
        hp_s = font_s.render(f"HP: {self.hp} / {self.max_hp}", True, WHITE)
        screen.blit(hp_s, hp_s.get_rect(centerx=self.rect.centerx, top=self.rect.bottom + 6))
```

</details>

## ステップ22. Player クラスを作る

`Character` の下に、2行空けて書く。ex01 の `PLAYER_SIZE = 60`（キャラクターを作るところにあった）は消して、ここに書く。

- `PLAYER_SIZE = 60` を書く
- 2行空けて、`class Player(Character):` で、`Character` を継承する
- `__init__(self, name, cx, image, hp, attack_power)` で、中心のX座標 `cx` を受け取る
- `rect = pg.Rect(cx - PLAYER_SIZE // 2, 200, PLAYER_SIZE, PLAYER_SIZE)` で、`cx` が中心になるように位置を決める（横幅の半分を引く）
- `super().__init__(name, hp, rect, image)` で、`Character` の初期化を呼ぶ
- `self.attack_power = attack_power` で、攻撃力は `Player` 独自の属性にする（`attack` という名前にすると、次に作る `attack()` メソッドと名前がかぶるので、`attack_power` にする）
- `is_alive()` / `take_damage()` / `draw()` は `Character` から継承するので、書かない

<details>
<summary>コードを見る</summary>

```python
PLAYER_SIZE = 60


class Player(Character):
    def __init__(self, name, cx, image, hp, attack_power):
        rect = pg.Rect(cx - PLAYER_SIZE // 2, 200, PLAYER_SIZE, PLAYER_SIZE)
        super().__init__(name, hp, rect, image)   # ← Character の __init__ を呼ぶ
        self.attack_power = attack_power
```

</details>

## ステップ23. Player の attack() を書く

`__init__` の下に、1行空けて書く。

- `def attack(self, target):` を定義する
- `dmg = random.randint(self.attack_power - 5, self.attack_power + 5)` で、攻撃力の±5の範囲でダメージを決める
- `target.take_damage(dmg)` で、相手の HP を減らす（`Character` から継承したメソッド）
- `return f"{self.name}の攻撃! {dmg}ダメージ!"` で、メッセージを返す

<details>
<summary>コードを見る</summary>

```python
    def attack(self, target):
        dmg = random.randint(self.attack_power - 5, self.attack_power + 5)
        target.take_damage(dmg)   # ← Character から継承したメソッドを使う
        return f"{self.name}の攻撃! {dmg}ダメージ!"
```

</details>

## ステップ24. Enemy クラスを書き換える

ex01 の `Enemy` クラスと、`ENEMY_SIZE = 70` の行は消して、`Player` の下に書き直す。

- 2行空けて、`ENEMY_SIZE = 70` を書く
- 2行空けて、`class Enemy(Character):` を書く
- `__init__(self, name, hp, attack_power)` に変える（`rect` と `image` は、`Enemy` の中で決める）
- `rect = pg.Rect(0, 40, ENEMY_SIZE, ENEMY_SIZE)` を作り、次の行で `rect.centerx = WIDTH // 2` と、画面の横の中央に合わせる
- `super().__init__(name, hp, rect, slime_img)` で、`Character` の初期化を呼ぶ
- `self.attack_power = attack_power` で、攻撃力を持たせる

<details>
<summary>コードを見る</summary>

```python
ENEMY_SIZE = 70


# ── ex01 との違い: attack_power / attack() を追加して反撃できるようにした ──
class Enemy(Character):
    def __init__(self, name, hp, attack_power):
        rect = pg.Rect(0, 40, ENEMY_SIZE, ENEMY_SIZE)
        rect.centerx = WIDTH // 2
        super().__init__(name, hp, rect, slime_img)   # ← Character の __init__ を呼ぶ
        self.attack_power = attack_power
```

</details>

## ステップ25. Enemy の attack() を書く

`__init__` の下に、1行空けて書く。`Player` と同じ形で、ダメージの幅を±3と小さくする。

- `dmg = random.randint(self.attack_power - 3, self.attack_power + 3)` で、ダメージを決める
- `target.take_damage(dmg)` で、HP を減らす
- `return f"{self.name}の反撃! {target.name}に{dmg}ダメージ!"` で、メッセージを返す

<details>
<summary>コードを見る</summary>

```python
    def attack(self, target):
        dmg = random.randint(self.attack_power - 3, self.attack_power + 3)
        target.take_damage(dmg)
        return f"{self.name}の反撃! {target.name}に{dmg}ダメージ!"
```

</details>

## ステップ26. 敵とパーティーを作る

ex01 の「キャラクターを作る」の `player_rect` 〜 `enemy = Enemy(...)` の行は、すべて消して、次を書く。

- `enemy = Enemy("スライム", 80, 12)` で、名前・HP・攻撃力を渡して、敵を作る
- `party = [ ... ]` で、3人のリストを作る。`Player(名前, 中心のX座標, 画像, hp=…, attack_power=…)` の形で、1人1行で書く
  - 勇者 `(100, hero_img, hp=100, attack_power=25)`
  - 魔法使い `(300, mage_img, hp=70, attack_power=35)`
  - 戦士 `(500, warrior_img, hp=130, attack_power=20)`

<details>
<summary>コードを見る</summary>

```python
enemy = Enemy("スライム", 80, 12)
party = [
    Player("勇者",    100, hero_img,    hp=100, attack_power=25),
    Player("魔法使い", 300, mage_img,    hp=70,  attack_power=35),
    Player("戦士",    500, warrior_img, hp=130, attack_power=20),
]
```

</details>

## ステップ27. メッセージをリストにする

ex01 の `message`、`sub_message`、`game_over` の3行を消して、次の2行に書き換える。1ターンで複数の出来事が起こるので、メッセージはリストで持つ。

- `messages = ["スライムが現れた！", "SPACE: 攻撃"]` で、最初のメッセージを入れる
- `game_over = False` を書く

<details>
<summary>コードを見る</summary>

```python
messages  = ["スライムが現れた！", "SPACE: 攻撃"]
game_over = False
```

</details>

## ステップ28. 生き残っている仲間から、攻撃する人を選ぶ

`for event` の中の SPACE の処理（`if event.type == pg.KEYDOWN ...` の中身）を、ex01 の `sub_message = player.attack(enemy)` 以降をすべて消して、書き直す。`if` の行はそのまま。

- `messages = []` で、メッセージを空にする（毎ターン、新しく作り直す）
- `alive = []` を作り、`for p in party:` で `if p.is_alive():` のとき `alive.append(p)` と、生きている仲間を集める
- `attacker = random.choice(alive)` で、ランダムに1人選ぶ
- `messages.append(attacker.attack(enemy))` で、その人が攻撃して、メッセージをリストに足す

<details>
<summary>コードを見る</summary>

```python
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and not game_over:
            messages = []

            # 生存しているプレイヤーをリストに集める
            alive = []
            for p in party:
                if p.is_alive():
                    alive.append(p)

            # パーティーの攻撃
            attacker = random.choice(alive)
            messages.append(attacker.attack(enemy))
```

</details>

## ステップ29. 敵を倒したときの処理

攻撃の下に、1行空けて書く（`if` の中と同じ字下げ）。

- `if not enemy.is_alive():` なら、`messages.append("スライムをたおした!")` と `game_over = True`

<details>
<summary>コードを見る</summary>

```python
            if not enemy.is_alive():
                messages.append("スライムをたおした!")
                game_over = True
```

</details>

## ステップ30. 敵が反撃する

倒れていないとき（`else:`）の中に書く。

- `else:` を書く
- `target = random.choice(alive)` で、攻撃される人をランダムに選ぶ
- `messages.append(enemy.attack(target))` で、敵が攻撃して、メッセージをリストに足す

<details>
<summary>コードを見る</summary>

```python
            else:
                # 敵の反撃
                target = random.choice(alive)
                messages.append(enemy.attack(target))
```

</details>

## ステップ31. 全滅したか調べる

敵が反撃したあと、同じ `else:` の中に書く。敵の反撃で全員倒れていることがあるので、調べないとゲームが続いてしまう。

- `if not any(p.is_alive() for p in party):`（生きている仲間が1人もいない）なら、`messages.append("パーティーは全滅した…")` と `game_over = True`
- `else:` なら、`messages.append("SPACE: 攻撃")`

<details>
<summary>コードを見る</summary>

```python
                # 全滅チェック（enemy の反撃で全員倒れたら、次の alive が空になってしまうため）
                if not any(p.is_alive() for p in party):
                    messages.append("パーティーは全滅した…")
                    game_over = True
                else:
                    messages.append("SPACE: 攻撃")
```

</details>

## ステップ32. キャラクターを描く

背景を塗りつぶす処理（`screen.fill(...)`）の下の、ex01 の勇者・敵の描画（`if player.is_alive(): ...` から `enemy_s` を描く行まで）は、すべて消して、書き直す。

- `enemy.draw()` で、敵を描く
- `for p in party:` で、`p.draw()` と、仲間を全員描く

<details>
<summary>コードを見る</summary>

```python
    screen.fill(pg.Color("DARKSLATEGRAY"))

    enemy.draw()
    for p in party:
        p.draw()
```

</details>

## ステップ33. メッセージを描く

ex01 のメッセージの描画（`msg` 〜 `sub_s` の行）は消して、書き直す。直近の3件だけ、画面の下に並べて描く。

- `show_msgs = messages[-3:]` で、リストの最後の3件を取り出す
- `line_h = font_s.get_linesize()` で、1行の高さを求める
- `start_y = HEIGHT - line_h * len(show_msgs) - 4` で、いちばん上の行のY座標を求める（件数が少なくても、画面の下にそろう）
- `for i, msg in enumerate(show_msgs):` で、番号 `i` とメッセージを取り出し、`s = font_s.render(msg, True, pg.Color("WHITE"))` で文字の画像を作り、`screen.blit(s, s.get_rect(centerx=WIDTH // 2, top=start_y + i * line_h))` で、`i` 行目に描く

<details>
<summary>コードを見る</summary>

```python
    show_msgs = messages[-3:]
    line_h  = font_s.get_linesize()
    start_y = HEIGHT - line_h * len(show_msgs) - 4
    for i, msg in enumerate(show_msgs):
        s = font_s.render(msg, True, pg.Color("WHITE"))
        screen.blit(s, s.get_rect(centerx=WIDTH // 2, top=start_y + i * line_h))
```

</details>

ここまでで、`example/ex02.py` と同じ動きになる。3人のパーティーがランダムに攻撃し、敵が反撃して、全滅するか敵を倒すと終わる。

### 実行する

ターミナルで、リポジトリのルートから実行する（自分のファイルなら、ファイル名を置き換える）。

```bash
python 16_battle_game/example/ex02.py
```

---

# ex03 — 複数の敵と連戦する

スライムを倒したらドラゴンが現れる連戦を追加する。`enemy_queue` で戦う順序を管理し、`Enemy` に画像と大きさを足して見た目を変える（完成形は [example/ex03.py](example/ex03.py)）。

## ステップ34. ドラゴンの画像を読み込む

ここから、ex02 のコードに書き足して、連戦にする。

- `pg.display.set_caption(...)` の文字を、`"ex03: 連戦"` に変える
- `slime_img` の読み込みの下に、`dragon_img` に `fantasy_dragon_red.png` を、同じ形で読み込む

タイトル:

<details>
<summary>コードを見る</summary>

```python
pg.display.set_caption("ex03: 連戦")
```

</details>

画像:

<details>
<summary>コードを見る</summary>

```python
dragon_img  = pg.image.load(IMG_DIR / "fantasy_dragon_red.png").convert_alpha()
```

</details>

## ステップ35. Enemy に image と size を足す

敵ごとに、画像と大きさを変えられるようにする。`Enemy` の `__init__` を書き換える。

- 引数を `(self, name, hp, attack_power, image=slime_img, size=70)` に変える（指定しなければ、スライムの画像と大きさ70になる）
- `rect = pg.Rect(0, 40, size, size)` に変える（`ENEMY_SIZE` の代わりに `size`）
- `super().__init__(name, hp, rect, image)` に変える（`slime_img` の代わりに `image`）
- `ENEMY_SIZE = 70` の行は、もう使わないので消す
- `attack()` は、`self.name` でメッセージを作っているので、変えなくてよい（ドラゴンに替わると、自動で「ドラゴンの反撃!」になる）

<details>
<summary>コードを見る</summary>

```python
class Enemy(Character):
    def __init__(self, name, hp, attack_power, image=slime_img, size=70):
        rect = pg.Rect(0, 40, size, size)
        rect.centerx = WIDTH // 2
        super().__init__(name, hp, rect, image)   # ← Character の __init__ を呼ぶ
        self.attack_power = attack_power
```

</details>

## ステップ36. 次の敵を enemy_queue に入れる

`enemy = Enemy("スライム", 80, 12)` の上に書く。

- `enemy_queue = [ ... ]` で、あとから出てくる敵のリストを作る
- 中に、`Enemy("ドラゴン", 200, 20, image=dragon_img, size=90)` を1つ入れる（ドラゴンは少し大きく描く）

<details>
<summary>コードを見る</summary>

```python
enemy_queue = [
    Enemy("ドラゴン", 200, 20, image=dragon_img, size=90),
]
enemy = Enemy("スライム", 80, 12)
```

</details>

## ステップ37. 敵を倒したら、次の敵に交代する

「敵を倒したときの処理」を書き換える。`if not enemy.is_alive():` の中の、`messages.append("スライムをたおした!")` と `game_over = True` を、次のように変える。

- `messages.append(f"{enemy.name}をたおした!")` に変える（倒した敵の名前を使う）
- `if enemy_queue:`（次の敵がいる）なら、次の3つを行う
  - `enemy = enemy_queue.pop(0)` で、リストの先頭を取り出して、`enemy` に入れ替える
  - `messages.append(f"{enemy.name}が現れた！")` で、新しい敵の名前を表示する
  - `messages.append("SPACE: 攻撃")` を足す
- `else:`（次の敵がいない）なら、`messages.append("全ての敵をたおした!")` と `game_over = True`

<details>
<summary>コードを見る</summary>

```python
            if not enemy.is_alive():
                messages.append(f"{enemy.name}をたおした!")
                # ── ex02 との違い: 次の敵がいれば交代する ──
                if enemy_queue:
                    enemy = enemy_queue.pop(0)
                    messages.append(f"{enemy.name}が現れた！")
                    messages.append("SPACE: 攻撃")
                else:
                    messages.append("全ての敵をたおした!")
                    game_over = True
```

</details>

ここまでで、`example/ex03.py` と同じ、完成版の動きになる。スライムを倒すとドラゴンが現れ、ドラゴンも倒すと終わる。

### 実行する

ターミナルで、リポジトリのルートから実行する（自分のファイルなら、ファイル名を置き換える）。

```bash
python 16_battle_game/example/ex03.py
```
