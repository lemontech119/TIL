# https://www.acmicpc.net/problem/1920

import sys


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

a.sort()

for chk in x:
    if binary_search(a, chk, 0, n-1) is None:
        print(0)
    else:
        print(1)


