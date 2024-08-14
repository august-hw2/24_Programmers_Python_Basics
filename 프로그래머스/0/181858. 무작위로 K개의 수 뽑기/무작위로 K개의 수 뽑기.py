def solution(arr, k):
    res = []

    for i in arr:
        if i not in res and len(res) < k:
            res.append(i)

    if len(res) == k:
        return res
    else:
        for i in range(k - len(res)):
            res.append(-1)
        return res