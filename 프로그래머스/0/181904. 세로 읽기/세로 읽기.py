def solution(my_string, m, c):
    if 1<=m<=len(my_string) and len(my_string)<=1000 and my_string.islower():
        
        return my_string[c-1::m] #입력받은 문자열의 c-1의 자리에 있는 글자부터 끝까지 m씩 증가하여 이은 문자열 리턴
    
    else:
        return -1