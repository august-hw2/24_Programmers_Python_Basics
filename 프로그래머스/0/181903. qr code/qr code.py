def solution(q, r, code):
    if 0<=r<q and q<=20 and r<len(code)<=1000 and code.islower():
        
        res = ""
        
        for i in range(len(code)):
            if i%q == r:
                res = res + code[i]
                
        return res
        
    else:
        return -1