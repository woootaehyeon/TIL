heights = sorted([int(input()) for _ in range(9)])
sum_heights = sum(heights)

for i in range(8):
    for j in range(i + 1, 9):
        if sum_heights - (heights[i] + heights[j]) == 100:
            x1, x2 = heights[i], heights[j]

heights.remove(x1)
heights.remove(x2)

[print(h) for h in heights]