from collections import defaultdict

N = int(input())
M = int(input())

adj_list = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

visited = [False] * (N+1)
visited[1] = True

def dfs(node=1):
    for v in adj_list[node]:
        if not visited[v]:
            visited[v] = True
            dfs(v)
dfs()

print(sum(visited)-1)