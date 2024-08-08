def solution(my_string, queries):
    if 1<=len(my_string)<=1000 and my_string.islower() and 1<=len(queries)<=1000:
        
        arr = list(my_string) #문자열 -> 리스트화
        re_arr = "" #빈 문자열
        re_list = [] #빈 리스트

        for s, e in queries: #queries의 요소 값
            re_arr = reversed(arr[s:e+1]) #리스트 슬라이싱 -> 끝 숫자 포함하지 않으므로, +1
            re_list = list(re_arr)

            i = 0 

            while s < e+1:

                arr[s] = re_list[i]
                s += 1
                i += 1


            re_arr = [] #초기화

    return ''.join(arr)
    
    return -1
        