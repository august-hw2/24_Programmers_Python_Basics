def solution(binomial):
        
    res = binomial.split()
    
    if res[1] == '+':
        return int(res[0]) + int(res[2])
    elif res[1] == '-':
        return int(res[0]) - int(res[2])
    elif res[1] == '*':
        return int(res[0]) * int(res[2])
