def solution(ineq, eq, n, m):
    if 1<=n<=100 and 1<=m<=100:
        if ineq == ">" and eq == "=":
            return 1 if n >= m else 0
        elif ineq == "<" and eq == "=":
            return 1 if n <= m else 0
        elif ineq == ">" and eq == "!":
            return 1 if n > m else 0
        elif ineq == "<" and eq == "!":
            return 1 if n < m else 0
    else: return -1