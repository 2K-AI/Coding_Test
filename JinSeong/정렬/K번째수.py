# Level1
def quick(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array)//2]
    small, equal, big = [], [], []
    
    for num in array:
        if num < pivot :
            small.append(num)
        elif num > pivot:
            big.append(num)
        else:
            equal.append(num)
    return quick(small)+equal+quick(big)

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        new_array = array[commands[i][0]-1:commands[i][1]]
        new_array = quick(new_array)
        print(new_array)
        answer.append(new_array[commands[i][2]-1])
    return answer
