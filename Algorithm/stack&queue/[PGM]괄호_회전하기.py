# https://school.programmers.co.kr/learn/courses/30/lessons/76502

from collections import deque
from copy import deepcopy
def check(s):
    s = deepcopy(s)
    stk = []
    
    reverse = {'{' : '}', '(':')', '[':']',']':'', ')':'', '}':''}
    while s:
        com = s.pop()
        if not stk:
            stk.append(com)
            continue
        
        if stk[-1] == reverse[com]:
            stk.pop()
            continue
            
        stk.append(com)
        
    return True if not stk else False    

def solution(s):
    answer = 0
    len_s = len(s)
    
    s = deque(s)
    
    for _ in range(0, len_s):
        s.rotate(1)
 
        if check(s):
            answer += 1
    return answer