import sys

n = int(sys.stdin.readline())
d = [0,1,2,4,0,0,0,0,0,0,0]
for i in range(4,11):
  d[i] = d[i-1] + d[i-2] + d[i-3]
  
for j in range(n):
  num = int(sys.stdin.readline())
  print(d[num])