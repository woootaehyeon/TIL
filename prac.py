def gcd(a,b):
    while b>0:
        a,b = b, a%b
    return a

x1, y1 = map(int,input().split())
x2, y2 = map(int,input().split())
x3, y3 = map(int,input().split())

if x1 == x2 == x3:
    print("WHERE IS MY CHICKEN?")
elif y1 == y2 == y3:
    print("WHERE IS MY CHICKEN?")
elif x1 / gcd(x1,y1) == x2 / gcd(x2,y2) == x3 / gcd(x3,y3) and y1 / gcd(x1,y1) == y2 / gcd(x2,y2) == y3 / gcd(x3,y3):
    print("WHERE IS MY CHICKEN?")
else:
    print("WINNER WINNER CHICKEN DINNER!")