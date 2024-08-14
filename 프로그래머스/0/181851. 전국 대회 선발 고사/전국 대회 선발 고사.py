def solution(rank, attendance):
    temp = dict(zip(rank, attendance)) #keys: rank, values: attendance

    check = sorted(temp.items())

    res = []

    for i, j in check:
        if j: #참석여부가 True일 때
            res.append(i)

    return 10000*rank.index(res[0])+100*rank.index(res[1])+rank.index(res[2])