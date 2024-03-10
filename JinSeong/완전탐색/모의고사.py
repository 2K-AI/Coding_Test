# LEVEL 1
def solution(answers):
    n = len(answers)
    temp1 = [2, 1, 2, 3, 2, 4, 2, 5]
    temp2 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    s1, s2, s3 = [], [], []
    for i in range(n):
        s1.append(i%5+1)
    for _ in range(n//8):
        s2 = s2+ temp1
    for i in range(n%8):
        s2.append(temp1[i])
    for _ in range(n//10):
        s3 = s3 + temp2
    for i in range(n%10):
        s3.append(temp2[i])
    num1, num2, num3 = 0, 0, 0
    for i in range(n):
        if s1[i] == answers[i]:
            num1 += 1
        if s2[i] == answers[i]:
            num2 += 1
        if s3[i] == answers[i]:
            num3 += 1
    answer = []
    max = 0
    for i in [num1, num2, num3]:
        if i > max :
            max = i
    if max == num1 :
        answer.append(1)
    if max == num2 :
        answer.append(2)
    if max == num3 :
        answer.append(3)
    return answer
