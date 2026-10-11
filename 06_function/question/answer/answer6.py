"""数値のリストを受け取り、最小値と最大値をタプルで返す関数 min_max を作成せよ

呼び出し方：lo, hi = min_max([4, 1, 7, 3])

出力結果：
        1 7
"""

def min_max(numbers):
    return min(numbers), max(numbers)  # タプルとして返される

lo, hi = min_max([4, 1, 7, 3])
print(lo, hi)  # 出力: 1 7
