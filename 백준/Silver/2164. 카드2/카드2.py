import sys
from collections import deque

n = int(sys.stdin.readline())
card = deque()

for i in range(n):
    card.append(i+1)
card.reverse()

while len(card) != 1:
    card.pop()
    card.appendleft(card[-1])
    card.pop()

print(card[0])