def solution(num_list):
    if 3<=len(num_list)<=15:
        
        cnt = 0
        
        for i in range(len(num_list)):
            while num_list[i]!=1: #1이 아닐 때만 동작
                if num_list[i]%2==0: #짝수일 때
                    num_list[i]//=2
                    cnt += 1
                else: #홀수일 때
                    num_list[i]-=1
                    num_list[i]//=2
                    cnt += 1
        return cnt  
        
    else:
        return -1