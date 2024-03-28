n = int(input())
d = list(map(int,input().split()))

stack = []
goal = []
rank = 1

while True:
    if len(d) == 0:
        break

    if d[0] != rank:
        if len(stack) > 0 and stack[-1] == rank:
            goal.append(stack[-1])
            stack.remove(stack[-1])
            rank += 1
        else:
            stack.append(d[0])
            d.remove(d[0])
    else:
        goal.append(d[0])
        d.remove(d[0])
        rank += 1

for j in range(len(stack)):
    goal.append(stack.pop())

sorted_goal = sorted(goal)

if goal == sorted_goal:
    print("Nice")
else:
    print("Sad")
