def solution(arr):
    if 1<=len(arr)<=100:
        
        res = []
        
        for i in range(len(arr)):
            for j in range(arr[i]):
                res.append(arr[i])
                
        return res
        
    else:
        return -1