import sys
input = sys.stdin.readline
n, m = map(int,input().split())
d = []
for i in range(n):
    d.append(list(map(int,input().split())))

k = int(input())
for j in range(k):
    sum = 0
    i, j, x, y = map(int,input().split())
    for o in range(i-1,x):
        for p in range(j-1,y):
            sum = sum + d[o][p]
    print(sum)    

