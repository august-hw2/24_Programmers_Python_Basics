def solution(num_list, n):
    if 5<=len(num_list)<=20 and 1<=n<=4:
    
        return num_list[::n]
    
    else:
        return -1