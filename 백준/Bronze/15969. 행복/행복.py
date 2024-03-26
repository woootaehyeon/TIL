import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int,sys.stdin.readline().split()))
print(max(arr) - min(arr))