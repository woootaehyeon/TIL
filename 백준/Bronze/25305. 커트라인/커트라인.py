import sys
a,b = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
arr.reverse()
print(arr[b-1])