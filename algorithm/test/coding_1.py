def solution(n, m):
    answer = 0
    for i in range(n, m+1):
        num = str(i)
        answer += palindrome(num)
    return answer


def palindrome(number):
    result = 1
    for j in range(len(number) // 2):
        if number[j] != number[-1 - j]:
            result = 0
            pass

    return result


