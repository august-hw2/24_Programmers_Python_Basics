def solution(my_string, queries):
    if 1<=len(my_string)<=1000 and my_string.islower() and 1<=len(queries)<=1000:
        
        arr = list(my_string) #문자열 -> 리스트화
        re_arr = "" #빈 문자열
        re_list = [] #빈 리스트

        for s, e in queries: #queries의 요소 값
            arr[s:e+1] = arr[s:e+1][::-1] 
            #[::-1] -> 역순으로 리스트 요소 가져오기

        return ''.join(arr)
    
    return -1
        