# https://www.acmicpc.net/problem/4948


def check_decimal(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True


decimal_list = []
for num in range(2, 123456*2):
    if check_decimal(num):
        decimal_list.append(num)


num_list = []
while True:
    input_data = int(input())
    chk_num = 0
    if input_data == 0:
        break
    else:
        for i in decimal_list:
            if input_data < i <= input_data*2:
                chk_num += 1
        print(chk_num)