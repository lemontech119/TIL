def solution(arr):
    # 그리드 문제이기 때문에 가장 가치가 높은 종료시간을 우선적으로 정렬합니다.
    arr.sort(key=lambda x: (x[1], x[0]))
    answer, end_time = 0, arr[0][0]

    for meeting in arr:
        if end_time <= meeting[0]:
            end_time = meeting[1]
            answer += 1
    return answer

