def solution(arr):
    answer = True
    arr.sort()
    for num, chk in enumerate(arr):
        if num+1 != len(arr):
            if chk+1 != arr[num+1]:
                answer = False
                break

    return answer


print(solution([4, 1, 3]))