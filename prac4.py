import random
import time

# 버블 정렬 구현
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# 퀵 정렬 구현
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 병합 정렬 구현
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result

# 성능 테스트
if __name__ == "__main__":
    array_size = 1000
    random_array = [random.randint(0, 10000) for _ in range(array_size)]

    # 버블 정렬 성능 측정
    bubble_array = random_array.copy()
    bubble_start_time = time.time()
    bubble_sort(bubble_array)
    bubble_end_time = time.time()
    bubble_time = bubble_end_time - bubble_start_time

    # 퀵 정렬 성능 측정
    quick_array = random_array.copy()
    quick_start_time = time.time()
    quick_sort(quick_array)
    quick_end_time = time.time()
    quick_time = quick_end_time - quick_start_time

    # 병합 정렬 성능 측정
    merge_array = random_array.copy()
    merge_start_time = time.time()
    merge_sort(merge_array)
    merge_end_time = time.time()
    merge_time = merge_end_time - merge_start_time

    print("배열 크기:", array_size)
    print("버블 정렬 시간:", bubble_time)
    print("퀵 정렬 시간:", quick_time)
    print("병합 정렬 시간:", merge_time)
