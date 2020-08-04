## https://www.acmicpc.net/problem/11047

import sys


length, money = map(int, sys.stdin.readline().split())

coin_pocket = list()
coin_number = 0
greedy = 0

for i in range(length):
    coin = int(sys.stdin.readline())
    coin_pocket.append(coin)

while money != 0:
    for coin in coin_pocket:
        if greedy < coin <= money:
            greedy = coin
    coin_number += int(money/greedy)
    money = money % greedy
    greedy = 0

print(coin_number)

