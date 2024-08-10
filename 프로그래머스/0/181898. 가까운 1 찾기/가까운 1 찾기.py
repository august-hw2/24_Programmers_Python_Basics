def solution(arr, idx):
    if 3<=len(arr)<=100000:
        
        for i in range(idx, len(arr)):
            if arr[i] == 1:
                return i
    
        return -1
    
    else:
        return -1