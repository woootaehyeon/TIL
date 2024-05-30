import sys
n = int(sys.stdin.readline())
d = set()
cnt = 0
for i in range(n):
  s = sys.stdin.readline().strip()
  if s == "ENTER":
    d = set()
  else:
    if s not in d:
      d.add(s)
      cnt = cnt + 1
print(cnt)