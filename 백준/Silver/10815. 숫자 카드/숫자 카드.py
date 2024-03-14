import sys
n = int(sys.stdin.readline().rstrip())
arr = set(map(int,sys.stdin.readline().split()))

k = int(sys.stdin.readline().rstrip())
arr2 = list(map(int,sys.stdin.readline().split()))

for i in arr2:
    if i in arr:
        print(1,end=' ')
    else:
        print(0,end=' ')

