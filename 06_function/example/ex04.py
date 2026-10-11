"""グローバル変数"""
message = "こんにちは"  # グローバル変数: プログラム全体で有効

def greet():
    print(message)  # 関数の中からも参照できる

greet()  # 出力: こんにちは
