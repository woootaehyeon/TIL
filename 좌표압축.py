import sys

input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline을 input으로 사용

n = int(input())            # 입력: 숫자 배열의 길이를 사용자로부터 입력받음
arr = list(map(int, input().split()))  # 입력: 공백을 기준으로 숫자들을 입력받고, 이를 정수형 리스트로 저장

arr2 = sorted(list(set(arr)))  # 중복을 제거한 원소를 정렬하여 arr2 리스트에 저장
print(arr2)
dic = {arr2[i] : i for i in range(len(arr2))}  # arr2의 값을 key로, 해당 원소의 인덱스를 value로 갖는 딕셔너리 생성
print(dic)

for i in arr:
    print(dic[i], end=' ')    # 입력된 숫자 배열의 각 원소에 대해 딕셔너리 dic를 이용하여 대응되는 인덱스를 찾아서 출력


