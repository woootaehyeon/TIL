from collections import deque
d = deque()
for i in range(10):
    d.append(i)
print(d) # deque([0,1,2,3,4,5,6,7,8,9])

d.appendleft(10)
print(d) # deque([10,0,1,2,3,4,5,6,7,8,9])

d.extend([99,99,99])
print(d) # deque([10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 99, 99])

d.pop()
print(d) # deque([10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 99])

d.popleft()
print(d) # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 99])
