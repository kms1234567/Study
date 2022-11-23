from heapq import heapify, heappush, heappop

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 비용이 있고, 최소의 비용으로 처리해야 하므로, 다익스트라 이용
        m, n = len(grid), len(grid[0])
        INF = 10**9
        dp = [[INF for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        
        dx = [1,0]
        dy = [0,1]
        
        def bfs(x, y):
            q = [[grid[x][y], x, y]]
            heapify(q)
            
            while q:    
                c, x, y = heappop(q)
                    
                if [x, y] == [m-1, n-1]:
                    break
                    
                for i in range(2):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    # 현재 최소비용을 dp에 기록해놓고 dp보다 작아야지만 통과
                    if 0<=nx<m and 0<=ny<n and dp[nx][ny] > c+grid[nx][ny]:
                        dp[nx][ny] = c + grid[nx][ny]
                        heappush(q, [dp[nx][ny], nx, ny])
            
        bfs(0, 0)
        return dp[-1][-1]