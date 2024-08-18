def solution(board, moves):
    cnt = 0
    basket = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                if basket and basket[-1] == board[j][i-1]:
                    basket.pop()
                    board[j][i-1] = 0
                    cnt += 2
                    break
                else:
                    basket.append(board[j][i-1])
                    board[j][i-1] = 0
                    break

    answer = cnt
    return answer