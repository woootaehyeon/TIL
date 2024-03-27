import sys
import math

a,b = map(int,sys.stdin.readline().split())
c,d = map(int,sys.stdin.readline().split())

boonmo = math.lcm(b,d)
boonja = int((boonmo/b * a) + (boonmo/d * c))

print(int(boonja / math.gcd(boonmo,boonja)),end = ' ')
print(int(boonmo / math.gcd(boonmo,boonja)))