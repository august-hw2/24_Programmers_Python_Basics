def solution(my_string):
    if 1<=len(my_string)<=100 and my_string.islower():
        
        res = []
        
        for i in range(len(my_string)):
            res.append(my_string[i:])
        
        res.sort()
        
        return res
        
    else:
        return -1