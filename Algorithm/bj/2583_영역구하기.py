from collections import deque
M, N, K = map(int, input().split())

visited = [[False for _ in range(N)] for _ in range(M)]

for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(M-y2, M-y1):
        for j in range(x1, x2):
            visited[i][j] = True

ans = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    area = 1
    q = deque([[x,y]])
    while q:
        r, c = q.popleft()
        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]
            if 0<=nx<M and 0<=ny<N and not visited[nx][ny]:
                area += 1
                visited[nx][ny] = True
                q.append([nx,ny])
    return area

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            ans.append(bfs(i, j))
ans.sort()
print(len(ans))
print(*ans)