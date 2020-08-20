# https://www.acmicpc.net/problem/1018

n, m = map(int, input().split())
chess_board = [list(input()) for _ in range(n)]
white_board, black_board = [], []
min_answer = 64

for made in range(8):
    if made % 2 == 0:
        white_board.append(["W", "B"] * int(m / 2))
        black_board.append(["B", "W"] * int(m / 2))
    elif made % 2 == 1:
        white_board.append(["B", "W"] * int(m / 2))
        black_board.append(["W", "B"] * int(m / 2))

for row in range(n-7):
    for column in range(m-7):
        chk_white, chk_black = 0, 0
        a = 0
        for x in range(row, row + 8):
            b = 0
            for y in range(column, column + 8):
                if chess_board[x][y] != white_board[a][b]:
                    chk_white += 1
                if chess_board[x][y] != black_board[a][b]:
                    chk_black += 1
                b += 1
            a += 1
        if min_answer > min(chk_white, chk_black):
            min_answer = min(chk_white, chk_black)

print(min_answer)
