class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        maps = [['.' for _ in range(n)] for _ in range(n)]
        ans = []
        
        
        col = []
        positive_dialog = []
        negative_dialog = []
        # row 가 곧 deep의 역할을 한다.
        # col 은 같은 열에 있는 것인지 검사한다.
        # i+j 가 같은 것들은 우측 상향 부분으로 가는 대각선 모음
        # i-j 가 같은 것들은 오측 하향 부분으로 가는 대각선 모음
        # 이 세개가 겹치지 않아야 조건이 성립한다.

        # -> 초기 상태  n = 3  [Q . .]
        # -> 초기 상태  n = 3  [Q . .]
        # -> 초기 상태  n = 3  [Q . .]

        def backtracking(i):
            if i == n:
                tmp = [''.join(row) for row in maps]
                ans.append(tmp)
                return
                
            for j in range(n):
                if j in col or (i+j) in positive_dialog or (i-j) in negative_dialog:
                    continue
                    
                col.append(j)
                positive_dialog.append(i+j)
                negative_dialog.append(i-j)
                maps[i][j] = 'Q'
                backtracking(i+1)
                maps[i][j] = '.'
                col.pop()
                positive_dialog.pop()
                negative_dialog.pop()

        backtracking(0)
        return ans