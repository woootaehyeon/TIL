import sys
input = sys.stdin.readline
money = []
n,total= map(int,input().split())

for i in range(n):
    money.append(int(input()))

money.reverse()

cnt = 0
for j in money:
    cnt = cnt + (total // j)
    total = total % j
    
print(cnt)
        

    
