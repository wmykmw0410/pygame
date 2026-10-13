"""
練習1: クラスを定義してインスタンスを使う
example/ex01.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(Player クラスを作る → インスタンスを作る → メソッドを呼ぶ)
このプログラムはウィンドウを開かず、ターミナルに結果を表示する
実行のしかた: リポジトリのルートで python 15_class/practice/practice01.py

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  実行する前に、表示される結果を予想してみよう
  1. Player("勇者", 100) を Player("魔法使い", 80) に変える → 表示は?
  2. take_damage(30) を take_damage(120) に変える → HP はどうなる?
  3. show_status の中の self.name を name に変える → どうなる?
  4. take_damage(30) を take_damage() に変える(引数を渡さない) → どうなる?
"""
# ★ Player クラスを定義する
#   __init__(self, name, hp): self.name と self.hp に代入する
#   take_damage(self, amount): self.hp を amount だけ減らす
#   show_status(self): "勇者 HP: 100" の形で表示する


# ★ Player("勇者", 100) でインスタンスを作り、player に入れる

# ★ show_status() を呼ぶ

# ★ take_damage(30) を呼んでから、show_status() を呼ぶ

# ★ take_damage(20) を呼んでから、show_status() を呼ぶ
