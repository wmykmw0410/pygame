"""
練習4: 関数を別ファイルに切り出して、インポートして使う
ex04/ex04.py と mycalc.py と testlist.py を見ながら、practice04_mycalc.py と、このファイルの「# ★」の下に同じコードを自分で打ち込もう
実行のしかた: リポジトリのルートで python 18_module/example/ex04/practice04_testlist.py

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  実行する前に、表示される結果を予想してみよう
  1. scorelist に 90 と 89 を足す → それぞれの評価は?
  2. practice04_mycalc.py の score >= 90 を score > 90 に変える → 90 点の評価は?
  3. import practice04_mycalc を from practice04_mycalc import gap に変えて、gap(score) で呼ぶ → どうなる?
  4. import practice04_mycalc as mc に変えて、mc.gap(score) で呼ぶ → どうなる?
"""
# ★ practice04_mycalc をインポートする

# ★ scorelist に [95, 75, 30, 85] のリストを作る

# ★ for で scorelist の点数を取り出し、「点数 点は、 評価」の形で表示する(評価は practice04_mycalc.gap(score))
