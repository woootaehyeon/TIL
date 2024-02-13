import sys
arr = list(map(int,sys.stdin.readline().split()))
str = ""
for i in arr:
    if i == 1:
        str = str + 'c'
    elif i == 2:
        str = str + 'd'
    elif i == 3:
        str = str + 'e'
    elif i == 4:
        str = str + 'f'
    elif i == 5:
        str = str + 'g'
    elif i == 6:
        str = str + 'a'
    elif i == 7:
        str = str + 'b'
    elif i == 8:
        str = str + 'C'

if str == "cdefgabC":
    print("ascending")
elif str == "Cbagfedc":
    print("descending")
else:
    print("mixed")