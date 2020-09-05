# https://www.acmicpc.net/problem/10816
import sys


def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if array[mid] == target:
        return array[start:end+1].count(target)
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

a.sort()
x_dict = {}
for chk in x:
    if chk in x_dict:
        print(x_dict[chk])
    else:
        x_dict[chk] = binary_search(a, chk, 0, n-1)
        print(x_dict[chk])
