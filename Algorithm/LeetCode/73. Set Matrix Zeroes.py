class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        m_set = set()
        n_set = set()
        
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    m_set.add(i)
                    n_set.add(j)
                    
        for i in m_set:
            for j in range(n):
                matrix[i][j] = 0
        
        for j in n_set:
            for i in range(m):
                matrix[i][j] = 0