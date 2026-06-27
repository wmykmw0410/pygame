"""文字列を入力した時に例外処理を実行するプログラムでas句の活用"""

# 関数：入力された変数を表示
def display_number():
    try:
        # 例外発生が想定される処理
        num = int(input("数字を入力してください："))
        print(f"入力された数字は{num}です")
    
    # ValueErrorが発生した時の処理
    # 例外オブジェクトをeに格納
    except ValueError as e:
        
        # エラー詳細を出力
        print(f"エラーが発生しました：{e}")        
        
        # エラーの型を出力
        print(f"エラーの型：{type(e)}")        
        
# ループ
while True:
    display_number()