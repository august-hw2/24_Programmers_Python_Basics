def solution(arr, queries):
    if 1<=len(arr)<=1000 and 1<=len(queries)<=1000:
        
        for i, j in queries:
            for x in range(i, j+1):
                arr[x] += 1
                
        return arr
        
    else:
        return -1