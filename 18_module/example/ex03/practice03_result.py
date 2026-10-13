"""
練習3: from ... import で、指定した関数だけが使える
ex03/greeting3.py と result3.py を見ながら、practice03_greeting.py と、このファイルの「# ★」の下に同じコードを自分で打ち込もう
実行のしかた: リポジトリのルートで python 18_module/example/ex03/practice03_result.py

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  実行する前に、表示される結果を予想してみよう
  1. greetingA() の下に greetingB() を書く → どうなる?
  2. from practice03_greeting import greetingA を、greetingA, greetingB の2つに変えて、greetingB() を呼ぶ → どうなる?
  3. from ... import をやめて import practice03_greeting にし、practice03_greeting.greetingA() で呼ぶ → どうなる?
  4. 3. のまま greetingA() と書く(モジュール名を付けない) → どうなる?
"""
# ★ practice03_greeting から greetingA だけをインポートする

# ★ "A" を表示し、greetingA() を呼び、"B" を表示する
