import sys

n, m = map(int,sys.stdin.readline().split())
arr = [[0 for _ in range(m*2)] for _ in range(n*2)]

for i in range(n):
    s = list(sys.stdin.readline().rstrip())
    for j in range(len(s)):
        arr[i][j] = s[j]
    s.reverse()
    cnt = 0
    for k in range(m, m*2):
        arr[i][k] = s[cnt]
        cnt += 1
        
cnt2 = n - 1
for i in range(n, n*2):
    for j in range(m*2):
        arr[i][j] = arr[cnt2][j]
    cnt2 = cnt2 - 1

A,B = map(int,sys.stdin.readline().split())

if arr[A-1][B-1] == '#':
    arr[A-1][B-1] = '.'
else:
    arr[A-1][B-1] = '#'
    
for i in range(n*2):
    for j in range(m*2):
        print(arr[i][j],end='')
    print()