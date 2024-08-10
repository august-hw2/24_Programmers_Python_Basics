def solution(my_string, m, c):
    if 1<=m<=len(my_string) and len(my_string)<=1000 and my_string.islower():
        
        return my_string[c-1::m]
    
    else:
        return -1