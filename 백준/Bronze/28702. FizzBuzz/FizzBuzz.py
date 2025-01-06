import math
import sys

arr = []

for _ in range(3):
    i = sys.stdin.readline().strip()
    arr.append(i)

for num in arr:
    if num.isdigit():
        next_num = int(num) + (len(arr) - arr.index(num))

if next_num % 15 == 0:
    print("FizzBuzz")
elif next_num % 3 == 0 and next_num % 5 != 0:
    print("Fizz")
elif next_num % 3 != 0 and next_num % 5 == 0:
    print("Buzz")
else:
    print(next_num)