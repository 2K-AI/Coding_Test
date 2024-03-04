def solution(answers):

    answer_one = [1,2,3,4,5]*2000
    answer_one = answer_one[:len(answers)]

    answer_two =[2,1,2,3,2,4,2,5]*1250
    answer_two = answer_two[:len(answers)]

    answer_three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    answer_three = answer_three[:len(answers)]

    sum_one , sum_two, sum_three = 0,0,0
    for i in range(len(answers)): 
        if answers[i]== answer_one[i]:
            sum_one+=1
        if answers[i]== answer_two[i]:
            sum_two+=1
        if answers[i]== answer_three[i]:
            sum_three+=1

    my_dict = {    1: sum_one,     2: sum_two,      3: sum_three }
    my_dict = sorted(my_dict.items(), key=lambda x: (-x[1], x[0]))
    max_value = max(dict(my_dict).values())

    answer =[]
    for tup in my_dict:
        if tup[1]== max_value:
            answer.append(tup[0])
    return answer
