import sys
p = int(sys.stdin.readline())
cnt = 0
num = 1
while True:
    if p == cnt:
        print(num)
        break
    else:
        num += 1
        if "666" in str(num):
            cnt += 1
        else:
            continue
    