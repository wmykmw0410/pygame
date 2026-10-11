"""ユーザー情報を受け取り、キーと値を表示する関数 show_user_info を作成せよ
キーの種類が変わっても対応できるように、可変長キーワード引数(**kwargs)を使うこと

呼び出し方：show_user_info(name="太郎", age=20, hobby="ゲーム")

出力結果：
        name：太郎
        age：20
        hobby：ゲーム
"""

def show_user_info(**info):
    for key, value in info.items():
        print(f"{key}：{value}")

show_user_info(name="太郎", age=20, hobby="ゲーム")
