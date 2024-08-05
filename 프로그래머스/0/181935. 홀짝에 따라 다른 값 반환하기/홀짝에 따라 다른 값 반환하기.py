def solution(n):
    if 1<=n<=100:
        
        result = 0
        
        if n%2 == 0:
            for i in range(2, n+1, 2):
                result += (i*i)
            return result
        else:
            for i in range(1, n+1, 2):
                result += i
            return result
    else: return -1