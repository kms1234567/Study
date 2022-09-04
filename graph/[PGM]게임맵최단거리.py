# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque
def bfs(maps, row, col):
    q = deque([[1, (0,0)]])
    visited = [[False]*col for _ in range(row)]
    visited[0][0] = True
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q:
        cost, coord = q.popleft()
        x = coord[0];y = coord[1]
        
        if coord == (row-1, col-1):
            return cost
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<row and 0<=ny<col and not visited[nx][ny] and maps[nx][ny]:
                # 현재 경로는 이미 최적이라는 것이 보장되므로, 큐에 들어감과 동시에 막아버린다.
                visited[nx][ny] = True
                q.append([cost+1,(nx, ny)])
            
    return -1
        
def solution(maps):
    row = len(maps)
    col = len(maps[0])
    return bfs(maps, row, col)