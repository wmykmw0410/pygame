"""
練習7: Exceptionクラス
example/ex07.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(Exception を raise する)
このプログラムはウィンドウを開かず、ターミナルで動かす
実行のしかた: リポジトリのルートで python 10_exception/practice/practice07.py

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  実行する前に、結果を予想してみよう
  1. Exception を ValueError に変える → エラーの最後の行はどう変わる?
  2. try: raise ValueError("x") / except Exception as e: で、ValueError を Exception でキャッチする → キャッチされる?
  3. try: raise Exception("x") / except ValueError as e: で、Exception を ValueError でキャッチする → キャッチされる?
  4. try: 1 / 0 / except ArithmeticError as e: → キャッチされる?(ZeroDivisionError は ArithmeticError の仲間)
  5. [][0] を、except LookupError でキャッチする → キャッチされる?(IndexError は LookupError の仲間。README の「例外クラスの継承階層」を参照)
"""
# ★ raise 文で、Exception を「エラーメッセージ」というメッセージつきで発生させる
