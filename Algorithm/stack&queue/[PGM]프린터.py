# https://school.programmers.co.kr/learn/courses/30/lessons/42587

# 깔끔한 풀이
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

# 내풀이
from collections import deque
def solution(priorities, location):
    answer = 0

    idx_priorities = deque()
    for idx, priority in enumerate(priorities):
        idx_priorities.append([priority, idx])

    while idx_priorities:
        p, i = idx_priorities.popleft()
        if idx_priorities:
            m = max(idx_priorities)[0]
        else:
            m = p
            
        if p >= m :
            answer += 1
            if i == location:
                break
        else:
            idx_priorities.append([p, i])
        
    return answer

# 22.10.20
from collections import deque
def solution(priorities, location):
    answer = 0

    sort_pri = sorted(priorities)
    priorities = deque([[p, i] for p, i in zip(priorities, range(len(priorities)))])
    
    while priorities:
        p, i = priorities.popleft()
        if p == sort_pri[-1]:
            sort_pri.pop()
            answer += 1
            if i == location:
                return answer
        else:
            priorities.append([p, i])   
