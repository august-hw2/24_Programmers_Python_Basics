def solution(my_string, indices):
    if 1<=len(indices)<len(my_string) and len(my_string)<=100 and my_string.islower() and len(set(indices)) == len(indices):
        
        res = ""
        
        for i in range(len(my_string)):
            if i not in indices:
                res += my_string[i]
            
        return res
        
    else:
        return -1