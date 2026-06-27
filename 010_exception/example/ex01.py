"""文字列を入力した時に例外が発生するプログラム"""

# 関数：入力された変数を表示
def display_number():
    num = int(input("数字を入力してください："))
    print(f"入力された数字は{num}です")
    
# ループ
while True:
    display_number()