def solution(my_strings, parts):
    if 1<=len(my_strings)<=100 and 1<=len(parts)<=100:
        
        res = ""
        
        for i in range(len(parts)):
            
            temp = my_strings[i] #문자열 배열 임시 저장

            res += temp[parts[i][0]:parts[i][1]+1]

        return res
            
              
    else:
        return -1
    