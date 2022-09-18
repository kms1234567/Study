# https://school.programmers.co.kr/learn/courses/30/lessons/42628

from heapq import heappop, heappush, heapify

def solution(operations):
    # - 붙여서 저장
    hq_max = []
    # 그대로 저장
    hq_min = []
    
    for operation in operations:
        command, number = operation.split(' ')
        if command == 'I':
            num = int(number)
            heappush(hq_min, num)
            heappush(hq_max, -num)
        elif hq_max or hq_min:
            if number[0] == '-':
                num = heappop(hq_min)
                hq_max.remove(-num)
                heapify(hq_max)
            else:
                num = heappop(hq_max)
                hq_min.remove(-num)
                heapify(hq_min)    
    
    if not hq_max:
        return [0, 0]
    else:
        return [-heappop(hq_max), heappop(hq_min)]
