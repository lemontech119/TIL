# https://www.acmicpc.net/problem/5543

burger_list = []
drink_list = []

for burger in range(3):
    burger_list.append(int(input()))

for drink in range(2):
    drink_list.append(int(input()))

print(min(burger_list)+min(drink_list) - 50)