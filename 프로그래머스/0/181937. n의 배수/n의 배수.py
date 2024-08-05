def solution(num, n):
    if 2<=num<=100 and 2<=n<=9:
        if num%n == 0:
            return 1
        else: return 0
    else: return -1