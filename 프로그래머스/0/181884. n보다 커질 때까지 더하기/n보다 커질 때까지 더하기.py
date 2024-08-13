def solution(numbers, n):
    if 1<=len(numbers)<=100 and 0<=n<=sum(numbers):
        
        res = 0
        
        for i in numbers:
            if res <= n:
                res += i
            else:
                return res
        return res
        
    else:
        return -1