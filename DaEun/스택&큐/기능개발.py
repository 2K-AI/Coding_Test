def solution(progresses, speeds):
    import math
    days = []
    through = []
    answer = []
    
    for idx in range(len(progresses)):
        days.append(math.ceil((100-progresses[idx])/speeds[idx]))

    for i in range(len(days)):
        cnt = 1
        if i in through :
            continue
        for j in range(i+1, len(days)):
            if i<j and days[i]>=days[j] :
                cnt+=1 
                through.append(j)
            else :
                break
        answer.append(cnt)
    return answer
