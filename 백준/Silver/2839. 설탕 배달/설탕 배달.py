import sys
p = int(sys.stdin.readline())
cnt = 0
while p >= 0:
    if p % 5 == 0:
        cnt = cnt + (p // 5)
        print(cnt)
        break
    p = p - 3
    cnt = cnt + 1
else:
    print(-1)
        