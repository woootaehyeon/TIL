def solution(dirs):
    arr = []
    x = 5
    y = 5

    def is_valid_move(x, y):
        return 0 <= x < 11 and 0 <= y < 11

    for i in dirs:
        if i == 'U':
            if is_valid_move(x, y+1):
                arr.append((x,y+1,x,y))
                arr.append((x,y,x,y+1))
                y += 1
        elif i == 'D':
            if is_valid_move(x, y-1):
                arr.append((x,y-1,x,y))
                arr.append((x,y,x,y-1))
                y -= 1
        elif i == 'R':
            if is_valid_move(x+1, y):
                arr.append((x+1,y,x,y))
                arr.append((x,y,x+1,y))
                x += 1
        elif i == 'L':
            if is_valid_move(x-1, y):
                arr.append((x-1,y,x,y))
                arr.append((x,y,x-1,y))
                x -= 1
    arr = set(arr)
    return(len(arr) / 2)