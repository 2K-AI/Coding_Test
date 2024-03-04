def solution(sizes):
    sort_sizes = []
    for tup in sizes:
        if tup[1]> tup[0]:
            temp = [tup[1], tup[0]]
            sort_sizes.append(temp)
        else :
            sort_sizes.append(tup)
    w_max = max([tup[0] for tup in sort_sizes])
    h_max = max([tup[1] for tup in sort_sizes])
    
    answer = w_max * h_max
    return answer
