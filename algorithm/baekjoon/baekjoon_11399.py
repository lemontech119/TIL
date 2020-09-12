## https://www.acmicpc.net/problem/11399

N = int(input())
time_list = list(map(int, input().split()))
time_list = sorted(time_list)
sum_value = time_list[0]

for i in range(1, N):
    sum_value = sum_value + sum(time_list[:i + 1])

print(sum_value)