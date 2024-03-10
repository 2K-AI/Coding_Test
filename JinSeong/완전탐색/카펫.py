# LEVEL 2
def solution(brown, yellow):
    answer = []
    sum = brown+yellow
    for i in range(1, sum+1) :
        if sum % i : continue
        j = sum//i
        if i + j == brown//2 + 2 :
            answer.append(j)
            answer.append(i)
            break
    return answer
