import sys
n = sys.stdin.readline().rstrip()
arr = []
for i in n:
    arr.append(int(i))
arr.sort(reverse=True)
for j in arr:
    print(j,end="")