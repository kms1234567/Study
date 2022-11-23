# https://school.programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque, defaultdict
def bfs(graph, n):
    visited = [0] * (n+1)
    dq = deque([1])
    visited[1] = 1
    
    while dq:
        node = dq.popleft()
        
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = visited[node] + 1
                dq.append(next_node)  
    return visited

def solution(n, edge):
    answer = 0

    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    answer = bfs(graph, n)
    
    return answer.count(max(answer))