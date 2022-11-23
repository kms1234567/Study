# 지금 장애물을 파괴할 수 있는 k의 개수가 다르다면 visited된 것이 아니다.
# 그래서 현재 좌표와 파괴할 수 있는 k의 데이터를 set 자료형에 저장하여, visited로 사용한다.

from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        R, C = len(grid), len(grid[0])
        
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        
        def bfs():
            q = deque()
            q.append((0, 0, k, 0))
            seen = set()
            while q:
                x, y, c, p = q.popleft()
                if [x, y] == [R-1, C-1]:
                    return p
                
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if 0 <= nx < R and 0 <= ny < C :
                        data = (nx, ny, c-grid[nx][ny], p+1)
                        if data[2] >= 0 and not data[0:3] in seen:
                            q.append(data)
                            seen.add(data[0:3])
            return -1
            
        return bfs()
                    