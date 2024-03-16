def solution(priorities, location):
    idx = 0 
    order = []
    while idx>= 0  : 
        i = idx % len(priorities)
        if max(priorities) == priorities[i] :  # out조건
            order.append(i)
            priorities[i] = 0

        if sum(priorities)==0 :
            break

        idx+=1 
    return order.index(location)+1
