# https://programmers.co.kr/learn/courses/30/lessons/42839
import itertools

def solution(numbers):
    number_list = list(numbers)
    chk_list = []
    answer = 0

    for j in range(1, len(number_list)+1):
        chk_list += list(map(''.join, itertools.permutations(number_list, j)))

    chk_list = list(set(chk_list))

    for chk in chk_list:
        if chk[0] != '0':
            if decimal[int(chk)]:
                answer += 1
    return answer


LEN = 9999999
decimal = [False] + [True] * LEN
decimal[1] = False
m = int(LEN ** 0.5)
for i in range(2, m+1):
    if decimal[i] == True:
        for j in range(i+i, LEN+1, i):
            decimal[j] = False

