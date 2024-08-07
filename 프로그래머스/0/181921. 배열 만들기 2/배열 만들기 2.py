def solution(l, r):
    
    if 1<=l<=1000000 and 1<=r<=1000000:
        
        res = []
        
        for i in range(l, r+1):
            
            if not set(str(i)) - set(['0', '5']):
                #(모든 정수 - 0과 5가 포함된 정수) = 0과 5가 포함되지 않은 정수만 추출되나, not을 붙여 0과 5만 포함된 정수일 때만 배열에 요소 추가
                res.append(i)
                
        if len(res) == 0:
            res.append(-1)
        
        return res
        
    else:
        return -1