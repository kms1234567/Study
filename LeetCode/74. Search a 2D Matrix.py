class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = 0
        
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            if matrix[i][n-1] >= target:
                row = i
                break
        
        for j in range(n):
            if matrix[row][j] == target:
                return True
        return False