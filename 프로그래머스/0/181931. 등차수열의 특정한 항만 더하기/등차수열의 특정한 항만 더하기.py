def solution(a, d, included):
    
    if 1<=a<=100 and 1<=d<=100 and 1<=len(included)<=100:

        result = 0

        for i in range(len(included)):
            if included[i] == True:
                result += a + i * d

        return result

    else:
        return -1