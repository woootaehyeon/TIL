import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
total = 0
if 1 in arr:
    arr.remove(1)

for i in arr:
    cnt = 0
    for j in range(1,i+1):
        if i % j == 0:
            cnt = cnt + 1
    if cnt == 2:
        total += 1

print(total)
        
