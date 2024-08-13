def solution(num_list):
    if 2<=len(num_list)<=20:
        
        res = 1
        
        if len(num_list)>=11:
            return sum(num_list)
        else:
            for i in num_list:
                res *= i
            return res    
        
    else: 
        return -1