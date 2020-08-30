def solution(strs, t):
    answer = 0
    length = len(t)
    dp = [20001] * (length + 1)
    dp[length] = 0
    for i in range(length - 1, -1, -1):
        temp = ""
        for j in range(i, length):
            temp += t[j]
            if strs.count(temp) != 0:
                if dp[j + 1] != 20001:
                    dp[i] = min(dp[i], dp[j + 1] + 1)
            if j > i + 5:
                break
        if dp[0] != 20001:
            answer = dp[0]
        else:
            answer = -1

    return answer

