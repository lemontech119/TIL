def solution(bricks):
    answer = 0

    for i in range(len(bricks)):
        max_height_left = max(bricks[:i+1])
        max_height_right = max(bricks[i:])
        min_height = min(max_height_left, max_height_right)
        answer += (min_height - bricks[i])

    return answer


print(solution([0, 2, 0, 1, 3, 1, 2, 0, 1, 0, 2, 0]))
print(solution([1, 2, 3, 4, 5, 6, 7]))