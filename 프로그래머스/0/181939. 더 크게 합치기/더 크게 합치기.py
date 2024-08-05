def solution(a, b):
    
    if 1<=a<10000 and 1<=b<10000:
        c = str(a)+str(b)
        d = str(b)+str(a)

        if int(c) < int(d):
            return int(d)
        elif int(c) > int(d):
            return int(c)
        elif int(c) == int(d):
            return int(c)
    else:
        return -1