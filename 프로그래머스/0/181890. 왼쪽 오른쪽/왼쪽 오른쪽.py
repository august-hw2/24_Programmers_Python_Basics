def solution(str_list):
    
    if 1<=len(str_list)<=20:
        
        res = [] #결과값 리스트 선언
        
        for i, j in enumerate(str_list):
            if j == "l": #왼쪽인 경우
                res+=str_list[0:i]
                return res
                
            elif j == "r": #오른쪽인 경우
                res+=str_list[i+1:]
                return res
            
        return res #"l" 또는 "r"이 없는 경우
    
    else:
        return -1