# Level 1
def solution(sizes):
    n = 0
    for i, j in sizes:
        if j > i :
            sizes[n][0] = j
            sizes[n][1] = i
        n+=1
    maxi, maxj = 0, 0
    for i in range(n):
        if sizes[i][0] > maxi :
            maxi = sizes[i][0]
    for i in range(n):
        if sizes[i][1] > maxj :
            maxj = sizes[i][1]
    answer = maxi * maxj
    return answer
