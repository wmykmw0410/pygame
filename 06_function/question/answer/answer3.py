"""好きな食べ物をいくつでも受け取り、一覧を表示する関数 list_foods を作成せよ
個数が変わっても対応できるように、可変長位置引数(*args)を使うこと

呼び出し方：list_foods("カレー", "寿司", "ラーメン")

出力結果：
        好きな食べ物：
        カレー
        寿司
        ラーメン
"""

def list_foods(*foods):
    print("好きな食べ物：")
    for food in foods:
        print(food)

list_foods("カレー", "寿司", "ラーメン")