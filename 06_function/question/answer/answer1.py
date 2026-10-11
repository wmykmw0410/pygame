"""名前を受け取ってあいさつを表示する関数 greet を作成せよ
引数にデフォルト値"ゲスト"を設定し、引数なしでも呼び出せるようにすること

呼び出し方：greet() / greet("太郎")

出力結果：
        Hello, ゲスト.
        Hello, 太郎.
"""

def greet(name="ゲスト"):
    print(f"Hello, {name}.")

greet()        # 出力: Hello, ゲスト.
greet("太郎")   # 出力: Hello, 太郎.
