def solution(s): 
    stk = 0
    for s in list(s):
        if s == '(' :  # 열린 괄호이면
            stk+=1 
        else : # 닫힌 괄호이면
            stk-=1 
        if stk < 0 :
            return False
    if stk != 0 :
        return False
    else :
        return True
