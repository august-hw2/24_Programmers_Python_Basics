def solution(picture, k):
    res = []

    for i in picture:
        temp = ""
        for j in range(len(i)):
            temp += i[j] * k
        for x in range(k):
            res.append(temp)
            
    return res