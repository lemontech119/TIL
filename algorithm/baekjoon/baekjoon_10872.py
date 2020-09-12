def factorial(n, result=1):
    if n == 0:
        return result
    multiply = n * result
    n = n - 1
    return factorial(n, multiply)


num = int(input())
print(factorial(num))