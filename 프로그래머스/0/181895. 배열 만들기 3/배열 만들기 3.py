def solution(arr, intervals):
    if 1<=len(arr)<=100000:
        
        res = []
    
        for a, b in intervals:
            for i in range(a, b+1):
                res.append(arr[i])
            
        return res
        
    else:
        return -1