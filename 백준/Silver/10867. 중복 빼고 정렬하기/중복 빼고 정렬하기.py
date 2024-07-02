import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int,sys.stdin.readline().split()))
arr = set(arr)
arr = list(arr)
for i in sorted(arr):
    print(i, end = ' ')