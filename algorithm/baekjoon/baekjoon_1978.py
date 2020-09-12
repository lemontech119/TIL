## https://www.acmicpc.net/problem/1978


num = int(input())
num_list = list(map(int, input().split(' ')))
decimal_cnt = 0

for i in num_list:
    cnt = 0
    if i == 1:
        continue
    for j in range(2, i+1):
        if i % j == 0:
            cnt = cnt + 1
    if cnt == 1:
        decimal_cnt = decimal_cnt + 1


print(decimal_cnt)