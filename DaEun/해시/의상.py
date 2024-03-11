def solution(clothes):
    from collections import Counter

    second_values = [item[1] for item in clothes] # 종류
    nn = list((Counter(second_values)).values())
    
    def div(nn):
        if len(nn) ==2 :
            return nn[0]* nn[1]+nn[0]+nn[1]
        elif len(nn) ==1 :
            return nn[0]
        else  :
            line = len(nn)//2
            first = div(nn[:line])
            second = div(nn[line:])
            return div([first, second])

        
    return div(nn)
