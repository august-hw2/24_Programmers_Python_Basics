def solution(myString, pat):
    if 1<=len(myString)<=1000 and 1<=len(pat)<=10:
        
        cnt = 0

        for i in range(len(myString)):
            if myString[i:len(pat)+i] == pat:
                cnt += 1
                
        return cnt
        
    else:
        return -1