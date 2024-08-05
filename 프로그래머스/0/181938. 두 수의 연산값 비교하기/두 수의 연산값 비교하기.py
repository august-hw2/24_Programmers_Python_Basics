def solution(a, b):
    
    if 1<=a<10000 and 1<=b<10000:
        
        c = str(a)+str(b)
        d = int(c)
        
        return d if d == 2*a*b else max(d, 2*a*b)