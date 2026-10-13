"""
練習5: global 宣言(グローバル変数の書き換え)
example/ex05.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(global 宣言をつけた関数と、つけない関数を比べる)
このプログラムはウィンドウを開かず、ターミナルに結果を表示する
実行のしかた: リポジトリのルートで python 06_function/practice/practice05.py

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  実行する前に、表示される結果を予想してみよう
  1. increment() を3回続けて呼ぶ → count はいくつになる?
  2. increment の global count の行を消して呼ぶ → どうなる?
  3. 関数の中で count を書き換えず、print(count) だけにする → global は必要?
"""
# ★ グローバル変数 count を 0 にしておく

# ★ global 宣言なしで count += 1 をする関数 increment_wrong を定義する


# ★ global 宣言をして count += 1 をする関数 increment を定義する


# ★ count を表示する

# ★ increment_wrong() を呼んで、エラーが出ることを try / except UnboundLocalError で確かめる

# ★ increment() を呼んで、count を表示する
