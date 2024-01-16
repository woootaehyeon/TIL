import sys
a, b = map(int,sys.stdin.readline().rsplit())
arr = []
for i in range(1,a+1):
    if a % i == 0:
        arr.append(i)
if len(arr) < b:
    print(0)
else:
    print(arr[b-1])