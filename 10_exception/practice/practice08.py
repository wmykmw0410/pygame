"""
練習8: Noneオブジェクトの使用例
example/ex08.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(None かどうかを is で調べる)
このプログラムはウィンドウを開かず、ターミナルで動かす
実行のしかた: リポジトリのルートで python 10_exception/practice/practice08.py

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  実行する前に、結果を予想してみよう
  1. value = None を value = 0 や value = "" に変える → 何が表示される?
  2. value = None の行を消す → どうなる?
  3. value is None を value == None に変える → 結果は同じ?
  4. value = None を value = "None"(文字列)に変える → 何が表示される?
"""
# ★ 変数 value に None を代入する

# ★ value が None なら「Noneです」、そうでなければ「Noneではない」と表示する(is を使う)
