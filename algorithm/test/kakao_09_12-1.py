import re


def solution(new_id):
    first_id = new_id.lower()
    second_id = ''.join(re.findall('[0-9a-z-_.]', first_id))
    if len(second_id) < 2:
        third_id = second_id
    else:
        third_id = second_id[0]
        for i in range(1, len(second_id)):
            if second_id[i] != ".":
                third_id += second_id[i]
            elif second_id[i-1] != second_id[i]:
                third_id += second_id[i]
    fourth_id = third_id
    if len(fourth_id) == 0:
        pass
    elif len(fourth_id) == 1:
        if third_id[0] == '.':
            fourth_id = third_id[1:]
    elif len(fourth_id) > 1:
        if third_id[0] == '.':
            fourth_id = third_id[1:]
        if fourth_id[len(fourth_id)-1] == '.':
            fourth_id = fourth_id[:len(fourth_id)-1]
    fifth_id = fourth_id
    if len(fifth_id) == 0:
        fifth_id = "a"
    sixth_id = fifth_id
    if len(sixth_id) >= 16:
        sixth_id = sixth_id[0:15]
        if sixth_id[14] == '.':
            sixth_id = sixth_id[0:14]
    seventh_id = sixth_id
    if len(seventh_id) <= 2:
        while len(seventh_id) != 3:
            seventh_id = seventh_id + seventh_id[-1]

    answer = seventh_id
    return answer


