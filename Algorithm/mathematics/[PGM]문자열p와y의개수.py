# https://school.programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    s = s.lower()
    
    p = s.count('p')
    y = s.count('y')  

    return p == y