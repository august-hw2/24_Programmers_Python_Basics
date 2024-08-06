def solution(a, b, c):
    res1 = a+b+c
    res2 = (a**2) + (b**2) + (c**2)
    res3 = (a**3) + (b**3) + (c**3)
    if a != b and b != c and c != a: #모두 다른 경우
        return res1
    elif a == b and b == c and c == a: #모두 같은 경우
        return res1*res2*res3
    else: #나머지 경우
        return res1*res2
