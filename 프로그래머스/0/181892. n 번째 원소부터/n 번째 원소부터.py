def solution(num_list, n):
    if 2<=len(num_list)<=30 and 1<=n<=len(num_list):
        
        return num_list[n-1:]
        
    else:
        return -1