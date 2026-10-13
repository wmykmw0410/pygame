"""
練習2: 複数のインスタンス
example/ex02.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(Player クラスは ex01 と同じ。2つのインスタンスが独立していること、リストでまとめて処理することを確かめる)
このプログラムはウィンドウを開かず、ターミナルに結果を表示する
実行のしかた: リポジトリのルートで python 15_class/practice/practice02.py

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  実行する前に、表示される結果を予想してみよう
  1. p1.take_damage(30) を p2.take_damage(30) に変える → どちらの HP が減る?
  2. party に Player("僧侶", 60) を足す → 表示は何行になる?
  3. for の中の take_damage(10) を take_damage(50) に変える → 表示は?
  4. p2 = Player("魔法使い", 80) を p2 = p1 に変える → p1.take_damage(30) のあと、p2 の HP は?
"""
# ★ Player クラスを定義する(ex01 と同じ)


# ★ p1 = Player("勇者", 100)、p2 = Player("魔法使い", 80) を作る

# ★ p1.take_damage(30) を呼び、p1.show_status() と p2.show_status() を呼ぶ

print("---")

# ★ party = [勇者(100), 魔法使い(80), 戦士(120)] のリストを作る

# ★ for で全員に take_damage(10) を呼ぶ

# ★ for で全員の show_status() を呼ぶ
