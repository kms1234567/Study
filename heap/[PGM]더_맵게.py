# https://school.programmers.co.kr/learn/courses/30/lessons/42626

from heapq import heapify,heappush,heappop
def solution(scoville, K):
    answer = 0
    
    len_scoville = len(scoville)
    heapify(scoville)
    while len_scoville >= 2 and scoville[0] < K:
        answer += 1
        heappush(scoville, heappop(scoville) + 2 * heappop(scoville))
        len_scoville -= 1
        
    if scoville[0] < K:
        return -1
    return answer