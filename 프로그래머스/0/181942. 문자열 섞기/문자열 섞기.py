def solution(str1, str2):

    if 1<=len(str1)<=10 and 1<=len(str2)<=10 and len(str1)==len(str2):
        if str1.islower() and str2.islower():
            answer = ''
            for i in range(0, len(str2)):
                answer += str1[i]+str2[i]
        else:
            return -1
    else:
        return -1
    return answer