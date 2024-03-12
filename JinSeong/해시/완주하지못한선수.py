# LEVEL 1
def solution(participant, completion):
    sorted_participant = sorted(participant)
    sorted_completion = sorted(completion)
    for i in range(len(participant)) :
        if i == len(participant) - 1 :
            answer = sorted_participant[i]
        elif sorted_participant[i] != sorted_completion[i] :
            answer = sorted_participant[i]
            break
    return answer
