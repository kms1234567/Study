# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = ''
    
    s = s.lower()

    idx = 0
    for ch in s:
        if not idx:
            ch = ch.upper()
        idx += 1
        
        if ch == ' ':
            idx = 0
        
        answer += ch
        
    return answer