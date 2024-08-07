def solution(numLog):
    
    if 2<=len(numLog)<=100000 and -100000<=numLog[0]<=100000:
        
        result = ""
        str_arr = {1: "w", -1: "s", 10: "d", -10: "a"}
        
        for i in range(1, len(numLog)): 
            cnt = numLog[i] - numLog[i-1] #현재 숫자 - 이전 숫자의 값
            
            if cnt in str_arr.keys(): #차이값이 딕셔너리의 키인지 확인
                result += str_arr[cnt]       
                
        return result
    
    else:
        return -1