def solution(a, d, included):
    
    if 1<=a<=100 and 1<=d<=100 and 1<=len(included)<=100:

        result = 0

        for i in range(len(included)):
            result += (a + i * d) * int(included[i])
            #boolean배열 -> 정수형 변환 이용하여 1일 때만 계산값이 0이 아님

        return result

    else:
        return -1