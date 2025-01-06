import math
import sys

N = int(sys.stdin.readline())
size = list(map(int,sys.stdin.readline().split()))
T, P = map(int,sys.stdin.readline().split())

bundle_T = 0

for t in size:
    bundle_T += math.ceil(t/T)

# print(bundle_T)

bundle_P = N // P

print(bundle_T)
print(bundle_P, end = " ")
print(N - bundle_P * P)