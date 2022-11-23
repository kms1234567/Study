# https://school.programmers.co.kr/learn/courses/30/lessons/12918

import re
def solution(s):
    
    len_s = len(s)
    if len_s !=4 and len_s != 6:
        return False
    
    return False if re.search('[\D]',s) else True