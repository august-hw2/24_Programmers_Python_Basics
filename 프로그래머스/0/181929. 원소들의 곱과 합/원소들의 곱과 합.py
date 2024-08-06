def solution(num_list):
    
    if 2<=len(num_list)<=10:
        
        pro = 1
        
        
        for i in range(len(num_list)):
            pro *= num_list[i] if 1<=num_list[i] else -1
        return 1 if pro < sum(num_list)**2 else 0
    
    else: 
        return -1