# LEVEL 2
def solution(progresses, speeds):
    answer = []
    result = []
    import math
    for i in range(len(progresses)) :
        result.append(math.ceil((100-progresses[i])/speeds[i]))
    pivot = 0
    num = 0
    for i in range(len(result)):
        if i == 0 :
            answer.append(1)
        elif result[pivot] < result[i]:
            answer.append(1)
            num += 1
            pivot = i
        else :
            answer[num] += 1
    return answer
