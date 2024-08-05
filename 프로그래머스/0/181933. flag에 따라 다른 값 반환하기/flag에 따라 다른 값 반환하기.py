def solution(a, b, flag):
    if -1000<=a<=1000 and -1000<=b<=1000:
        if flag:
            return a+b 
        else:
            return a-b 
    else: return -1