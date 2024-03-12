import sys
n = int(sys.stdin.readline().rstrip())
arr = []
for i in range(n):
    arr.append(sys.stdin.readline().rstrip())
arr = set(arr)
arr = list(arr)
arr.sort()
arr.sort(key=len)
for j in arr:
    print(j)