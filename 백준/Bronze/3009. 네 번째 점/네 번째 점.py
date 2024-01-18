import sys
arr = []
arr2 = []

for i in range(3):
    a,b = map(int,input().split())
    arr.append(a)
    arr2.append(b)
    
for i in range(3):
    if (arr.count(arr[i])) == 1:
        x = arr[i]
    if (arr2.count(arr2[i]) == 1):
        y = arr2[i]

print(f"{x} {y}")