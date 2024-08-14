def solution(order):
    
    res = 0
    
    for i in order:
        if "cafelatte" in i:
            res += 5000
        else:
            res += 4500
        
    return res