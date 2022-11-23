class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix)
        C = len(matrix[0])
        
        r, c = R-1, 0
        
        while 0<=r<R and 0<=c<C:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                r -= 1
            elif matrix[r][c] < target:
                c += 1
        
        return False