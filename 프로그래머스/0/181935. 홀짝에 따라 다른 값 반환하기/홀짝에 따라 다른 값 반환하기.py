def solution(n):
    if 1<=n<=100:
        
        if n%2:
            return sum(range(1, n+1, 2))
        else:
            return sum(i**2 for i in range(2, n+1, 2))
        
    else: return -1