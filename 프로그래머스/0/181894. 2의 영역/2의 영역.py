def solution(arr):
    if 1<=len(arr)<=100000:
        
        res = []
        cnt = arr.count(2)
        
        if 2 in arr:
            if cnt == 1:
                res.append(2)
            elif cnt >= 2:
                
                idx = arr.index(2)
                re_arr = arr.copy()

                re_arr.reverse()
                re_idx = re_arr.index(2)

                return arr[idx:len(arr)-re_idx]
                
        elif 2 not in arr:
            res.append(-1)
        return res
    else:
        return -1