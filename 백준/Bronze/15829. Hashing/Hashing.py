import math
import sys

r = 31
m = 1234567891

n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()
hash = 0

for i in range(len(s)):
    # print(ord(i) - 96)
    hash += (ord(s[i]) - 96) * r**i

print(hash % m)
