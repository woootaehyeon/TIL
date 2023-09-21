while True:
    stack = []
    s = input()
    isVPS = True

    if s == '.':
        break

    for j in s:

        if j == '(':
            stack.append('(')
        elif j == ')':
            if len(stack) > 0 and stack[len(stack) - 1] == '(':
                stack.pop()
            else:
                isVPS = False
                break
            
        elif j == '[':
            stack.append('[')
        elif j == ']':
            if len(stack) > 0 and stack[len(stack) - 1] == '[':
                stack.pop()
            else:
                isVPS = False
                break
            
    if len(stack) == 0 and isVPS == True:
        print('yes')
    else:
        print('no')