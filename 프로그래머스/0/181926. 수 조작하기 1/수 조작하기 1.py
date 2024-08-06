def solution(n, control):

    if -100000<=n<100000 and 1<=len(control)<=100000 and control.islower():
        
        control_dict = {"w":1, "s":-1, "d":10, "a":-10}
        
        for i in control:
            n += control_dict[i]
        return n

    else: 
        return -1