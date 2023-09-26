s = input().split('-')

num = []

for i in s:
    sum = 0
    temp = i.split('+')
    for j in temp:
        sum = sum + int(j)
    num.append(sum)

total = num[0]
num.remove(num[0])

for k in num:
    total = total - k
print(total)