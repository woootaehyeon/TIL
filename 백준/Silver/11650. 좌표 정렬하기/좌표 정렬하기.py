import sys
n = int(sys.stdin.readline().rstrip())
arr = []
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    arr.append((a,b))
arr.sort()
for j in arr:
    print(j[0], j[1])