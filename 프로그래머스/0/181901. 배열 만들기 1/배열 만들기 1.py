def solution(n, k):
    if 1<=n<=1000000 and 1<=k<=min(1000,n):
        
        res = []
        
        for i in range(1, n+1):
            res.append(i)
            
        return res[k-1::k]
        
    else:
        return -1