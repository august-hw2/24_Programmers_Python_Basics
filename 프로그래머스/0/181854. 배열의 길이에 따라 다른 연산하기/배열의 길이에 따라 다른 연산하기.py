def solution(arr, n):
    
    if len(arr)%2: #홀수일 때
        for i in range(len(arr)):
            if i%2==0:
                arr[i] += n
    else:
        for i in range(len(arr)):
            if i%2:
                arr[i] += n
                
    return arr