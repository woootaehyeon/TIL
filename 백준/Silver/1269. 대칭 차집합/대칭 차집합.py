import sys

n, m = map(int,sys.stdin.readline().split())
SA = set(map(int,sys.stdin.readline().split()))
SB = set(map(int,sys.stdin.readline().split()))
cnt = len(SA) + len(SB)

for i in SB:
    if i in SA:
        cnt -= 1

for j in SA:
    if j in SB:
        cnt -= 1
    
print(cnt)