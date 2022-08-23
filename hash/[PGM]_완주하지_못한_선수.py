# https://school.programmers.co.kr/learn/courses/30/lessons/42576

from collections import defaultdict
def solution(participant, completion):
    dicts = defaultdict(int)
    
    for pt_name in participant:
        dicts[pt_name] += 1
        
    for cp_name in completion:
        dicts[cp_name] -= 1

    for key in dicts.keys():
        if dicts[key]:
            return key