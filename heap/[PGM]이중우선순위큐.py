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

# 22.10.24
from heapq import heapify, heappop, heappush

def solution(operations):
    answer = []

    min_heap = []
    max_heap = []
    data_set = set()
    
    for operation in operations:
        op, num = operation.split(' ')
        num = int(num)
        if op == 'I':
            heappush(min_heap, num)
            heappush(max_heap, -num)
            data_set.add(num)          
        else:
            while data_set:
                if num > 0:
                    data = -heappop(max_heap)
                else:
                    data = heappop(min_heap)
                if data in data_set:
                    data_set.remove(data)
                    break
                
    if not data_set:
        return [0, 0]
    else:
        data = None
        while data not in data_set:
            data = -heappop(max_heap)
        answer.append(data)
        
        data = None
        while data not in data_set:
            data = heappop(min_heap)
        answer.append(data)

    return answer

import heapq

def solution(operations):
    heap = []

    for operation in operations:
        operator, operand = operation.split(' ')
        operand = int(operand)

        if operator == 'I':
            heapq.heappush(heap, operand)
        elif heap:
            if operand < 0:
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))

    if not heap:
        return [0, 0]

    return [max(heap), heap[0]]