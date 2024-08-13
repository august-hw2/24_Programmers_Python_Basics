def solution(strArr):
    if 1<=len(strArr)<=20:
        
        for i in range(len(strArr)):
            if i%2: #홀수일 때
                strArr[i] = strArr[i].upper()
            else: #짝수일 때
                strArr[i] = strArr[i].lower()
                
        return strArr
    
    else:
        return -1