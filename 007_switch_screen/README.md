```text
関数とページ変数を使って、ゲーム画面を切り替える方法を学びましょう
```

# 目次
- [ゲーム画面の構成](#ゲーム画面の構成)
  - [作り方](#作り方)
- [ページを表示する](#ページを表示する)
- [ボタンでページを切り替える](#ボタンでページを切り替える)
  - [ボタンジャンプ関数](#ボタンジャンプ関数)
  - [ページを追加する](#ページを追加する)
- [枝分かれの紙芝居](#枝分かれの紙芝居)
  - [枝分かれを追加する](#枝分かれを追加する)

---

# ゲーム画面の構成

例) タイトル、ステージ1、ステージ2、ボスステージ、ゲームクリア、ゲームオーバー

## 作り方

```
1. 1ページを1つの関数にまとめる
2. 変数 page で「今どのページを表示するか」管理する
3. 各ページにボタンを作成し、ボタンを押すと次のページに進む仕掛けを作る
```

```python
def page1():
    # ページ1で行う処理

def page2():
    # ページ2で行う処理

page = 1

while True:
    if page == 1:
        page1()
    elif page == 2:
        page2()
```

---

# ページを表示する

サンプル: [01_display_page/ex01.py](01_display_page/ex01.py)

flower1.png と flower2.png を変数に読み込み、それぞれのページ関数で表示する

```python
img1 = pg.image.load("../images/flower1.png")
img2 = pg.image.load("../images/flower2.png")

def page1():
    screen.blit(img1, (0, 0))  # 画像が800×600なので(0,0)から表示すれば画面いっぱいになる

def page2():
    screen.blit(img2, (0, 0))
```

ループの中で `page` の値を見て、表示するページを切り替える

```python
while True:
    if page == 1:
        page1()
    elif page == 2:
        page2()
```

---

# ボタンでページを切り替える

サンプル: [02_btn_to_jamp/ex02.py](02_btn_to_jamp/ex02.py)

## ボタンジャンプ関数

「押したら1回だけ実行するボタン」を関数にして、各ページから呼び出す

```python
pushFlag = False

def button_to_jump(btn, newpage):
    global page, pushFlag

    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()
    if mdown[0]:
        if btn.collidepoint(mx, my) and not pushFlag:
            page = newpage
            pushFlag = True
    else:
        pushFlag = False
```

呼び出し方: `button_to_jump(ボタンのRect, ページ番号)`

```python
def page1():
    screen.blit(img1, (0, 0))
    btn1 = screen.blit(next_img, (600, 540))  # blit の戻り値がボタンの Rect
    button_to_jump(btn1, 2)                   # btn1 を押したらページ2へ
```

## ページを追加する

```
1. 画像の読み込みを追加する
2. ページ切り替え関数を追加する
3. ループを修正する
```

サンプル: [02_btn_to_jamp/ex03.py](02_btn_to_jamp/ex03.py)

---

# 枝分かれの紙芝居

サンプル: [03_page_branch/ex04.py](03_page_branch/ex04.py)

1つのページに複数のボタンを置いて、押したボタンに応じて異なるページへ進む

```python
def page1():
    screen.blit(img1, (0, 0))
    btn1 = screen.blit(next_img, (90, 220))   # 左ボタン → ページ2へ
    btn2 = screen.blit(next_img, (590, 220))  # 右ボタン → ページ3へ
    button_to_jump(btn1, 2)
    button_to_jump(btn2, 3)
```

## 枝分かれを追加する

```
ページ1 → ページ2, 3 へ分岐 (NEXT)
ページ3 → ページ4, 5 へ分岐 (NEXT)
ページ2, 4, 5 → ページ1 へ戻る (リトライ)
```

サンプル: [03_page_branch/ex05.py](03_page_branch/ex05.py)
