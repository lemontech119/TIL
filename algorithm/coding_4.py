def solution(s):
    alpha_stack = []
    answer = 0
    for idx, num in enumerate(s):
        if len(alpha_stack) == 0:
            alpha_stack.append(num)
        ## top과 비교
        elif alpha_stack[-1] == num:
            alpha_stack.pop()
        elif alpha_stack[-1] != num:
            alpha_stack.append(num)
    if len(alpha_stack) == 0:
        answer = 1
    return answer
