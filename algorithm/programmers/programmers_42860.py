# https://programmers.co.kr/learn/courses/30/lessons/42860
import math


def solution(name):
    ran = math.ceil((len(name)/2))
    result = 99999999999999999
    for num in range(ran):
        compare_name = "A" * len(name)
        compare_list = list(compare_name)
        number = 0
        answer = 0
        right = True
        while compare_name != name:
            up = alphabet.index(name[number])
            down = 26 - alphabet.index(name[number])
            if up >= down:
                answer += down
            elif down > up:
                answer += up
            compare_list[number] = name[number]
            if num == number:
                if number == 0:
                    number = len(name)-1
                else:
                    number -= 1
                right = False
            elif right:
                number += 1
            elif not right:
                if number == 0:
                    number = len(name) - 1
                else:
                    number -= 1
            compare_name = ''.join(compare_list)
            if compare_name != name:
                answer += 1
        result = min(result, answer)

    return result


alphabet = []
for i in range(65, 91):
    alphabet.append(chr(i))
