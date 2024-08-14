def solution(arr, flag):
    
    res = []
    
    for i, j in enumerate(arr):
        if flag[i] == True:
            for x in range(j*2):
                res.append(j)
        else:
            for y in range(j):
                res.pop()

    return res