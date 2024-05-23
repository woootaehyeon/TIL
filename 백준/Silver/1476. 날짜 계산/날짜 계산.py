import sys

e,s,m = map(int,sys.stdin.readline().split())
cnt = 0
year = [0,0,0]

while True:
  cnt += 1
  year[0] = year[0] + 1
  year[1] = year[1] + 1
  year[2] = year[2] + 1
  if year[0] == 16:
    year[0] = 1
  if year[1] == 29:
    year[1] = 1
  if year[2] == 20:
    year[2] = 1
  if year[0] == e and year[1] == s and year[2] == m:
    print(cnt)
    break