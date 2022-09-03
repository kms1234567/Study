# https://school.programmers.co.kr/learn/courses/30/lessons/12978

# cost가 K를 넘었다는 것은 그 후에것은 볼 필요도 없다
# cost가 통과된 애들의 node만 visited를 True로 해준다.
# 사실 visited의 용도보다는 얘들은 갈 수 있다는 의미. 경로상으로는 중복으로 갈 수 있어야 한다.

from collections import defaultdict
from heapq import heappop, heappush
def solution(N, road, K):
    roads = defaultdict(list)
    for start, end, cost in road:
        roads[start].append((cost, end))
        roads[end].append((cost, start))
        
    visited = [False] * (N+1)
    visited[1] = True
    hq = [[0,1]]
    while hq:
        cost, node = heappop(hq)
        if  cost > K:
            break
        visited[node] = True
        
        for c, n in roads[node]:
            if not visited[n]:
                heappush(hq, (c+cost, n))
    return sum(visited)