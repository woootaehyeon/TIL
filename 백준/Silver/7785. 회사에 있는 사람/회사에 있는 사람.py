import sys

arr = set()
n = int(sys.stdin.readline())

for i in range(n):
    name, state = map(str, sys.stdin.readline().split())
    if state == "enter":
        arr.add(name)
    elif state == "leave":
        arr.remove(name)
    else:
        continue
    
arr2 = list(arr)
arr2.sort(reverse=True)
for j in arr2:
    print(j)
    