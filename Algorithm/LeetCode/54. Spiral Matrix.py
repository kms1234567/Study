class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        # 무조건 첫 번째 행의 값을 뽑게한다.
        # zip을 이용해 각 값들끼리 묶은 후, 마지막 값을 뽑을 수 있도록 뒤집는다.
        while matrix:
            ans += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return ans

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 첫 번째 행 pop
        # 나머지 행의 마지막 값들 pop
        # 마지막 행 리버스로 가져오기
        # 나머지 행의 첫 번째 값들 pop
        
        ans = []
        
        while matrix:
            ans += matrix.pop(0)
            
            if matrix:
                for i in range(len(matrix)):
                    if not matrix[i]:
                        break
                    ans = ans + [matrix[i].pop()]
            
            if matrix:
                ans += list(reversed(matrix.pop()))
                
            if matrix:
                for i in range(len(matrix)-1,-1,-1):
                    if not matrix[i]:
                        break
                    ans = ans + [matrix[i].pop(0)]
                
        return ans