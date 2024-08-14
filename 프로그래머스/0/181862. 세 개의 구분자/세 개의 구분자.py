import re

def solution(myStr):
    if 1<=len(myStr)<=1000000:
        
        if len(' '.join(re.split(r'[abc]', myStr)).split()) == 0:
            return ["EMPTY"]
        else:
            return ' '.join(re.split(r'[abc]', myStr)).split()
        
    else:
        return -1