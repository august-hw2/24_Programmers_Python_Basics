def solution(myString, pat):
    if 1<=len(myString)<=100 and 1<=len(pat)<=10:
        
        res = list(myString)
        
        for i in range(len(res)):
            if res[i] == 'A':
                res[i] = 'B'
            elif res[i] == 'B':
                res[i] = 'A'
                
        res_str = ''.join(res)
        
        if pat in res_str:
            return 1
        else:
            return 0
        
    else:
        return -1