# https://school.programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations
def solution(k, dungeons):
    answer = []
    
    tmp = [i for i in range(len(dungeons))]
    dungeons = list(permutations(dungeons, tmp[-1]+1))
    
    for dungeon in dungeons:
        cnt = 0
        fatigue = k
        for need, consumption in dungeon:
            if fatigue >= need:
                fatigue -= consumption
                cnt += 1
            else:
                break
        answer.append(cnt)
    
    return max(answer)