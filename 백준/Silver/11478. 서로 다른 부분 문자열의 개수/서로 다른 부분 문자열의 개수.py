import sys

s = sys.stdin.readline().rstrip()
S = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        S.add(s[i:j+1])
        
print(len(S))