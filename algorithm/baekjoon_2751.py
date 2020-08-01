## https://www.acmicpc.net/problem/2751
import sys


array_size = int(sys.stdin.readline())

array = []

for i in range(array_size):
    array.append(int(sys.stdin.readline()))

for i in sorted(array):
    print(i)