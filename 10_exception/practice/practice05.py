"""
練習5: raise文の使用例
example/ex05.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(raise で NameError を発生させる)
このプログラムはウィンドウを開かず、ターミナルで動かす
実行のしかた: リポジトリのルートで python 10_exception/practice/practice05.py

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  実行する前に、結果を予想してみよう
  1. NameError を ValueError や ZeroDivisionError に変える → エラーの最後の行はどう変わる?
  2. メッセージ("エラーテスト")を変える → どこに表示される?
  3. raise の下に print("この行は実行される?") を足す → 表示される?
  4. raise を try: に入れて、except NameError as e: print(e) でキャッチする → どうなる?
"""
# ★ raise 文で、NameError を「エラーテスト」というメッセージつきで発生させる
