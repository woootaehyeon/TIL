import sys
n = int(sys.stdin.readline().rstrip())
arr = []
for i in range(n):
    a,b = sys.stdin.readline().split()
    arr.append((int(a),b))
arr.sort(key=lambda x:x[0])
for i in arr:
    print(i[0], i[1])