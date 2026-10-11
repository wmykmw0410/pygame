"""
二次元リストmatrixを時計回りに90度回転させた
二次元リストrotated_matrixを出力する

rotated_matrix
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
<ポイント>
・最初にrotated_matrixをmatrixと同じサイズに初期化する
・matrixの列番号がrotated_matrixの行番号になる
・matrixの行番号を反転したものがrotated_matrixの列番号になる
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated_matrix = []
for _ in range(3):
    row = []
    for _ in range(3):
        row.append(None)
    rotated_matrix.append(row)


# rotated_matrix = [
#     [None, None, None],
#     [None, None, None],
#     [None, None, None]
#     ]


for i in range(len(matrix)):

    for j in range(len(matrix[i])):
        
        rotated_matrix[i][2-j] = matrix[j][i]

    print(rotated_matrix[i])
