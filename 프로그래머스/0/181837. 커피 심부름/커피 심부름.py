def solution(order):
    
    res = 0
    
    for i in order:
        if "americano" in i:
            res += 4500
        elif "cafelatte" in i:
            res += 5000
        elif "anything" in i:
            res += 4500
    return res