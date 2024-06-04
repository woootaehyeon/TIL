import sys
n = int(sys.stdin.readline())
for i in range(n):
  N = int(sys.stdin.readline())
  book1 = set(map(int,sys.stdin.readline().split()))
  
  M = int(sys.stdin.readline())
  book2 = list(map(int,sys.stdin.readline().split()))
  
  for j in book2:
    if j in book1:
      print(1)
    else:
      print(0)