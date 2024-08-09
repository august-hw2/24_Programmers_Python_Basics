def solution(my_string, n):
    if 1<=len(my_string)<=1000 and my_string.isalnum():
        
        return my_string[-n:]
        
    else:
        return -1