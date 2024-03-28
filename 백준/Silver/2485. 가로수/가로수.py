import sys
import math

n = int(sys.stdin.readline().rstrip())
cnt = 0
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
sub = []

for i in range(len(arr) -1):
    sub.append(arr[i+1] - arr[i])

g = sub[0]
for j in range(1, len(sub)):
    g = math.gcd(g, sub[j])
    
cnt = 0
for j in sub:
    cnt += j // g - 1

print(cnt)