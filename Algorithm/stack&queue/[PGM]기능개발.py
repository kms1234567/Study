# https://school.programmers.co.kr/learn/courses/30/lessons/42586

from collections import deque
def solution(progresses, speeds):
    answer = []
    
    progresses = deque(progresses);speeds = deque(speeds)
    
    while progresses:
        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1
        if cnt:
            answer.append(cnt)
        
        for idx, data in enumerate(zip(progresses, speeds)):
            progresses[idx] = data[0] + data[1]
    
    return answer

import math
def solution(progresses, speeds):
    answer = []
    
    target, cnt = math.ceil((100-progresses[0])/speeds[0]), 0
    for p, s in zip(progresses, speeds):
        if math.ceil((100-p)/s) <= target:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            target = math.ceil((100-p)/s)
            
    answer.append(cnt)    
    return answer