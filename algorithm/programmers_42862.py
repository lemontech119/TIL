# https://programmers.co.kr/learn/courses/30/lessons/42862


def solution(n, lost, reserve):
    lost_set = list(set(lost) - set(reserve))
    reserve_set = list(set(reserve) - set(lost))
    workout = n - len(lost_set)
    for i in reserve_set:
        if i-1 in lost_set:
            lost_set.remove(i-1)
            workout += 1
        elif i+1 in lost_set:
            lost_set.remove(i+1)
            workout += 1
    answer = workout
    return answer


