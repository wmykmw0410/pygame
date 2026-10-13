"""
練習5: パッケージを作って使う
ex05/calculation/ と import_add_sub.py などを見ながら、practice_calculation/ の3つのファイルと、このファイルの「# ★」の下に同じコードを自分で打ち込もう
(practice_calculation/ には、パッケージの目印になる __init__.py がある)
実行のしかた: リポジトリのルートで python 18_module/example/ex05/practice05_import.py

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  実行する前に、表示される結果を予想してみよう
  1. __init__.py の中身を全部消して、from practice_calculation import add, sub を実行する → どうなる?
  2. 1. のまま、from practice_calculation.addition import add に変える → どうなる?
  3. __init__.py の from .addition import add を from addition import add にする(. を消す) → どうなる?
  4. practice_calculation/__init__.py ファイルを別の名前に変える → どうなる?
"""
# ★ practice_calculation から add と sub をインポートする

# ★ add(1, 2) の結果を表示する

# ★ sub(1, 2) の結果を表示する
