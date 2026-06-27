import pygame as pg

pg.init()

#-------------------------------------------------------------------------------
# 変数
#-------------------------------------------------------------------------------

# ウィンドウの作成
screen_width = 600
screen_height = 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('ox ゲーム')

# 色の設定
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# フォントの設定
font = pg.font.SysFont(None, 100)

# ボード(0: 空白、1: 〇、-1: ×)
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

number = 1  # 1: 〇、-1: ×

#-------------------------------------------------------------------------------
# 関数
#-------------------------------------------------------------------------------

# グリッド線の描画
def draw_grid():
    for i in range(1, 3):
        pg.draw.line(screen, BLACK, (0, i * 200), (screen_width, i * 200), 5)
        pg.draw.line(screen, BLACK, (i * 200, 0), (i * 200, screen_height), 5)

# ボードの描画
def draw_board():
    for row_index in range(3):
        for col_index in range(3):
            col = board[row_index][col_index]
            if col == 1:
                pg.draw.circle(screen, RED, (col_index * 200 + 100, row_index * 200 + 100), 80, 5)
            elif col == -1:
                pg.draw.line(screen, BLUE, (col_index * 200 + 20, row_index * 200 + 20),
                             (col_index * 200 + 180, row_index * 200 + 180), 5)
                pg.draw.line(screen, BLUE, (col_index * 200 + 180, row_index * 200 + 20),
                             (col_index * 200 + 20, row_index * 200 + 180), 5)

# 文字描画用関数
def draw_message(main_text, sub_text=None, main_pos=(200, 200), sub_pos=(100, 400)):
    """ 画面に文字を描画する """
    main_img = font.render(main_text, True, BLACK, GREEN)
    screen.blit(main_img, main_pos)
    if sub_text:
        sub_img = font.render(sub_text, True, BLACK, GREEN)
        screen.blit(sub_img, sub_pos)

# 勝利／引き分けの確認
def check_winner():
    winner = None
    game_over = False
    size = len(board)

    # 横列・縦列の確認
    for row_index in range(size):
        # 横列
        if sum(board[row_index]) == size:
            winner = 'o'
        if sum(board[row_index]) == -size:
            winner = 'x'
        # 縦列
        col_sum = 0
        for i in range(size):
            col_sum += board[i][row_index]
        if col_sum == size:
            winner = 'o'
        if col_sum == -size:
            winner = 'x'

    # 斜めの確認
    diag1, diag2 = 0, 0
    for i in range(size):
        diag1 += board[i][i]
        diag2 += board[i][size - 1 - i]
    if diag1 == size or diag2 == size:
        winner = 'o'
    if diag1 == -size or diag2 == -size:
        winner = 'x'

    # 勝敗表示
    if winner == 'o' or winner == 'x':
        draw_message(winner + ' Win!', 'click to reset')
        game_over = True
    else:
        # 全セルが0以外かどうかチェック（引き分け）
        all_filled = True
        for row in board:
            for cell in row:
                if cell == 0:
                    all_filled = False
                    break
            if not all_filled:
                break
        if all_filled:
            draw_message('Draw!', 'click to reset')
            game_over = True

    return game_over

#-------------------------------------------------------------------------------
# メインループ
#-------------------------------------------------------------------------------

run = True
while run:

    # 背景の塗りつぶし
    screen.fill(WHITE)

    # マウスの位置の取得
    mx, my = pg.mouse.get_pos()
    x = mx // 200
    y = my // 200

    # グリッド線の描画
    draw_grid()

    # ボードの描画
    draw_board()

    # 勝利の確認
    game_over = check_winner()

    # イベントの取得
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False

        # マウスのクリック
        if event.type == pg.MOUSEBUTTONDOWN:
            if not game_over:
                if board[y][x] == 0:
                    board[y][x] = number
                    number *= -1

            # リトライ機能
            if game_over:
                board = [
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]
                ]
                number = 1

    # 更新
    pg.display.update()

#-------------------------------------------------------------------------------
pg.quit()
