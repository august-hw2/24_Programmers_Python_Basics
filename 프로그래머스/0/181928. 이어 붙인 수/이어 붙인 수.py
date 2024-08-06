def solution(num_list):
    if 2<=len(num_list)<=10:
        even = "" #짝수
        odd = "" #홀수
        for i in num_list:
            if 1<=i<=9:
                if i%2: #홀수인 경우
                    odd += str(i)
                else: #짝수인 경우
                    even += str(i)
            else:
                return -1
        return int(even)+int(odd)
    else: 
        return -1