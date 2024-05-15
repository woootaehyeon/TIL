import sys
from collections import deque

d = deque()
n = int(sys.stdin.readline())

for i in range(n):
    num = (sys.stdin.readline().split())
    if int(num[0]) == 1:
        d.appendleft(num[1])
    elif int(num[0]) == 2:
        d.append(num[1])
    elif int(num[0]) == 3:
        if d:
            print(d[0])
            d.popleft()
        else:
            print(-1)
    elif int(num[0]) == 4:
        if d:
            print(d[-1])
            d.pop()
        else:
            print(-1)
    elif int(num[0]) == 5:
        print(len(d))
    elif int(num[0])== 6:
        if d:
            print(0)
        else:
            print(1)
    elif int(num[0]) == 7:
        if d:
            print(d[0])
        else:
            print(-1)
    elif int(num[0]) == 8:
        if d:
            print(d[-1])
        else:
            print(-1)
