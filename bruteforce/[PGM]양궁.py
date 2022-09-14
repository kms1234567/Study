# https://school.programmers.co.kr/learn/courses/30/lessons/92342
from itertools import * 
def retScore(a, b):
    totalB = 0;totalA = 0;score=10
    
    for i, j in zip(a, b):
        if j > i:
            totalB += score
        elif i:
            totalA += score
        score -= 1
        
    return totalB - totalA

def solution(n, info):
    answer = []
    diff_sum = 1
    # 시뮬레이션 방식과 그리디 방식이있음
    # 시뮬레이션 방식 : combinations_with_replacement() 메소드로 모든 경우의수를 따져봄.
    # 그리디 방식 : 해당 점수를 먹을것이냐 포기할것이냐를 비트마스킹 방식으로 2^10(1024)가지의 경우만 따져볼 수 있음.
    
    for combi in combinations_with_replacement(range(11), n):
        arr_score = [0] * 11
        for i in combi:
            arr_score[i] += 1
            
        diff = retScore(info, arr_score)
        
        if diff > diff_sum:
            diff_sum = diff
            answer = arr_score
        elif diff == diff_sum:     
            for a, b in zip(answer[-1::-1], arr_score[-1::-1]):
                if b > a:
                    answer = arr_score
                    break
                if a > b:
                    break

    if not answer:
        answer = [-1]
    
    return answer
