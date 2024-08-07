def solution(arr, queries):
    if 1<=len(arr)<1000 and 1<=len(queries)<=1000:
        
        for s, e, k in queries:
            
            for i in range(s, e+1):
                if i%k == 0:
                    arr[i] += 1
        return arr
    else:
        return -1