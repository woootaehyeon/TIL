import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    num = sys.stdin.readline().split()
    if num[0] == '0':
        if len(arr) == 0:
            print(-1)
        else:
            print(max(arr))
            arr.remove(max(arr))
    else:
        for i in range(1,int(num[0])+1):
            arr.append(int(num[i]))
