def solution(arr):
        
    while True:
        
        n = len(arr)
        
        if n&(n-1) == 0:
            return arr
        else:
            arr.append(0)