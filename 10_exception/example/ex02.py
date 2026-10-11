"""文字列を入力した時に例外処理を実行するプログラム"""

# 関数：入力された変数を表示
def display_number():
    try:
        # 例外発生が想定される処理
        num = int(input("数字を入力してください："))
        print(f"入力された数字は{num}です")
    
    # ValueErrorが発生した時の処理
    except ValueError:
        print("入力は無効です。整数を入力してください。")
        
# ループ
while True:
    display_number()