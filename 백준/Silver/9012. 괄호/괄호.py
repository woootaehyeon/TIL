t = int(input())
for i in range(t):
    stack = []
    s = input()
    isTF = True

    for j in s:
        if j == '(':
            stack.append('(')
        if j == ')':
            if stack:
                stack.pop()
            elif not stack:
                isTF = False
                break
    if not stack and isTF:
        print('YES')
    elif stack or not isTF:
        print('NO')