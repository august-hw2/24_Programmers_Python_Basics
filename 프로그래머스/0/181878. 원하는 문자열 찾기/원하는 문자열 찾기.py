def solution(myString, pat):
    if 1<=len(myString)<=100000 and 1<=len(pat)<=300:
        
        if len(pat)>len(myString):
            return 0
        
        if pat.lower() in myString.lower():
            return 1
        else:
            return 0
        
    else:
        return -1