def solution(my_string):
    if 1<=len(my_string)<=1000 and my_string.isalpha():
        
        res = [0] * 52
        
        for i in range(len(my_string)):
            if 65 <= ord(my_string[i]) <= 90: #대문자
                res[ord(my_string[i]) - 65] += 1
            elif 97 <= ord(my_string[i]) <= 122: #소문자
                res[ord(my_string[i]) - 71] += 1
            
        return res
        
    else:
        return -1