import itertools


def solution(orders, course):
    answer = []
    for idx, i in enumerate(orders):
        alpha_sort = sorted(list(i))
        orders[idx] = ''.join(alpha_sort)

    for k in course:
        order_list = []
        for j in orders:
            order_list += list(map(''.join, itertools.combinations(j, k)))
        count = {}
        for a in order_list:
            try: count[a] += 1
            except: count[a] = 1
        if len(count) != 0:
            count = sorted(count.items(), reverse = True,
                   key= lambda x: x[1])
            big_num = count[0][1]
            if big_num > 1:
                for chk in count:
                    if big_num == chk[1]:
                        answer.append(chk[0])
    answer = sorted(answer)
    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))