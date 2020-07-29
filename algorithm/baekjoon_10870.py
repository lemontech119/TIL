# https://www.acmicpc.net/problem/10870


def Fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return Fibonacci(num-1) + Fibonacci(num-2)


num = int(input())
print(Fibonacci(num))
