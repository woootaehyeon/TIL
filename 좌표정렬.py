import sys
input = sys.stdin.readline

n = int(input())

d = []

for _ in range(n):
    a,b = input().split()
    d.append([int(a), int(b)])

d.sort(key = lambda x: (x[0],x[1]))


for a, b in d:
    print(a, b)