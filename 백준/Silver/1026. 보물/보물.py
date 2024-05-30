import sys
n = int(sys.stdin.readline())
d = list(map(int,sys.stdin.readline().split()))
d2 = list(map(int,sys.stdin.readline().split()))
d.sort()
d2.sort(reverse=True)
cnt = 0
for i in range(n):
  cnt = cnt + (d[i] * d2[i])
print(cnt)