# 플로이드 - 워셜

from collections import defaultdict

INF = int(1e9)
N, M = map(int, input().split())

graph = [[INF for _ in range(N+1)]for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

X, K = map(int, input().split())

for i in range(1, N+1):
    graph[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

if graph[1][K] + graph[K][X] >= INF:
    print(-1)
else:
    print(graph[1][K] + graph[K][X])