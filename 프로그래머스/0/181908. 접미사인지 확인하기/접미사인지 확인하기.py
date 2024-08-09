def solution(my_string, is_suffix):
    if 1<=len(my_string)<=100 and 1<=len(is_suffix)<=100 and my_string.islower() and is_suffix.islower():
        
        temp = [] #my_string의 접미사를 저장할 리스트
        
        for i in range(len(my_string)):
            temp.append(my_string[i:])
    
        if is_suffix in temp:
            return 1
        else:
            return 0
    
    else:
        return -1