n, k = map(int, input().split())

result = 0

# 설명 보기 전에 직접 짠 코드 (문제점 => K의 값이 높아지게 될 경우 실행시간의 문제 발생)
# while n != 1:
#     if n % k == 0:
#         n = n / k
#         result += 1
#     else:
#         n -= 1
#         result += 1
#
# print(result)

while True:
    target = (n//k) * k
    result += (n-target)
    n = target

    if n < k:
        break
    result += 1
    n //= k

result += (n-1)
print(result)