import sys
n = int(sys.stdin.readline())
d = list(map(int,sys.stdin.readline().split()))
total = []
d.sort()
cnt = 0
for i in d:
  cnt += i
  total.append(cnt)
print(sum(total))