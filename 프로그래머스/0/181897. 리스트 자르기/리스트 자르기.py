def solution(n, slicer, num_list):
    if len(slicer) == 3 and 5<=len(num_list)<=30:
        
        a = slicer[0]
        b = slicer[1]
        c = slicer[2]
        
        if n == 1:
            return num_list[0:b+1]
            
        elif n == 2:
            return num_list[a:]
            
        elif n == 3:
            return num_list[a:b+1]
            
        elif n == 4:
            return num_list[a:b+1:c]
            
        else:
            return -1 
    else:
        return -1