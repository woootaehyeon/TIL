while True:
    arr = list(map(int, input().split()))
    if sum(arr) == 0:
        break
    else:
        arr.sort()  # 입력된 숫자들을 오름차순으로 정렬
        if arr[0]**2 + arr[1]**2 == arr[2]**2:
            print("right")
        else:
            print("wrong")
