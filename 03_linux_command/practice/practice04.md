# 練習4: Pythonファイルを実行する

README の「Pythonの実行」を見ながら、「★」の部分のコマンドを、自分の端末のターミナルで自分で打ち込もう。
（`python` で動かないときは `python3` を使う）

## 準備

```bash
cd ~
mkdir -p Practice
cd Practice
```

## 手順

```bash
# ★ 空のファイル game.py を作る

# ★ game.py に print("Hello, World") を書き込む

# ★ game.py の内容を確認する

# ★ 相対パス（./ を使う）で game.py を実行する
```

## 試してみよう

実行する前に、結果を予想してみよう。

1. `echo 'print("Hello, pygame")' > game.py` で書き換えて、もう一度実行する → 表示はどうなる?
2. `./` を付けずに `python game.py` を打つ → `./game.py` のときと違う?
3. `cd ..` で1つ上に移動してから `python ./game.py` を打つ → どうなる? なぜ?
4. そのまま（`Practice` の1つ上のまま）、`Practice/game.py` と相対パスで書いて実行する → どうなる?
5. `pwd` で `Practice` の絶対パスを確認して、どのフォルダからでも絶対パスで `game.py` を実行する → どうなる?
6. 確認できたら後片付けをする: ホームディレクトリへ移動して、`Practice` フォルダを中身ごと削除する
