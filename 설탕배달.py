sugar = int(input())
cnt = 0
while sugar >= 0:
    if sugar % 5 == 0:
        cnt = cnt + (sugar // 5)
        print(cnt)
        break
    sugar = sugar - 3
    cnt = cnt + 1
else:
    print(-1)