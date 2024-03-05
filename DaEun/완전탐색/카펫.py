def solution(brown, yellow):
    num = brown + yellow
    # 약수 찾기
    yaksu = []
    for i in range(num):
        if num % (i+1) == 0 :
            yaksu.append(i+1)
    answer = []
   # 조건 부합 확인
    for i in range(int(len(yaksu)/2+0.5)):
        width = yaksu[-(i+1)]
        height = yaksu[i]
        if (width-2)*(height-2) == yellow :
            answer.append(width)
            answer.append(height)

    return answer
