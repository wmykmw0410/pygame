"""global 宣言（グローバル変数の書き換え）"""
count = 0

def increment_wrong():
    count += 1  # UnboundLocalError: global なしに外の変数を変更しようとするとエラー

def increment():
    global count
    count += 1  # global をつけると外の変数を変更できる

print(count)   # 出力: 0 (グローバル変数はそのまま参照できる)

# increment_wrong() は実際に呼ぶとエラーになることを確認する
try:
    increment_wrong()
except UnboundLocalError as e:
    print(f"エラー発生: {e}")

increment()
print(count)   # 出力: 1
