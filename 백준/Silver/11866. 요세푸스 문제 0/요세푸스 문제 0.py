import sys
n, k = map(int,sys.stdin.readline().split())
stack = []
d = []
for i in range(1,n+1):
    d.append(i)

cnt = k - 1
while True:
    stack.append(d[cnt])
    d.remove(d[cnt])

    if not len(d):
        break

    cnt = cnt + (k - 1)
    if cnt >= len(d):
        cnt = cnt % len(d)

print('<', end='')
for i in range(n):
    if i == n-1:
        print(stack[i], end=">")
    else:
        print(stack[i], end=', ')