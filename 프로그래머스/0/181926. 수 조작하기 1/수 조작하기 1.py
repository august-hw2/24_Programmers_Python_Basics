def solution(n, control):

    if -100000<=n<100000 and 1<=len(control)<=100000 and control.islower():
        for i in range(len(control)):
            if "w" == control[i]:
                n += 1
            elif "s" == control[i]:
                n -= 1
            elif "d" == control[i]:
                n += 10
            elif "a" == control[i]:
                n -= 10
            else:
                return -1
        return n

    else: 
        return -1