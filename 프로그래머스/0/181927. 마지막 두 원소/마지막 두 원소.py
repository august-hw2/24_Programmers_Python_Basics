def solution(num_list):
    cnt = len(num_list)
    last = num_list[cnt-1]
    notlast = num_list[cnt-2]
    
    if 2<=cnt<=10:
        
        for i in num_list:
            
            if 1<=i<=9:
                pass
            else:
                return -1
            
        num_list.append(last-notlast) if last > notlast else num_list.append(last*2)
        return num_list
        
    else:
        return -1
            