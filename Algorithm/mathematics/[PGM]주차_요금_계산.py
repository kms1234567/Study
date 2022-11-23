# https://school.programmers.co.kr/learn/courses/30/lessons/92341

import math
from collections import defaultdict

def changeTime(time):
    total = 0
    h, m = time.split(':')
    total += (int(h) * 60 + int(m))
    
    return total
    
def solution(fees, records):
    answer = []
    
    base_time  = fees[0]
    base_money = fees[1]
    unit_time  = fees[2]
    unit_money = fees[3]
    
    dicts = defaultdict(list)
    
    for record in records:
        record = record.split(' ')
        if record[2] == "IN":
            dicts[record[1]].append(changeTime(record[0]))
            dicts[record[1]].append(-1)
        else:
            dicts[record[1]].pop()
            endTime = changeTime(record[0])
            startTime = dicts[record[1]][-1]
            dicts[record[1]][-1] = endTime - startTime
    
    for key in dicts.keys():
        if dicts[key][-1] == -1:
            dicts[key].pop()
            endTime = changeTime('23:59')
            startTime = dicts[key][-1]
            dicts[key][-1] = endTime - startTime
            
    for key in sorted(dicts.keys()):
        result = base_money
        total_time = sum(dicts[key])
        if total_time <= base_time:
            answer.append(result)
            continue
        else:
            result += (math.ceil((total_time - base_time)/unit_time)) * unit_money
            answer.append(result)
    
    return answer