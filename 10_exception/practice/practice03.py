"""
練習3: 文字列を入力した時に例外処理を実行するプログラム(as句)
example/ex03.py を見ながら、「# ★」の下に同じコードを自分で打ち込もう
(except ... as e で例外オブジェクトを受け取り、メッセージと型を表示する)
このプログラムはウィンドウを開かず、ターミナルで動かす
実行のしかた: リポジトリのルートで python 10_exception/practice/practice03.py
(終わらないループなので、止めるときは Ctrl+C を押す)

動いたら、書き換えてもう一度動かし、どう変わるか確認しよう(1つ変えたら元に戻してから次へ)
  実行する前に、結果を予想してみよう
  1. "abc" を入力する → 表示されるメッセージと、エラーの型は?
  2. 何も入力せずに Enter を押す → メッセージはどう変わる?
  3. type(e) を type(e).__name__ に変える → 型の表示はどう変わる?
  4. except ValueError as e を except Exception as e に変える → "abc" を入力すると、同じように処理される?
"""
# ★ 関数 display_number を作る
#   try: input で入力を受け取り int に変換して num に代入する → 「入力された数字はnumです」と表示する
#   except ValueError as e: e をエラー詳細として「エラーが発生しました：e」と表示し、type(e) を「エラーの型：…」と表示する

# ★ while True: で display_number() をくり返し呼び出す
