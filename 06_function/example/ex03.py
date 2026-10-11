"""ローカル変数"""
def greet():
    name = "Alice"  # ローカル変数: 関数の中でのみ有効
    print("Hello,", name)  # 出力: Hello, Alice

greet()
# print(name)  # エラー！関数の外からは name にアクセスできない（NameError）
