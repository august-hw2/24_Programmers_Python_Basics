def solution(num_list):
    if 5<=len(num_list)<=100:
        
        for i in range(len(num_list)):
            if num_list[i]<0:
                return i
            else:
                pass
        return -1
        
    else:
        return -1