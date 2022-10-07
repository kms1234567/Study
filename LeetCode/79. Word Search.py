class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
       # 백트래킹 문제 -> 시간초과코드..
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        
        r = len(board)
        c = len(board[0])
        
        start_list = []
        
        visited = [[False for _ in range(c)] for _ in range(r)]
        
        def dfs(x, y, n):
            ans = False
            
            if n == len(word):
                return True
            
            if x < 0 or x >= r or y < 0 or y >= c or visited[x][y] or word[n] != board[x][y]:
                return False
            
            visited[x][y] = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                ans = ans | dfs(nx, ny, n+1)
            visited[x][y] = False 
            
            return ans
            
        for i in range(r):
            for j in range(c):
                if dfs(i, j, 0):
                    return True
                
        return False



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
       
        r = len(board)
        c = len(board[0])
        
        # set로 푼 코드인데 visited와 뭐가 다른지 잘 모르겠다.
        path = set()
        def dfs(x, y, n):
            ans = False
            
            if n == len(word):
                return True
            
            if x < 0 or x >= r or y < 0 or y >= c or (x, y) in path or word[n] != board[x][y]:
                return False
            
            path.add((x, y))
            ans = (dfs(x+1, y, n+1) or
                  dfs(x-1, y, n+1) or
                  dfs(x, y+1, n+1) or
                  dfs(x, y-1, n+1))
            path.remove((x,y))
            return ans
            
        for i in range(r):
            for j in range(c):
                if dfs(i, j, 0):
                    return True
        return False