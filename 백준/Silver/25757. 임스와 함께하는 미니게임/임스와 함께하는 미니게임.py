import sys

n, m = sys.stdin.readline().split()
n = int(n)
d = set()

for i in range(n):
    d.add(sys.stdin.readline().rstrip())

if m == 'Y':
    num = 2
elif m == 'F':
    num = 3
else:
    num = 4

total = len(d)
cnt = 0

while total >= num - 1:
    cnt = cnt + 1
    total = total - (num - 1)
    
print(cnt)
    