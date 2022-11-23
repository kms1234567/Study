class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        R = len(grid)
        C = len(grid[0])
        # visited를 이용하지 않고 들른 좌표 자체를 0으로 변경하는 방법도
        visited = [[False for _ in range(C)] for _ in range(R)]
        ans = 0
        
        def dfs(r, c):
            visited[r][c] = True

            for i in range(4):
                x = r + dx[i]
                y = c + dy[i]
                
                if 0 <= x < R and 0 <= y < C and grid[x][y] == '1' and not visited[x][y]:
                    dfs(x, y)
            
        for i in range(R):
            for j in range(C):
                if grid[i][j]=='1' and not visited[i][j]:
                    dfs(i, j)
                    ans += 1
        return ans