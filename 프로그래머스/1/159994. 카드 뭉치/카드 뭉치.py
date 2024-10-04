from collections import deque
def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    answer = "Yes"

    for i in range(len(goal)):
        if cards1 and goal[0] == cards1[0]:
            goal.popleft()
            cards1.popleft()
        elif cards2 and goal[0] == cards2[0]:
            goal.popleft()
            cards2.popleft()
        else:
            answer = "No"
    return answer