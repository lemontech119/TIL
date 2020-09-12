## https://www.acmicpc.net/problem/2581


num_one = int(input())
num_two = int(input())

decimal_list = []
for num in range(num_one, num_two+1):
    cnt = 0
    if num == 1:
        continue
    for i in range(2, num+1):
        if num % i == 0:
            cnt = cnt + 1
    if cnt == 1:
        decimal_list.append(num)

if len(decimal_list) == 0:
    print(-1)
else:
    print(sum(decimal_list))
    print(decimal_list[0])
