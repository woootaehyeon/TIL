import sys
n = int(sys.stdin.readline())
arr = [0] * 10001
for i in range(n):
    arr[int(sys.stdin.readline())-1] += 1

for j in range(10001):
    for k in range(arr[j]):
        print(j+1)