def solution(numbers):
    from functools import cmp_to_key
    def compare(a, b):
        if str(a) + str(b) > str(b) + str(a):
            return -1
        elif str(a) + str(b) < str(b) + str(a):
            return 1
        else:
            return 0
    sorted_numbers = sorted(numbers, key=cmp_to_key(compare))    
    result = int(''.join(map(str, sorted_numbers)))
    return str(result)
 
