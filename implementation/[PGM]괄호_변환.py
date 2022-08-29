# https://school.programmers.co.kr/learn/courses/30/lessons/60058

from collections import deque

def checkCorrectBracket(strings):
    stk = list(strings)
    dicts = {'(':0, ')':0}
    while stk:
        bracket = stk.pop()
        dicts[bracket] += 1
        if dicts['('] > dicts[')']:
            return False
    return True

def retBalancedBracket(strings):
    queue = deque(strings)
    dicts = {'(':0, ')':0}
    
    u = '';v=''
    while queue and not dicts['('] or dicts['('] != dicts[')']:
        bracket = queue.popleft()
        u += bracket
        dicts[bracket] += 1
    
    while queue:
        v += queue.popleft()
    
    return [u, v]
    
def makeCorrectBracket(u, v):    
    tmp = '('
    tmp += solution(v)
    tmp += ')'
    
    dicts = {'(':')', ')':'('}
    tmp_bracket = u[1:len(u)-1]
    new_bracket = ''
    for c in tmp_bracket:
        new_bracket += dicts[c]
    tmp += new_bracket
    
    return tmp
    
def solution(p):
    if not p:
        return p
    
    u, v = retBalancedBracket(p)

    if checkCorrectBracket(u):
        v = solution(v)
        u+=v
        return u
    else:
        return makeCorrectBracket(u, v)