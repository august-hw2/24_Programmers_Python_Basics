def solution(start_num, end_num):
    if 0<=end_num<=start_num and start_num<=50:
        
        return [i for i in range(start_num, end_num-1, -1)]
        
    else:
        return -1