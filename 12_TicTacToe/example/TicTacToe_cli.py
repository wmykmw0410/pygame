"""マルバツゲーム CLI版"""

# 3×3のボード（0: 空白, 1: ○, -1: ×）
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
current = 1  # 1: 先攻, -1: 後攻

def print_board():
    for row in board:
        print(*row)
    print()

def check_winner():
    size = len(board)
    for i in range(size):
        # 横
        if sum(board[i]) == size:  return 1
        if sum(board[i]) == -size: return -1
        # 縦
        col = 0
        for r in range(size):
            col += board[r][i]
        if col == size:  return 1
        if col == -size: return -1
    # 斜め
    d1, d2 = 0, 0
    for i in range(size):
        d1 += board[i][i]
        d2 += board[i][size - 1 - i]
    if d1 == size or d2 == size:  return 1
    if d1 == -size or d2 == -size: return -1
    # 引き分け
    empty = 0
    for r in range(size):
        for c in range(size):
            if board[r][c] == 0:
                empty += 1
    if empty == 0:
        return "draw"
    return None

# メインループ
while True:
    print_board()
    row = int(input(f"{current} 行(0-2): "))
    col = int(input(f"{current} 列(0-2): "))

    if board[row][col] != 0:
        print("そのマスは埋まっています\n")
        continue

    board[row][col] = current
    result = check_winner()

    if result == "draw":
        print_board()
        print("引き分け！")
        break
    elif result is not None:
        print_board()
        print(f"{result} の勝ち！")
        break

    current *= -1  # プレイヤー交代
