import sys
input = sys.stdin.readline

N = int(input())
cards = [*map(int, input().split())]
M = int(input())
card2 = [*map(int, input().split())]

count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for j in range(len(card2)):
    if card2[j] in count:
        print(count[card2[j]], end = ' ')
    else:
        print(0, end = ' ')