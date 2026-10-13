```text
pathlibモジュールを使って、画像やサウンドのパスを管理する方法を学びましょう
```

# 目次
- [pathlibモジュール](#pathlibモジュール)
- [pygameでの使用方法](#pygameでの使用方法)
  - [BASE_DIR の作り方](#base_dir-の作り方)

---

# pathlibモジュール

ゲームを作成するときの画像やサウンドを管理するための、便利なパス記述方法

```python
from pathlib import Path
p = Path("test.txt")  # パスを表すオブジェクトが作られる
```

---

# pygameでの使用方法

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent  # このファイルが入っているフォルダ

IMG_DIR = BASE_DIR / "images"               # パスの結合

player_img = pg.image.load(IMG_DIR / "sample.png")
player_rect = player_img.get_rect(topleft=(x, y))
```

`/` 演算子でパスを結合できる

[04_draw_images](../04_draw_images/README.md) のように `"04_draw_images/images/car.png"` と文字列で書くと、実行するフォルダ（作業ディレクトリ）が違うだけで画像が見つからなくなる。`Path(__file__)`（このファイルの場所）を基準にしておけば、どのフォルダから実行しても同じ画像を読み込める。

---

## BASE_DIR の作り方

```python
BASE_DIR = Path(__file__).resolve().parent
```

| ステップ | コード | 内容 |
| --- | --- | --- |
| 1 | `__file__` | 今実行している .py ファイルのパス |
| 2 | `Path(__file__)` | 文字列 → Path オブジェクトに変換 |
| 3 | `.resolve()` | 相対パスを絶対パスに変換 |
| 4 | `.parent` | 1つ上のフォルダ（ファイルが入っているフォルダ） |

```
例: /home/user/game/main.py
                 ↑
              parent → /home/user/game/
```

| 変数 | 内容 | 例 |
| --- | --- | --- |
| `BASE_DIR` | .py ファイルのあるフォルダ | `/home/user/game` |
| `IMG_DIR` | 画像フォルダ | `/home/user/game/images` |
| `IMG_DIR / "car.png"` | 画像ファイルのフルパス | `/home/user/game/images/car.png` |

親の親フォルダに行くには `.parent` を重ねる

```python
BASE_DIR   = Path(__file__).resolve().parent         # /home/user/game
PARENT_DIR = Path(__file__).resolve().parent.parent  # /home/user
```

または `parents[n]` で n 個上のフォルダを指定することもできる

```python
PARENT_DIR  = Path(__file__).resolve().parents[1]  # 1つ上: /home/user
GRANDPARENT = Path(__file__).resolve().parents[2]  # 2つ上: /home
```

サンプル: [pathlib_module.py](pathlib_module.py)

練習: [practice01.py](practice01.py)（「# ★」の部分が空欄になっているので、サンプルを見ながら自分の手でコードを打ち込んで完成させよう）

動いたら、書き換えてもう一度動かし、変化を確認する。

| 試すこと | 確認すること |
| --- | --- |
| `print(CURRENT_DIR)` | 絶対パス（`/` から始まる、ファイルの場所）が表示される |
| `.parent` → `.parent.parent`（`BASE_DIR` を表示） | 1つ上のフォルダ（`pygame` フォルダ）になる。`images` フォルダが無いので、画像の読み込みでエラーになる |
| `.parents[0]` / `.parents[1]` / `.parents[2]` を表示 | `[0]` は `.parent` と同じ（ファイルのあるフォルダ）、`[1]` は1つ上、`[2]` は2つ上のフォルダ |
| `IMG_DIR / "car.png"` → `IMG_DIR / "nothing.png"` | `FileNotFoundError`（`No such file or directory: '.../images/nothing.png'`）。存在しないファイルは読み込めない |
| `08_pathlib_module` フォルダへ `cd` してから、`python practice01.py` | 画像は表示される。`BASE_DIR` は実行した場所ではなく、ファイルの場所が基準だから |
