def solution(arr):
        
    while True:
        
        n = len(arr)
        
        if n&(n-1) == 0:
            return arr
        else:
            arr.append(0)
            
        # n=4 -> 거듭제곱 O => n&(n-1) = 0100 & 0011 = 0000 == 0
        # n=6 -> 거듭제곱 X => n&(n-1) = 0110 & 0110 = 0100 !=0