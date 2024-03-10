def solution(nums):
    from collections import Counter
    n = dict(Counter(nums))
    if len(n.keys()) >= len(nums)/2 :
        answer =  len(nums)/2
    else :
        final = []
        nn = dict(sorted(n.items(), key = lambda item: item[1], reverse = True))
        nn = dict(map(lambda item: (item[0], item[1] - 1), n.items()))
        final=final+list(nn.keys())
        for i in range(int(len(nums)/2)-len(final)):
            nm= {key: value for key, value in nn.items() if value > 0} # 값 없는 것들 탈락
            nm = dict(sorted(nm.items(), key = lambda item: item[1], reverse = True)) # 내림차순
            final.append(list(nm.keys())[0])
            nm[list(nm.keys())[0]] = nm[list(nm.keys())[0]]-1
        answer = len(set(final))
    return answer
