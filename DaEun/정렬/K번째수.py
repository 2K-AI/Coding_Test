def solution(array, commands):
    answer = []
    for com in commands : #[2, 5, 3]
        temp = array[com[0]-1 : com[1]].copy()
        temp.sort()
        answer.append(temp[com[2]-1])
    return answer
