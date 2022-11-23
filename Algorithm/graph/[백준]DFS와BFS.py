# https://www.acmicpc.net/problem/1260

from collections import defaultdict
from collections import deque

N, M, V = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)

def dfs(graph , v, visited):
    print(v, end=' ')
    visited[v] = True
    
    for n in sorted(graph[v]):
        if not visited[n]:
            dfs(graph, n, visited)

def bfs(graph, v):
    visited = [False] * (N + 1)
    visited[v] = True
    queue = deque([v])

    while queue:
        n = queue.popleft()
        print(n, end=' ')
        for node in sorted(graph[n]):
            if not visited[node]:
                visited[node] = True
                queue.append(node)


dfs(graph, V, visited)
print()
bfs(graph, V)