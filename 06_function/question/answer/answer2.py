"""次の関数 show_info を呼び出すとき、位置引数とキーワード引数を混ぜて使用する場合の
正しい呼び出し方を A〜D から1つ選べ（選んだら実際にコメントを外して実行し、確認しよう）"""

def show_info(name, age, country="日本"):
    print(f"{name}さん（{age}歳）は{country}出身です。")


# A. show_info("田中", country="アメリカ", 30)  # SyntaxError: キーワード引数の後に位置引数は置けない
# B. show_info("田中", 30, country="アメリカ")  # 正解
# C. show_info(name="田中", 30, "アメリカ")     # SyntaxError: キーワード引数の後に位置引数は置けない
# D. show_info(30, "田中", "アメリカ")          # 実行はできるが、name と age が逆で意味が変わってしまう

show_info("田中", 30, country="アメリカ")  # 出力: 田中さん（30歳）はアメリカ出身です。