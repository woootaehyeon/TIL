import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

cnt = [0,0,0,0,0,0,0,0,0,0]

num = str(a*b*c)

for i in range(len(num)):
    cnt[int(num[i])] = cnt[int(num[i])] + 1
for j in cnt:
    print(j)