import sys
n = int(sys.stdin.readline())
dot = []

for i in range(n) :
    [a,b] = map(int, sys.stdin.readline().split())
    dot.append([a,b])

dot.sort(key = lambda x : (x[1],x[0]))

for i in range(n) :
    print(dot[i][0],dot[i][1])