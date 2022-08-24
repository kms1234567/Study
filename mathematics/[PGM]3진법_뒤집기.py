# https://school.programmers.co.kr/learn/courses/30/lessons/68935


def change(n):
    ret = ''
    while True:
        if n < 3:
            ret += str(n)
            break
        ret += (str(n%3))
        n //= 3
    return ret   

def solution(n):
    return int(change(n), 3)