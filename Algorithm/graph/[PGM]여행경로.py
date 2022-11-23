# https://school.programmers.co.kr/learn/courses/30/lessons/43164#

from collections import defaultdict

def dfs(graph, visited, start, path, destination_num, ans):
    if len(path) == destination_num:
        ans.append(path)
        
    for node in graph[start]:
        if node in visited[start]:
            visited[start].remove(node)
            dfs(graph, visited, node, path+[node], destination_num, ans)
            visited[start].append(node)

def solution(tickets):
    graph = defaultdict(list)
    visited = defaultdict(list)
    tickets.sort(key = lambda x : x[1])
    
    for start, end in tickets:
        graph[start].append(end)
        visited[start].append(end)
    ans = []
    dfs(graph, visited, 'ICN', ['ICN'], len(tickets)+1, ans)
    return ans[0]