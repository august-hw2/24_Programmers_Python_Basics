def solution(strArr):
    if 1<=len(strArr)<=1000:
        
        return [i for i in strArr if "ad" not in i]
        
    else:
        return -1