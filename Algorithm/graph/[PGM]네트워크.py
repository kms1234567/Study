# https://school.programmers.co.kr/learn/courses/30/lessons/43162
from collections import defaultdict
def dfs(graph, visited, node):
    
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(graph, visited, next_node)

def solution(n, computers):
    answer = 0
    
    dicts = defaultdict(set)
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] and i!=j:
                dicts[i+1].add(j+1)
                dicts[j+1].add(i+1)
    
    visited = [False] * (n+1)

    for i in range(1, n+1):
        if not visited[i]:
            answer += 1
            visited[i] = True
            dfs(dicts, visited, i)

    return answer