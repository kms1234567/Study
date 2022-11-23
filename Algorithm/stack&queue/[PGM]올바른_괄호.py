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

def solution(s):
    stk = []
    s = list(s)
    while s:
        bracket = s.pop()
        if bracket == ')':
            stk.append(bracket)
        else:
            if stk and stk[-1] == ')':
                stk.pop()
            else:
                return False
        
    return True if not stk else False