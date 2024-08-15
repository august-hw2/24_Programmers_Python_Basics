def solution(myString):
    res = list(myString)

    for i in range(len(res)):
        if ord(res[i]) < ord("l"):
            res[i] = "l"

    return "".join(res)