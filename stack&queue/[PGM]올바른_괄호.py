# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    if len(s) == 1:
        return False
    
    closed = 0
    s = list(s)
    while s:
        if s.pop() == ')':
            closed += 1
        else:
            if not closed:
                return False
            closed -= 1
    if closed:
        return False
    
    return True