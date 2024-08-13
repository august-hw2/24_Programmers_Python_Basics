def solution(my_string, alp):
    if 1<=len(my_string)<=1000:
        
        return my_string.replace(alp, alp.upper())
        
    else:
        return -1