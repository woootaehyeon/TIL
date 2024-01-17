import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
arr = []

for i in range (a, b+1):
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt = cnt + 1
    if cnt == 2:
        arr.append(i)

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))