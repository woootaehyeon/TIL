import sys

N, M = map(int,sys.stdin.readline().split())
arr = set()
cnt = 0

for i in range(N):
    arr.add(sys.stdin.readline().rstrip())
    
for j in range(M):
    if sys.stdin.readline().rstrip() in arr:
        cnt += 1

print(cnt)

