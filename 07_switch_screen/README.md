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

flower1.png と flower2.png を変数に読み込み、それぞれのページ関数で表示する

```python
img1 = pg.image.load("07_switch_screen/images/flower1.png")
img2 = pg.image.load("07_switch_screen/images/flower2.png")

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

サンプル: [01_display_page/ex01.py](01_display_page/ex01.py)（画像は、リポジトリのルートからの相対パスで読み込んでいるので、ルートで実行する）

練習: [01_display_page/practice01.py](01_display_page/practice01.py)（「# ★」の部分が空欄になっているので、サンプルを見ながら自分の手でコードを打ち込んで完成させよう）

動いたら、書き換えてもう一度動かし、変化を確認する。

| 試すこと | 確認すること |
| --- | --- |
| `page = 1` → `page = 2` | 最初にページ2の画像（flower2）が表示される |
| `page = 3` | 何も描かれず、画面は黒のままになる（ページ3の関数も分岐も無いため、どの関数も呼ばれない） |
| `screen.blit(img1, (0, 0))` の `(0, 0)` → `(100, 100)` | 画像が右下にずれる。画面を塗りつぶしていないので、空いた部分は黒のまま |
| `page == 1` の分岐を消す | ページ1が表示されず、黒い画面のままになる |

---

# ボタンでページを切り替える

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
NEXT_BTN_POS = (600, 540)

def page1():
    screen.blit(img1, (0, 0))
    btn1 = screen.blit(next_img, NEXT_BTN_POS)  # blit の戻り値がボタンの Rect
    button_to_jump(btn1, 2)                     # btn1 を押したらページ2へ
```

サンプル: [02_btn_to_jump/ex02.py](02_btn_to_jump/ex02.py)

練習: [02_btn_to_jump/practice02.py](02_btn_to_jump/practice02.py)

| 試すこと | 確認すること |
| --- | --- |
| `NEXT_BTN_POS` の `(600, 540)` → `(100, 100)` | ボタンが移動し、反応する場所も新しい位置に移る（`btn1` は、画像を描いた範囲だから） |
| `page1` の `button_to_jump(btn1, 2)` → `(btn1, 1)` | ボタンを押してもページ1のまま（自分自身へ移動するため） |
| `pushFlag = True` の行を消す | ボタンを押し続けると、1フレームごとにページ1とページ2が入れ替わり続ける（移動先のページにも同じ位置にボタンがあり、まだ押されているため） |
| `global page, pushFlag` の行を消す | `UnboundLocalError` になる（`page` や `pushFlag` が、外の変数ではなくローカル変数として扱われるため。→ [06_function](../06_function/README.md)） |

## ページを追加する

```
1. 画像の読み込みを追加する
2. ページ切り替え関数を追加する
3. ループを修正する
```

サンプル: [02_btn_to_jump/ex03.py](02_btn_to_jump/ex03.py)

練習: [02_btn_to_jump/practice03.py](02_btn_to_jump/practice03.py)

| 試すこと | 確認すること |
| --- | --- |
| ボタンを順番に押していく | ページ1 → 2 → 3 → 4 → 1 の順に進み、ページ4のボタンでページ1に戻る |
| `page4` の `button_to_jump(btn1, 1)` → `(btn1, 2)` | ページ4の次はページ2になり、ページ1には戻れなくなる |
| `page2` の `button_to_jump(btn1, 3)` → `(btn1, 1)` | ページ1と2を行き来するだけで、ページ3・4には行けなくなる |

---

# 枝分かれの紙芝居

1つのページに複数のボタンを置いて、押したボタンに応じて異なるページへ進む

```python
def page1():
    screen.blit(img1, (0, 0))
    btn1 = screen.blit(next_img, (90, 220))   # 左ボタン → ページ2へ
    btn2 = screen.blit(next_img, (590, 220))  # 右ボタン → ページ3へ
    button_to_jump(btn1, 2)
    button_to_jump(btn2, 3)
```

サンプル: [03_page_branch/ex04.py](03_page_branch/ex04.py)

練習: [03_page_branch/practice04.py](03_page_branch/practice04.py)

| 試すこと | 確認すること |
| --- | --- |
| 左のボタン・右のボタンを押す | 左はページ2、右はページ3に進む |
| `button_to_jump(btn1, 2)` と `(btn2, 3)` の数字を入れ替える | 左のボタンがページ3、右のボタンがページ2に進むようになる |
| 2つのボタンの間（何もない場所）をクリックする | 何も起こらない（ボタンの範囲に入っていないため） |
| `REPLAY_BTN_POS` の `(600, 520)` → `(100, 100)` | ページ2・3のリプレイボタンが、どちらも左上に表示される（位置を定数にしているので、1か所の変更で両方変わる） |

## 枝分かれを追加する

```
ページ1 → ページ2, 3 へ分岐 (NEXT)
ページ3 → ページ4, 5 へ分岐 (NEXT)
ページ2, 4, 5 → ページ1 へ戻る (リトライ)
```

サンプル: [03_page_branch/ex05.py](03_page_branch/ex05.py)

練習: [03_page_branch/practice05.py](03_page_branch/practice05.py)

| 試すこと | 確認すること |
| --- | --- |
| ページ1の右のボタンでページ3へ進み、左・右のボタンを押す | 左はページ4、右はページ5に進む |
| `page3` の `button_to_jump(btn1, 4)` と `(btn2, 5)` の数字を入れ替える | 左のボタンがページ5、右のボタンがページ4に進むようになる |
| `page2` のリプレイボタンのジャンプ先 `1` → `3` | ページ2のリプレイボタンを押すと、ページ1ではなくページ3に進む |
