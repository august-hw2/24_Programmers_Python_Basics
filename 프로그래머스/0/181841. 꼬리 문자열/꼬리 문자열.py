def solution(str_list, ex):
    res = ""

    for i in range(len(str_list)):
            if ex not in str_list[i]:
                res += str_list[i]

    return res