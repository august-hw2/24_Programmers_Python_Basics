def solution(n):
    if 1<=n<=1000:
        
        res=[]
        res.append(n)
        
        while n!=1: #1이 아닐 때만
            if n%2==0:
                n /= 2
                res.append(n)
            else:
                n *= 3
                n += 1
                res.append(n)
        return res
    else:
        return -1