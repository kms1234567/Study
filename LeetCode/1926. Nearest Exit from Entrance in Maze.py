from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def bfs():
            M, N = len(maze), len(maze[0])
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            visited = [[False for _ in range(N)] for _ in range(M)]
            visited[entrance[0]][entrance[1]] = True
            q = deque([[entrance[0], entrance[1], 0]])

            while q:
                x, y, c = q.popleft()
                if [x, y] != [entrance[0], entrance[1]] and (x == 0 or x == M-1 or y == 0 or y == N-1):
                    return c
                    break
                
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < M and 0 <= ny < N and maze[nx][ny] == '.' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append([nx, ny, c+1])
        ans = bfs()
        return ans if ans else -1