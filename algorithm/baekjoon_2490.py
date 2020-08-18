# https://www.acmicpc.net/problem/2490

import sys


game_list = []
for i in range(3):
    game = list(map(int, sys.stdin.readline().split()))
    game_list.append(game)

for result in game_list:
    yut = sum(result)
    if yut == 4:
        print("E")
    elif yut == 3:
        print("A")
    elif yut == 2:
        print("B")
    elif yut == 1:
        print("C")
    elif yut == 0:
        print("D")