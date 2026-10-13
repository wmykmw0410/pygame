"""
練習6: raise文の使用例(関数の条件チェック)
example/ex06.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(関数の中で条件に合わないとき raise する → 呼び出し側で try / except でキャッチする)
このプログラムはウィンドウを開かず、ターミナルで動かす
実行のしかた: リポジトリのルートで python 10_exception/practice/practice06.py

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  実行する前に、結果を予想してみよう
  1. calc_speed(10, 0) を calc_speed(10, 2) に変える → 何が表示される?
  2. calc_speed(10, -1) にする → どうなる?
  3. except ValueError as e を except ZeroDivisionError as e に変える → どうなる?
  4. 関数の中の if 〜 raise の2行を消す → (10, 0) で何が起きる? その例外は except ValueError でキャッチされる?
"""
# ★ 距離 dist と時間 time を受け取る関数 calc_speed を作る
#   time が 0 以下なら、ValueError を「時間は0より大きい値を入力してください。」のメッセージで raise する
#   そうでなければ dist / time を return する

# ★ try: calc_speed(10, 0) を呼び出して speed に代入し、「時速はspeedkm/hです。」と表示する
#   except ValueError as e: e を表示する
