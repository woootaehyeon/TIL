import sys
from collections import deque
d = deque()
n, m = map(int,input().split())

for i in range(1,n+1): # 덱 생성
    d.append(i) 

check = deque(map(int,input().split()))
cnt = 0
while len(check) > 0:
    # 뽑으려는 카드가 맨 위에 있는 경우
    # 카드 뽑기
    if d[0] == check[0]:
        d.popleft()
        check.popleft()
    # 뽑으려는 카드가 현재 덱의 중간보다 앞에 있는 경우
    # 왼쪽으로 회전
    elif d.index(check[0]) < (len(d) / 2):
            d.append(d.popleft())
            cnt += 1
    # 뽑으려는 카드의 위치가 현재 덱의 중간보다 뒤에 있는 경우 
    # 오른쪽으로 회전
    else:
         d.appendleft(d.pop())
         cnt += 1

print(cnt)
        
# d.popleft() # 1
# d.append(d.popleft()) # 2
# d.appendleft(d.pop()) # 3
