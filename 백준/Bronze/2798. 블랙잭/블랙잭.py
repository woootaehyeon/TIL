import sys
n, max = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
blackjack = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            sum = arr[i] + arr[j] + arr[k]
            if sum <= max and sum > blackjack:
                blackjack = sum
print(blackjack)