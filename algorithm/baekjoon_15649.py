# https://www.acmicpc.net/problem/15649

import sys


n, m = map(int, sys.stdin.readline().split())

check = [False for i in range(n + 1)]
subs = [i for i in range(m)]


def go(idx, n, m):
    if idx == m:
        print(' '.join(map(str, subs)))
        return
    else:
        for i in range(1, n + 1):
            if check[i] == False:
                check[i] = True
                subs[idx] = i
                go(idx + 1, n, m)
                check[i] = False

go(0, n, m)