def solution(my_string, index_list):
    if 1<=len(my_string)<=1000 and 1<=len(index_list)<=1000 and my_string.islower():
        
        res = "" #리턴할 결과 문자열 변수
        
        for i in range(0, len(index_list)):
            res += my_string[index_list[i]]
            
        return res
    
    return -1