"""リスト形式で用意されている生徒6人の名簿を
五十音順に1人ずつ出力するプログラムを作る"""

# 生徒の名簿
students = ["たかはし", "いとう", "さとう", "うえの", "おおた", "やまだ"]

# 並び替え
students.sort()

# 1人ずつ出力
for student in students:
    print(student)