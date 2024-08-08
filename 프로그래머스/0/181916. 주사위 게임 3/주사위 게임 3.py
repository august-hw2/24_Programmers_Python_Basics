def solution(a, b, c, d):
    if 1<=a<=6 and 1<=b<=6 and 1<=c<=6 and 1<=d<=6:
        arr = [a, b, c, d]
        res_arr = [] #처음 나온 값만 저장
        temp_arr = [] #중복인 값만 저장
        
        
        for i in arr:
            if i not in res_arr: #해당 값이 없으면 배열에 저장
                res_arr.append(i)
            else: #해당 값이 있으면 중복이므로, 다른 배열에 저장
                temp_arr.append(i)
        
        if len(temp_arr) == 3: #모두 같은 값 -> 1개 제외한 나머지 모두 저장
            return 1111*a
        elif len(temp_arr) == 2: #4개 중 2개씩 중복 혹은 3개 중복 -> 중복된 값 2개 저장
            if len(set(temp_arr)) == 1: #temp에서도 중복이 발생한 경우
                for i in res_arr:
                    if i == temp_arr[0]: #temp와 동일한 값인 경우, 3번 중복인 값 찾기
                        p = i
                        res_arr.remove(i)
                return (10*p+res_arr[0])**2
            elif len(set(temp_arr)) == 2: #temp에서 중복이 발생하지 않은 경우
                return (res_arr[0]+res_arr[1])*abs(res_arr[0]-res_arr[1])                
        elif len(temp_arr) == 1: #4개 중 2개만 중복 -> 중복된 값 1개만 저장       
            res = 1
            
            for i in res_arr:
                if i != temp_arr[0]:
                    res *= i
            return res
        
        elif len(temp_arr) == 0: #서로 다른 값 -> 저장되지 않음
            return min(arr)
            
    return -1