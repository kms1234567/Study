# https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    s = list(s)
    stk = []
    
    for ch in s:
        if not stk:
            stk.append(ch)
            continue
        
        if stk[-1] == ch:
            stk.pop()
        else:
            stk.append(ch)

    return 0 if stk else 1