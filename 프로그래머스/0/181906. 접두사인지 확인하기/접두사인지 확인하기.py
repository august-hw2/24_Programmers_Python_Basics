def solution(my_string, is_prefix):
    if 1<=len(my_string)<=100 and 1<=len(is_prefix)<=100 and my_string.islower() and is_prefix.islower():
        
        temp = [] #my_string의 접두사 저장할 리스트
        
        for i in range(1, len(my_string)+1):
            temp.append(my_string[:i])
        
        return 1 if is_prefix in temp else 0
            
    
    else:
        return -1