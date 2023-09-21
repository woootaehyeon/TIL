import sys

d = []
n, m = 3, 3

for i in range(n):
    d.append([])
    for j in range(m):
        d[i].append(0)

for i in range(n):
    d[i] = list(map(int, sys.stdin.readline().strip().split()))  # 입력받은 값을 정수로 변환하여 리스트에 저장

for i in range(n):
    for j in range(m):
        print(d[i][j],end=' ')
    print()