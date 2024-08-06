def solution(num_list):
    if 2<=len(num_list)<=10:
        even = "" #짝수
        odd = "" #홀수
        for i in range(len(num_list)):
            if 1<=num_list[i]<=9:
                if num_list[i]%2: #홀수인 경우
                    odd += str(num_list[i])
                else: #짝수인 경우
                    even += str(num_list[i])
            else:
                return -1
        return int(even)+int(odd)
    else: 
        return -1