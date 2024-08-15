def solution(n):
    
    arr = []
    temp = []
    
    for i in range(n):
        
        for j in range(n):
            
            temp.append(1) if i == j else temp.append(0)
                
        arr.append(temp)
        
        temp = []
        
    return arr