def solution(participant, completion):
    from collections import Counter
    p = Counter(participant)
    c = Counter(completion)
    answer = list((p-c).elements())[0]
    return answer
