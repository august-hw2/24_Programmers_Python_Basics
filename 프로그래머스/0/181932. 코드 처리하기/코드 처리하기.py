def solution(code):
    ret = ''
    mode = 0
    
    if 1<=len(code)<=100000:

        for idx in range(len(code)):

            if mode == 0: #모드 = 0
                if code[idx] != '1' and idx%2 == 0:
                    ret += code[idx]
                elif code[idx] == '1':
                    mode = 1

            else: #모드 = 1
                if code[idx] != '1' and idx%2 != 0:
                    ret += code[idx]
                elif code[idx] == '1':
                    mode = 0
        return "EMPTY" if ret == "" else ret
    
    return -1