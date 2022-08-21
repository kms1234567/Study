# https://school.programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    res = 0
    for num, sign in zip(absolutes, signs):
        if not sign:
            num *= -1
        res += num
    
    return res