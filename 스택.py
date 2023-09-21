import sys
from collections import deque

n = int(input())
queue = deque()

for i in range(n):
    input = sys.stdin.readline().split()
    if input[0] == 'push':
        queue.append(int(input[1]))

    elif input[0] == 'pop':
        if queue:
            print(queue.popleft())
        else: print(-1)

    elif input[0] == 'size':
        print(len(queue))

    elif input[0] == 'empty':
        if queue: print(0)
        else: print(1)