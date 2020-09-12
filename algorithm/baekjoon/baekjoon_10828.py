# https://www.acmicpc.net/problem/10828
import sys


stack_len = int(sys.stdin.readline())
stack = list()

for i in range(stack_len):
    message = sys.stdin.readline().split()
    length = len(stack)
    if message[0] == "push":
        stack.append(int(message[1]))
    elif message[0] == "size":
        print(length)
    elif message[0] == "pop":
        if length == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif message[0] == "empty":
        if length == 0:
            print(1)
        else:
            print(0)
    elif message[0] == "top":
        if length == 0:
            print(-1)
        else:
            print(stack[-1])

