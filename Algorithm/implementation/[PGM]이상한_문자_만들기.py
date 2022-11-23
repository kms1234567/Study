# https://school.programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    answer = ''

    tmp = 0
    for char in s:
        if char == ' ':
            answer += ' '
            tmp = 0
            continue
            
        if not tmp%2:
            answer += char.upper()
        else:
            answer += char.lower()
        tmp += 1
        
    return answer