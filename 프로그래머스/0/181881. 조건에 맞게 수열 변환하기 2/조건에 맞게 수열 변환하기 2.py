def solution(arr):
    if 1<=len(arr)<=1000000:
        
        temp = arr.copy()
        res = 0
        
        while True:
            
            for i in range(len(arr)):
                if arr[i] >= 50 and arr[i] % 2 == 0:
                    arr[i] //= 2
                elif arr[i] < 50 and arr[i] % 2 != 0:
                    arr[i] = arr[i] * 2 + 1

            if arr == temp: #바뀐 리스트와 기존 리스트 비교
                return res
            else:
                temp = arr.copy()
                res += 1
        
    else:
        return -1