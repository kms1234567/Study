# https://school.programmers.co.kr/learn/challenges?order=recent&levels=2&languages=python3

def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        a = i//n # 몫
        b = i%n #나머지 
        a = max(a,b) 
        answer.append(a+1)
    
    return answer