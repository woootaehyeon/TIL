import sys

s = list(map(str, sys.stdin.readline().strip()))

res = ""
word = ""
reverse = True

for i in s:

    if i == '<':
        reverse = False
        res += word
        word = i

    elif i == '>':
        reverse = True
        res += (word + '>')
        word = ""

    elif i == ' ':
        res += word + i
        word = ""

    elif reverse:
        word = i + word

    else:
        word += i

res += word
print(res)