import sys

n,m = map(int,sys.stdin.readline().split())
arr = set()
d = []

for i in range(n):
    arr.add(sys.stdin.readline().rstrip())

for j in range(m):
    s = sys.stdin.readline().rstrip()
    if s in arr:
        d.append(s)

print(len(d))
for k in sorted(d):
    print((k))