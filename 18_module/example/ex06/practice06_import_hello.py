"""
練習6: __name__ == "__main__"
ex06/hello.py と import_hello.py を見ながら、practice06_hello.py と、このファイルの「# ★」の下に同じコードを自分で打ち込もう
実行のしかた:
  リポジトリのルートで python 18_module/example/ex06/practice06_hello.py (直接実行)
  リポジトリのルートで python 18_module/example/ex06/practice06_import_hello.py (インポート)

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  実行する前に、表示される結果を予想してみよう
  1. practice06_hello.py の if __name__ == "__main__": を消して(say_hello() だけにして)、2つのファイルを実行する → 表示は?
  2. practice06_hello.py に print(__name__) を書いて、2つのファイルを実行する → 表示は?
  3. practice06_import_hello.py に practice06_hello.say_hello() を書く → 表示は?
"""
# ★ practice06_hello をインポートする
