import sys
import math

n = int(sys.stdin.readline().rstrip())
stack = []

for i in range(n):
    num = sys.stdin.readline().split()
    if int(num[0]) == 1:
        stack.append(int(num[1]))
    elif int(num[0]) == 2:
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif int(num[0]) == 3:
        print(len(stack))
    elif int(num[0]) == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif int(num[0]) == 5:
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)