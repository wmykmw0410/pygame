"""
練習2: 文字列を入力した時に例外処理を実行するプログラム
example/ex02.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(try / except で ValueError をキャッチして、メッセージを表示する)
このプログラムはウィンドウを開かず、ターミナルで動かす
実行のしかた: リポジトリのルートで python 10_exception/practice/practice02.py
(終わらないループなので、止めるときは Ctrl+C を押す)

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  実行する前に、結果を予想してみよう
  1. "abc" を入力する → どうなる? そのあとも入力できる?
  2. except ValueError を except TypeError に変えて、"abc" を入力する → どうなる? なぜ?
  3. int(input(...)) を 10 / int(input(...)) に変えて(表示の文も変える)、0 を入力する → どうなる?
  4. 3 の状態で、except ZeroDivisionError: を足して、メッセージを表示する → 0 を入力するとどうなる?
  5. print(f"入力された数字は{num}です") を try の外に出す(字下げを1段浅くする) → "abc" を入力するとどうなる?
"""
# ★ 関数 display_number を作る
#   try: input で入力を受け取り int に変換して num に代入する → 「入力された数字はnumです」と表示する
#   except ValueError: 「入力は無効です。整数を入力してください。」と表示する

# ★ while True: で display_number() をくり返し呼び出す
