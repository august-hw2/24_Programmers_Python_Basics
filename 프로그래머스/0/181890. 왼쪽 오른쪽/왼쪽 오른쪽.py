def solution(str_list):
    
    if 1<=len(str_list)<=20:
        
        
        for i, j in enumerate(str_list):
            if j == "l": #왼쪽인 경우
                return str_list[0:i]
                
            elif j == "r": #오른쪽인 경우
                return str_list[i+1:]

        return [] #"l" 또는 "r"이 없는 경우
    
    else:
        return -1