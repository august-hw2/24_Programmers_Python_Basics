def solution(myString, pat):
    if 1<=len(myString)<=100000 and 1<=len(pat)<=300:
        
        return int(pat.lower() in myString.lower())
        
    else:
        return -1