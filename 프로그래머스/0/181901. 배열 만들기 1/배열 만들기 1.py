def solution(n, k):
    if 1<=n<=1000000 and 1<=k<=min(1000,n):
            
        return [i for i in range(k, n+1, k)] #[] 이용해서 한 번에 리스트 반환
        
    else:
        return -1