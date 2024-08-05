def solution(a, b):
    
    if 1<=a<10000 and 1<=b<10000:
        
        c = str(a)+str(b)
        d = int(c)
        
        if d == 2*a*b:
            return d
        else:
            return max(d, 2*a*b)