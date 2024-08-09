def solution(my_string, s, e):
    if 1<=len(my_string)<=1000 and my_string.isalnum():
        
        return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
        
    else:
        return -1