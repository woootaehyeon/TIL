import sys
import math

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

a, b = map(int, sys.stdin.readline().split())

for i in range(a, b+1):
    if is_prime(i):
        print(i)