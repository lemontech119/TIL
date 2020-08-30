def solution(arr):
    answer = []
    for num, chk in enumerate(arr):
        if num == 0:
            answer.append(chk)
        elif arr[num] != arr[num-1]:
            answer.append(chk)
    return answer


