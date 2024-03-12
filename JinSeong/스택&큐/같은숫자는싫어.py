# LEVEL 1
def solution(arr):
    answer = []
    i = 0
    arr.append(10)
    while i < len(arr) - 1:
        if arr[i] != arr[i+1] :
            answer.append(arr[i])
        i += 1
    return answer
