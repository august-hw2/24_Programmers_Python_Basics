def solution(start_num, end_num):
    if 0<=start_num<=50 and 0<=end_num<=50:
        res=[]
        for i in range(start_num, end_num+1):
            res.append(i)   
        return res
    else:
        return -1