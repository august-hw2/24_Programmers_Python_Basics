def solution(number):
    if 1<=len(number)<=100000 and number.isdecimal():
        
        num = int(number) #정수형으로 변환
        sum_num = 0 #받은 정수 문자열 내 숫자의 총합 저장할 변수
        
        for i in range(0, len(number)):
            sum_num += int(number[i])
            
        if sum_num%9 == num%9:
            return num%9
        
    else:
        return -1