def solution(S):
    alpha_num = [0] * 26
    answer = 0
    for alpha in S:
        asc = ord(alpha) - 97
        alpha_num[asc] += 1

    for chk in alpha_num:
        if chk % 2 == 1:
            answer += 1

    return answer


print(solution("aabbbccd"))
print(solution("abebeaedeac"))