def solution(my_string):
    if 1<=len(my_string)<=1000 and my_string.isalpha():
        
        res = [0] * 52
        
        for i in my_string:
            if i.isupper():#대문자
                res[ord(i) - 65] += 1
            else:  #소문자
                res[ord(i) - 71] += 1
            
        return res
        
    else:
        return -1