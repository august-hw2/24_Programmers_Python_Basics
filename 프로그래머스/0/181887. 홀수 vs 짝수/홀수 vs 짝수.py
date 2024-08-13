def solution(num_list):

        
    even = num_list[::2]#짝수 인덱스
    odd = num_list[1::2]#홀수 인덱스
        
    return max(sum(even), sum(odd))
