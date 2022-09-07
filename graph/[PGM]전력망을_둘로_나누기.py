# https://school.programmers.co.kr/learn/courses/30/lessons/86971


from collections import defaultdict
def dfs(graph, visited, node):
    cnt = 0
    for v in graph[node]:
        if not visited[v]:
            visited[v] = True
            cnt += dfs(graph, visited, v)
    return cnt + 1

def solution(n, wires):
    answer = 100
    graph = defaultdict(list)
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    for a, b in wires:
        visited = [False] * (n+1)
        visited[a] = True;visited[b]=True
        a_cnt = dfs(graph, visited, a)
        b_cnt = dfs(graph, visited, b)
        
        answer = min(answer, abs(a_cnt - b_cnt))
    
    return answer