def solution(my_strings, parts):
    if 1<=len(my_strings)<=100 and 1<=len(parts)<=100:
        
        res = ""
        
        for i, (s, e) in zip(my_strings, parts):

            res += i[s:e+1]

        return res
            
              
    else:
        return -1
    