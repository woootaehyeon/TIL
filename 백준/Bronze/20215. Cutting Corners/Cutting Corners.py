import sys
n, m = map(int,sys.stdin.readline().split())
long = n + m
short = ((n**2 + m**2)**0.5)
print(long - short)