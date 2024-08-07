def solution(arr, queries):
    if 1<=len(arr)<=1000 and 1<=len(queries)<=1000:
        for i, j in queries:
            if 0<=i<j<len(arr):
                arr[i], arr[j] = arr[j], arr[i]

        return arr
    else:
        return -1