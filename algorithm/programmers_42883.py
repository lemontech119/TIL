def solution(number, k):
    number = str(number)
    number_list = list(map(int, number))
    chk_num = 0
    chk_big = 1
    chk_big_idx = 0
    for i in range(k):
        if number_list[i] == 9:
            chk_big = number_list[i]
            chk_big_idx = i
            break
        if chk_big < number_list[i]:
            chk_big = number_list[i]
            chk_big_idx = i
        chk_num += 1

    k -= chk_big_idx

    for j in range(chk_big_idx):
        number_list.pop(0)

    for z in range(len(number_list)):
        if k == 0:
            break
        if number_list[z] < number_list[z + 1]:
            number_list.pop(z)
            k -= 1
    answer = ''
    for last in number_list:
        answer = answer + str(last)
    return answer


number, k = map(int, input().split())
print(solution(number, k))
