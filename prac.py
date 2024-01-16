import sys
while True:
    a = int(sys.stdin.readline().rstrip())
    if a == -1:
        break
    else:
        arr = []
        for i in range(1,a):
            if a % i == 0:
                arr.append(i)
                
        if sum(arr) == a:
            print(f"{a} = ", end='')
            for i in range(len(arr) - 1):
                print(f"{arr[i]} + ", end='')
            print(arr[-1])
        else:
            print(f"{a} is NOT perfect.")