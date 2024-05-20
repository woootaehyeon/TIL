import sys,math
n = int(sys.stdin.readline())
d = list(map(int,sys.stdin.readline().split()))
print(max(d) * min(d))