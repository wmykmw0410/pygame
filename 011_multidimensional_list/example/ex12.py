"""要素番号を使って要素を取り出す"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# リストの長さを出力する
print(len(matrix))
print(len(matrix[0]))
print(len(matrix[1]))
print(len(matrix[2]))

# 二次元リスト内の一次元リストを1つずつ取り出す
for i in range(len(matrix)):
    
    # 一次元リスト内の要素を1つずつ取り出す
    for j in range(len(matrix[i])):

        # 要素を出力する 
        print(f"matrix[{i}][{j}]の要素は{matrix[i][j]}")