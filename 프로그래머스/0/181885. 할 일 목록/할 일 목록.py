def solution(todo_list, finished):
    if 1<=len(todo_list)<=100:
        
        res = []
        
        for i, j in enumerate(finished):
            if j == False:
                res.append(todo_list[i])
                
        return res
        
    else:
        return -1