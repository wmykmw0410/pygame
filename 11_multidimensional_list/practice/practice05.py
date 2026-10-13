"""
練習5: for文でリストの要素を取り出す
example/ex05.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(for で要素を順に取り出す → enumerate でインデックスも一緒に取り出す)
このプログラムはウィンドウを開かず、ターミナルに結果を表示する
実行のしかた: リポジトリのルートで python 11_multidimensional_list/practice/practice05.py

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  実行する前に、結果を予想してみよう
  1. for fruit in fruits: を for fruit in fruits[::-1]: に変える → 順番はどうなる?
  2. fruits を空のリスト [] にする → 何が表示される?
  3. print(f"{i}: {fruit}") を print(f"{i + 1}: {fruit}") に変える → 番号はどうなる?
"""
# ★ リスト fruits を ["apple", "banana", "cherry"] で作る

# ★ for 文で、fruits の要素を順番に取り出して表示する

print("---")

# ★ enumerate を使って、インデックスと要素を同時に取り出し、「0: apple」のように表示する
