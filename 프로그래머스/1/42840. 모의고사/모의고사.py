def solution(answers):
    answer = []
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    
    total = [0,0,0]
    
    for i in range(len(answers)):
        if s1[i % len(s1)] == answers[i]:
            total[0] += 1
        if s2[i % len(s2)] == answers[i]:
            total[1] += 1
        if s3[i % len(s3)] == answers[i]:
            total[2] += 1
    print(total)
    
    max_num = max(total)
    
    for i in range(len(total)):
        if total[i] >= max_num:
            answer.append(i + 1)
            
    return answer