def solution(q, r, code):
    if 0<=r<q and q<=20 and r<len(code)<=1000 and code.islower():
        
        return code[r::q] #r부터 q씩 증가하는 문자열 반환
        
    else:
        return -1