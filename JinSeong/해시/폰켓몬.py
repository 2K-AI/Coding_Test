# LEVEL 1
def solution(nums):
    dict = {}
    N = len(nums)
    for i in range(len(nums)) :
        try:
            dict[nums[i]] = dict[nums[i]] + 1            
        except:
            dict[nums[i]] = 1
    if len(dict) > N /2 :
        answer = N/2
    else :
        answer = len(dict)
    return answer
