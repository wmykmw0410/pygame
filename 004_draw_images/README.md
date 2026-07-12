```text
画像ファイルを読み込んでゲーム画面に表示する方法を学びましょう
以下のサンプルファイルを見ながら実際に動かしてみよう
```

サンプル: [example/ex01.py](example/ex01.py) / [example/ex02.py](example/ex02.py) / [example/ex03.py](example/ex03.py)

# 画像を描く

### ステップ1.画像を読み込む
```python
"""image.load関数を使う
読み込む画像がどこにあるか(画像ファイルパス)を指定する
このコースでは pygame フォルダ(リポジトリのルート)を作業ディレクトリとして実行するため、
「004_draw_imagesフォルダの中のimagesフォルダの中のcar.pngファイル」であれば、
「pg.image.load("004_draw_images/images/car.png")」と指定し、画像用の変数に代入する"""
画像変数 = pg.image.load("画像ファイルパス")
```

### ステップ2.読み込んだ画像を描画する
```python
"""screenのblit関数を使って描画する
読み込んだ画像データを入れた変数と表示する位置(x,y)を指定する"""
screen.blit(画像変数, (x, y))
```

### 画像はRectとして扱える
```python
"""画像からRectを取得することで、位置管理や衝突判定に使える
get_rect()で画像と同じサイズのRectを取得する"""
myrect = 画像変数.get_rect()

# 位置を指定してRectを取得することもできる
myrect = 画像変数.get_rect(topleft=(100, 100))

# blitの第2引数にRectをそのまま渡せる
screen.blit(画像変数, myrect)
```

### ステップ3.画像のサイズを変更する
```python
"""「画像を読み込む」後に実行する
「画像のサイズを変更する」にはtransform.scale関数を使って、
画像を入れた変数、幅、高さを指定し、変数に入れ直す"""
画像変数 = pg.transform.scale(画像変数, (幅, 高さ))
```

| 項目 | 内容 |
| --- | --- |
| デフォルトサイズ | `image.load()` で読み込んだ画像の元のサイズ(変更なし) |
| 元のサイズを確認 | `画像変数.get_size()` → `(幅, 高さ)` のタプルで返る |
| 幅・高さの範囲 | 1以上の整数(ピクセル単位) |

---
