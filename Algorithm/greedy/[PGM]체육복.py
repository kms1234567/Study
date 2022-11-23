# https://school.programmers.co.kr/learn/courses/30/lessons/42862
# 좋은 풀이
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    _reserve.sort();_lost.sort() 
    for r in _reserve:
        f = r - 1
        b = r + 1
            
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
            
    return n - len(_lost)

# 내 풀이
from collections import defaultdict
def solution(n, lost, reserve):
    dicts = defaultdict(int)
    lost = lost + [0] * (n - len(lost))
    reserve = reserve + [0] * (n - len(reserve))
    
    for idx ,data in enumerate(zip(lost, reserve),start=1):
        l = data[0];r=data[1]
        dicts[idx] += 1;dicts[l] -= 1;dicts[r] += 1

    for key in dicts.keys():
        val = dicts[key]
        
        if not key or val <= 1:
            continue
        
        target = 0
        # 1은 오른쪽에게만
        if key == 1 :
            if not dicts[key+1]:
                target = key + 1
        # n은 왼쪽에게만
        elif key == n:
            if not dicts[key-1]:
                target = key - 1
        # 기본으로 왼쪽에게 빌려줌
        else:
            if not dicts[key-1]:
                target = key - 1
            elif not dicts[key+1]:
                target = key + 1
           
        if target:
            dicts[target] += 1
            dicts[key] -= 1
            
    dicts[0] = 0  
    answer = [1 if val >= 1 else 0 for val in dicts.values()]
    return sum(answer)