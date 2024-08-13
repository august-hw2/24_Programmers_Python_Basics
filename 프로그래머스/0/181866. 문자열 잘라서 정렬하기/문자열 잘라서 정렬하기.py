def solution(myString):
    if 1<=len(myString)<=100000:
        
        res = myString.strip().split('x')
        
        res = list(filter(None, res))
                
        res.sort()
        
        return res
        
    else:
        return -1