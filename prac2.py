import sys
from collections import deque
d = deque()
n, m = map(int,input().split())
for i in range(1,n+1):
    d.append(i)
print(d)
check = deque(map(int,input().split()))
cnt = 0

print(d.index(5))