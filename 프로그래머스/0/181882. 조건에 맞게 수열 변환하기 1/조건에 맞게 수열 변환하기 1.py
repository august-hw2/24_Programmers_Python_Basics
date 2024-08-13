def solution(arr):
    if 1<=len(arr)<=1000000:
        
        for i in range(len(arr)):
            if arr[i]>=50 and arr[i]%2==0:
                arr[i] //= 2
            elif arr[i]<50 and arr[i]%2!=0:
                arr[i] *= 2
        return arr
        
    else:
        return -1