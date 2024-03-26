import sys
n, m = sys.stdin.readline().split()
helmet = list(map(int,sys.stdin.readline().split()))
vest = list(map(int,sys.stdin.readline().split()))
print(max(helmet) + max(vest))