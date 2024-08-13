def solution(myString):
    if 1<=len(myString)<=100000:
        
        return [len(i) for i in myString.strip().split('x')]
        
    else:
        return -1