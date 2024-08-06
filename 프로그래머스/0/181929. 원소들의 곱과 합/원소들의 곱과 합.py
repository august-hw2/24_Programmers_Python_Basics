from math import prod

def solution(num_list):
    
    if 2<=len(num_list)<=10:
        
        pro = 1
        
        
        for i in range(len(num_list)):
            if 1<=num_list[i]<=9:
                pass
            else: return -1
        return 1 if prod(num_list) < sum(num_list)**2 else 0
    
    else: 
        return -1