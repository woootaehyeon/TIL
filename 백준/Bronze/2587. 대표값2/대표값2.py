import sys
arr = []
for i in range(5):
    arr.append(int(sys.stdin.readline()))
arr.sort()
print(int(sum(arr)/5))
print(arr[2])