# https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    one_cnt = bin(n)[2:].count('1')
    cmp_cnt = -1
    
    while one_cnt != cmp_cnt:
        n += 1
        cmp_cnt = bin(n)[2:].count('1')

    return n