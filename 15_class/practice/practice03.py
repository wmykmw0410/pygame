"""
練習3: 継承
example/ex03.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(Animal を親にして Dog / Cat / GuideDog を作る → 同じメソッド名で呼び出す)
このプログラムはウィンドウを開かず、ターミナルに結果を表示する
実行のしかた: リポジトリのルートで python 15_class/practice/practice03.py

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  実行する前に、表示される結果を予想してみよう
  1. Cat クラスの speak メソッドを消す(Cat の中を pass だけにする) → クロとミケの表示は?
  2. Dog クラスの speak メソッドを消す → シロとハチの表示は? GuideDog の speak() は?
  3. GuideDog の __init__ から super().__init__(name) の行を消す → どうなる?
  4. Animal を継承した Bird クラスを作り(speak で「ピヨ！」と表示)、animals に Bird("ピー") を足す → 表示は?
"""
# ★ Animal クラスを定義する(__init__ で name を持ち、speak で "名前: ..." と表示する)


# ★ Animal を継承した Dog クラスを定義する(speak を上書きして "名前: ワン！" と表示する)


# ★ Animal を継承した Cat クラスを定義する(speak を上書きして "名前: ニャー！" と表示する)


# ★ Dog を継承した GuideDog クラスを定義する
#   __init__(self, name, owner): super().__init__(name) を呼び、self.owner に代入する
#   guide(self): "名前 が 飼い主 を誘導しています" と表示する


# ★ animals = [Dog("シロ"), Cat("クロ"), Dog("ハチ"), Cat("ミケ")] を作り、for で全員の speak() を呼ぶ

print("---")

# ★ GuideDog("アポロ", "田中さん") を作り、speak() と guide() を呼ぶ
