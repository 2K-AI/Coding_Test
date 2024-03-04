def solution(word):
    all = []
    vowels = ['A','E','I',"O",'U']
    # 한 글자
    all = all + vowels
    #두 글자
    for i in vowels:
        for j in vowels:
            new = str(i+j)
            all.append(new)
    #세 글자
    for i in vowels:
        for j in vowels:
            for k in vowels:
                new = str(i+j+k)
                all.append(new)
    #네 글자
    for i in vowels:
        for j in vowels:
            for k in vowels:
                for t in vowels:
                    new = str(i+j+k+t)
                    all.append(new)
    #다섯 글자
    for i in vowels:
        for j in vowels:
            for k in vowels:
                for t in vowels:
                    for p in vowels:
                        new = str(i+j+k+t+p)
                        all.append(new)
    all.sort()
    answer = all.index(word)+1            
        
    return answer
