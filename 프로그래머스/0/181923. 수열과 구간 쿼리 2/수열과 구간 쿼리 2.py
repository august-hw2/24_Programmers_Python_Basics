def solution(arr, queries):
    if 1<=len(arr)<=1000 and 1<=len(queries)<=1000:
        res_arr = []
        
        for i in arr:
            if 0<=i<=1000000:
                pass
            else:
                return -1
        
        for s, e, k in queries:
            min_arr=[]
            new_arr = arr[s:e+1] #끝 번호는 포함되지 않으므로, +1 해줌
            if max(new_arr) > k:
                for i in new_arr:
                    if i > k:
                        min_arr.append(i) #k보다 큰 숫자만 저장
                res_arr.append(min(min_arr))
            else: #k보다 큰 숫자가 없을 경우, -1 반환
                res_arr.append(-1)
        return res_arr
    return -1