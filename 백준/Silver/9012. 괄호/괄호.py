import sys
n = int(sys.stdin.readline())
for i in range(n):
    stack = []
    s = sys.stdin.readline().rstrip()
    TF = True

    for j in s:
        if j == '(':
            stack.append('(')
        if j == ')':
            if stack:
                stack.pop()
            elif not stack:
                TF = False
                break
    if not stack and TF == True:
        print('YES')
    elif stack or TF == False:
        print('NO')