def solution(a, b):
    if a%2 and b%2: #둘 다 홀수
        return a**2+b**2
    elif a%2 or b%2: #하나만 홀수
        return 2*(a+b)
    else: #둘 다 짝수
        return abs(a-b)
        