import sys

def fido(n):
    if n == 1 or n == 2:
        ans = 1
    elif n == 0:
        ans = 0
    else:
        ans = fido(n-1) + fido(n-2)
    
    return ans

print(fido(int(sys.stdin.readline())))