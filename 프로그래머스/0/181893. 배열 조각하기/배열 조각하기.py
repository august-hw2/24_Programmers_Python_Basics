def solution(arr, query):
    if 5<=len(arr)<=100000:
        
        for i, j in enumerate(query):

            if i % 2 == 0:  #인덱스가 짝수일 때

                del arr[j+1:]

            else:  #인덱스가 홀수일 때

                del arr[:j]

        return arr
    
    else:
        return -1