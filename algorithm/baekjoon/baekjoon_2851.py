# https://www.acmicpc.net/problem/2851


mushroom_list = []
result = 0
mario = 0
for i in range(10):
    mushroom_list.append(int(input()))

for mushroom in mushroom_list:
    mario += mushroom
    if abs(mario-100) <= abs(result-100):
        result = mario

print(result)

