import sys
x, y = sys.stdin.readline().split()
sum = int(x[::-1]) + int(y[::-1])
print(int(str(sum)[::-1]))