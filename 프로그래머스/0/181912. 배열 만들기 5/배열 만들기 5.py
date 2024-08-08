def solution(intStrs, k, s, l):

        
    res = []      #결과 값 저장할 리스트
        
    for i in intStrs:

        if int(i[s:s+l]) > k:
            res.append(int(i[s:s+l]))
            
    return res