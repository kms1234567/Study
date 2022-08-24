# https://school.programmers.co.kr/learn/courses/30/lessons/12926

def change(c, n):
    if c.islower():
        std = ord('z')
        s = ord('a')
    else:
        std = ord('Z')
        s = ord('A')
        
    num = ord(c) + n

    if num > std:
        num = s + (num - (std+1))

    return chr(num)

def solution(s, n):
    answer = ''
    
    for char in s:
        if char == ' ':
            answer += ' '
        else:
            answer += change(char, n)
    
    return answer