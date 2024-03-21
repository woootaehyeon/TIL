import sys
import math

while True:
    s = list(sys.stdin.readline().rstrip())
    if len(s) == 1 and s[0] == '#':
        break
    else:
        s.reverse()
        sum = 0
        cnt = 0
        for i in range(len(s)):
            if s[i] == '-':
                sum = sum + 0
            elif s[i] == '\\':
                sum = sum + 1 * (8 ** cnt)
            elif s[i] == '(':
                sum = sum + 2 * (8 ** cnt)
            elif s[i] == '@':
                sum = sum + 3 * (8 ** cnt)
            elif s[i] == '?':
                sum = sum + 4 * (8 ** cnt)
            elif s[i] == '>':
                sum = sum + 5 * (8 ** cnt)
            elif s[i] == '&':
                sum = sum + 6 * (8 ** cnt)
            elif s[i] == '%':
                sum = sum + 7 * (8 ** cnt)
            elif s[i] == '/':
                sum = sum + -1 * (8 ** cnt)
            cnt += 1

        print(sum)