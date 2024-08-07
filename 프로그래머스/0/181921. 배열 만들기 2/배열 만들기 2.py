def solution(l, r):
    
    if 1<=l<=1000000 and 1<=r<=1000000:
        
        res = []
        
        for i in range(l, r+1):
            
            if set(str(i)) <= {'0', '5'}:
                res.append(i)
        if len(res) == 0:
            res.append(-1)
        
        return res
        
    else:
        return -1