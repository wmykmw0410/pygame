# pygameの色指定方法

pygameで色を指定する方法は主に5つある。

## 1. 色名(文字列)で指定

```python
pg.Color("RED")
pg.Color("WHITE")
pg.Color("BLACK")
pg.Color("BLUE")
pg.Color("GREEN")
```

- 大文字・小文字は区別しない (`"red"` でも `"RED"` でも可)
- 使えるカラー名は [CSS3の色名](https://www.w3.org/TR/css-color-3/#svg-color) に準拠

## 2. RGB値で指定

```python
pg.Color(R, G, B)
# 例
pg.Color(255, 0, 0)    # 赤
pg.Color(0, 255, 0)    # 緑
pg.Color(0, 0, 255)    # 青
pg.Color(255, 255, 255) # 白
pg.Color(0, 0, 0)      # 黒
```

| 引数 | 意味       | 範囲    | デフォルト |
| -- | -------- | ----- | ----- |
| R  | 赤(Red)   | 0〜255 | なし(必須) |
| G  | 緑(Green) | 0〜255 | なし(必須) |
| B  | 青(Blue)  | 0〜255 | なし(必須) |

## 3. RGBA値で指定(透明度あり)

```python
pg.Color(R, G, B, A)
# 例
pg.Color(255, 0, 0, 128)  # 半透明の赤
pg.Color(0, 0, 255, 255)  # 不透明の青
```

| 引数 | 意味              | 範囲    | デフォルト  |
| -- | --------------- | ----- | ------ |
| A  | 透明度(Alpha) | 0〜255 | 255(不透明) |

- `0` で完全透明、`255` で完全不透明

## 4. 16進数（HEX）で指定

```python
pg.Color("#FF0000")   # 赤
pg.Color("#FFFFFF")   # 白
pg.Color("#000000")   # 黒
pg.Color("#FF000080") # 半透明の赤（末尾2桁がAlpha）
```

- `#RRGGBB` の形式で、RR・GG・BB それぞれ 00〜FF（0〜255）を16進数で表す
- 透明度を含める場合は `#RRGGBBAA` の8桁にする
- 大文字・小文字は区別しない（`"#ff0000"` でも可）
- Web デザインツールからそのままコピーして使える

## 5. タプルで直接渡す

`pg.Color()` を使わずタプルで渡すこともできる。

```python
screen.fill((255, 255, 255))          # 白
pg.draw.rect(screen, (255, 0, 0), rect) # 赤
```

## よく使う色の早見表

| 色名 | RGB | HEX |
| --- | --- | --- |
| 黒(BLACK)  | (0, 0, 0)       | #000000 |
| 白(WHITE)  | (255, 255, 255) | #FFFFFF |
| 赤(RED)    | (255, 0, 0)     | #FF0000 |
| 緑(GREEN)  | (0, 255, 0)     | #00FF00 |
| 青(BLUE)   | (0, 0, 255)     | #0000FF |
| 黄(YELLOW) | (255, 255, 0)   | #FFFF00 |
| 水色(CYAN)  | (0, 255, 255)   | #00FFFF |
| 紫(PURPLE) | (128, 0, 128)   | #800080 |
| 灰(GRAY)   | (128, 128, 128) | #808080 |
