import sys
input = sys.stdin.readline
d = []

n = int(input())
for i in range(n):
    d.append(int(input()))

dic = dict()

for i in d: 
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

print(dic)

mx = max(dic.values())
mx_dic = [] 

for i in dic:
    if mx == dic[i]: 
        mx_dic.append(i)

print(mx_dic)