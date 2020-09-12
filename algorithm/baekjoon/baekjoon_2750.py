## https://www.acmicpc.net/problem/2750


array_size = int(input())

array = []

for i in range(array_size):
    array.append(int(input()))

for k in range(0, array_size):
    for j in range(k+1, array_size):
        empty = array[k]
        if array[k] > array[j]:
            array[k] = array[j]
            array[j] = empty

for last in array:
    print(last)