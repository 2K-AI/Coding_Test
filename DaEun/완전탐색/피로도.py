def solution(k, dungeons):
    import itertools
    result = 0 
    lnpr = list(itertools.permutations(dungeons, len(dungeons)))
    for pp in list(lnpr) : # 각각의 경우의 수 불러오기 -> ([80, 20], [50, 40], [30, 10])
        rst = 0 
        power = k 
        for p in pp : # 각각의 던전 참여 가능 확인 -> [80, 20]
            if power >=p[0]  : # 최소 필요 필도도 pass 
                rst +=1
                power -= p[1]
            else : 
                break
        result = max(result, rst)
    return result
