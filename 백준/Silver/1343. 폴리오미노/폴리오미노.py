import sys
card = sys.stdin.readline().rstrip()
card = card.replace("XXXX","AAAA")
card = card.replace("XX","BB")
if 'X' in card:
    print(-1)
else:
    print(card)