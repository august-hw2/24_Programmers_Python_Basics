def solution(number, n, m):
    if 10<=number<=100 and 2<=n<=10 and 2<=m<=10:
        if number%n == 0 and number%m == 0:
            return 1
        else: return 0
    else: return -1