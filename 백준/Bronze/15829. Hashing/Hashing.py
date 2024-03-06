import sys
p = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
sum = 0
num = 0
for i in s:
    sum = sum + (ord(i)-96) * 31**(num)
    num = num + 1
print(sum)