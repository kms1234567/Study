# https://school.programmers.co.kr/learn/courses/30/lessons/42627

from heapq import heappush, heappop, heapify
def solution(jobs):
    answer = 0
    
    len_jobs = len(jobs)
    jobs = [[y,x] for x, y in jobs]
    heapify(jobs)
    stk = []
    
    wait = 0;cur = 0

    while jobs or stk:
        if jobs:
            t, w = heappop(jobs)
        else:
            cur += 1
            while stk:
                heappush(jobs, stk.pop())
            continue

        if w > cur:
            stk.append([t,w])
            continue
        else:
            cur += t
            wait += (cur - w)
            while stk:
                heappush(jobs, stk.pop())        

    return int(wait//len_jobs)