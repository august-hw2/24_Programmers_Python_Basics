def solution(arr):
    if 1<=len(arr)<=100000:
        
        stk = []
        i = 0
    
        while i<len(arr):

            if len(stk) == 0:
                stk.append(arr[i])
                i += 1
            else:
                if stk[len(stk) - 1] < arr[i]:
                    stk.append(arr[i])
                    i += 1
                else:
                    stk.pop(len(stk) - 1)
        return stk
    
    else:
        return -1
