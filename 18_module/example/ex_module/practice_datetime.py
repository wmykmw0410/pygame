"""
練習: datetime モジュール
ex_datetime.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(datetime をインポートする → 今日の日付と、今の時・分・秒を表示する)
実行のしかた: リポジトリのルートで python 18_module/example/ex_module/practice_datetime.py

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  実行する前に、表示される結果を予想してみよう
  1. print(d.hour) を print(d.year) / print(d.month) / print(d.day) に変える → 表示は?
  2. print(today) を print(today.strftime("%Y/%m/%d")) に変える → 表示は?
  3. print(d) だけを書いて実行する → 表示は?
"""
# ★ datetime モジュールをインポートする

# ★ datetime.date.today() で今日の日付を today に入れ、表示する

# ★ datetime.datetime.now() で今の日時を d に入れ、d.hour, d.minute, d.second をそれぞれ表示する
