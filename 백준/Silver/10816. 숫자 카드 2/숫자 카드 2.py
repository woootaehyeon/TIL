import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

d = {}

for i in range(n):
    if arr[i] in d:
        d[arr[i]] += 1
    else:
        d[arr[i]] = 1

for j in range(m):
    print(d.get(arr2[j], 0), end=' ') # d.get(), 기본 반환값 -> 밸류값 없으면 기본 반환값 출력 (예외처리)