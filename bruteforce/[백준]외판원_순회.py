# https://www.acmicpc.net/problem/10971
def solution(num_min, v, depth, val):
    if depth == N-1:
        if adj_list[v][0]:
            num_min = min(num_min, val + adj_list[v][0])
        return num_min
    for i in range(N):
        if not visited[i] and adj_list[v][i]:
            visited[i] = 1
            num_min = solution(num_min, i, depth+1, val + adj_list[v][i])
            visited[i] = 0
    return num_min
N = int(input())

adj_list = [[] for _ in range(N)]
for i in range(N):
    num = list(map(int, input().split()))
    for j in num:
        adj_list[i].append(j)

visited = [0]*N

visited[0] = 1
print(solution(10**9, 0, 0, 0))