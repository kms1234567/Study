# https://school.programmers.co.kr/learn/courses/30/lessons/12899#

# 다른 풀이
def solution(n):
    num = ['1','2','4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer



def solution(n):
    answer = ''
    
    dicts = {'0':'4', '3':'4', '1':'1', '2':'2'}
    
    isZero = False
    while True:
        if n <= 3:
            answer += str(n)
            break
        
        rem = n%3
        if not rem:
            isZero = True
        else:
            isZero = False
        answer += str(rem)
        n = n//3
        if isZero:
            n -= 1
    
    answer = answer[-1::-1]
    
    res = ''
    for ans in answer:
        res += dicts[ans]
    
    return res