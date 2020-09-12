# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    one, two, three = 0, 0, 0
    one_case = [1, 2, 3, 4, 5]
    two_case = [2, 1, 2, 3, 2, 4, 2, 5]
    three_case = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for _ in range(12):
        one_case += one_case
        two_case += two_case
        three_case += three_case

    for num, test in enumerate(answers):
        if one_case[num] == test:
            one += 1
        if two_case[num] == test:
            two += 1
        if three_case[num] == test:
            three += 1
    correct = max(one, two, three)
    answer = []
    if correct == one:
        answer.append(1)
    if correct == two:
        answer.append(2)
    if correct == three:
        answer.append(3)

    return answer


# def solution(answers):
#     pattern1 = [1,2,3,4,5]
#     pattern2 = [2,1,2,3,2,4,2,5]
#     pattern3 = [3,3,1,1,2,2,4,4,5,5]
#     score = [0, 0, 0]
#     result = []
#
#     for idx, answer in enumerate(answers):
#         if answer == pattern1[idx%len(pattern1)]:
#             score[0] += 1
#         if answer == pattern2[idx%len(pattern2)]:
#             score[1] += 1
#         if answer == pattern3[idx%len(pattern3)]:
#             score[2] += 1
#
#     for idx, s in enumerate(score):
#         if s == max(score):
#             result.append(idx+1)
#
#     return result