def solution(str_list, ex):
    res = ""

    for i in str_list:
            if ex not in i:
                res += i

    return res