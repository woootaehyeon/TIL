import sys
from collections import deque

a, b = map(int,sys.stdin.readline().split())
arr = deque()
result = []


for i in range(1, a+1):
    arr.append(i)


while(arr):
    for j in range(b-1):
        arr.append(arr.popleft())
    result.append(arr.popleft())

print('<',end='')
for i in range(len(result)-1):
    print(result[i],end=', ')
print(result[-1],end='>')