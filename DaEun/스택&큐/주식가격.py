def solution(prices):
    answer = []
    for idx in range(len(prices)):
        value = len(prices) - idx -1 
        for limit in range(idx+1, len(prices)): 
            if prices[idx]> prices[limit]:
                value = limit - idx
                break
        answer.append(value)
    return answer
