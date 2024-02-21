import sys

a,b,c,d,e = map(int,sys.stdin.readline().split())
sum = a**2 + b**2 + c**2 + d**2 + e**2
print(sum % 10)