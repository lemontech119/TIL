n = int(input())
go_list = input().split()

x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']


for go in go_list:
    if n >= x + dx[move.index(go)] >= 1:
        if n >= y + dy[move.index(go)] >= 1:
            x = x + dx[move.index(go)]
            y = y + dy[move.index(go)]

print(x, y)