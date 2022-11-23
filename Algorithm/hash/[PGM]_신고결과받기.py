# https://school.programmers.co.kr/learn/courses/30/lessons/92334

from collections import defaultdict
def solution(id_list, report, k):
    dicts_accused = defaultdict(int)
    dicts = defaultdict(list)
    report = set(report)
    
    for rep in report:
        reported, accused = rep.split(' ')
        dicts[reported].append(accused)
        
    for val in dicts.values():
        for v in val:
            dicts_accused[v] += 1
    
    banned = []
    for key, val in zip(dicts_accused.keys(), dicts_accused.values()):
        if val >= k:
            banned.append(key)
    
    ans = defaultdict(int)
    for key, val in zip(dicts.keys(), dicts.values()):
        for v in val:
            if v in banned:
                ans[key] += 1
    
    result = []
    for id_val in id_list:
        result.append(ans[id_val])
        
    return result
    