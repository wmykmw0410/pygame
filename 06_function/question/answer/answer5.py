"""数値を受け取り、負の数なら早期returnでNoneを返し、
0以上の数ならその2乗を返す関数 safe_square を作成せよ

呼び出し方：safe_square(9) / safe_square(-4)

出力結果：
        81
        None
"""

def safe_square(x):
    if x < 0:
        return None  # 早期return: 負の数はここで抜ける
    return x ** 2

print(safe_square(9))    # 出力: 81
print(safe_square(-4))   # 出力: None
