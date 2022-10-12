class Solution:
    # 대각선, 위, 아래 중 최소값에 +1을 한 값을 자기 자신으로 한 것이 윗변 아랫변의 높이를 의미한다.
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                if i == 0 or j == 0:
                    if matrix[i][j] == '1':
                        matrix[i][j] = 1
                else:
                    matrix[i][j] = min(int(matrix[i-1][j]), int(matrix[i][j-1]), int(matrix[i-1][j-1])) + 1
                ans = max(ans,matrix[i][j])
        return ans*ans
                