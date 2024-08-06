def solution(num_list):
    cnt = len(num_list)
    
    if 2<=cnt<=10:
        
        for i in num_list:
            
            if 1<=i<=9:
                pass
            else:
                return -1
            
        if num_list[cnt-1] > num_list[cnt-2]:
            num_list.append(num_list[cnt-1]-num_list[cnt-2])
            return num_list
        else:
            num_list.append(num_list[cnt-1]*2)
            return num_list
        
    else:
        return -1
            