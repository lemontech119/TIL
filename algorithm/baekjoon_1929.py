## https://www.acmicpc.net/problem/1929
import math

num_one, num_two = map(int, input().split(' '))


def check_decimal(num):
    if num == 1:
        return False
    n = int(math.sqrt(num))
    for i in range(2, n + 1):
        if num % i == 0:
            return False
    return num


for num in range(num_one, num_two+1):
    if check_decimal(num):
        print(num)

