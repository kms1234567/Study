from copy import deepcopy
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        # 배열을 돌리는 문제.
        # 외곽부터 차례대로 규칙을 찾아 돌린다.
        cnt = N//2
        copy = deepcopy(matrix)
        for c in range(cnt):
            for i in range(c, N-c):
                for j in range(c, N-c):
                    matrix[i][j] = copy[N-1-j][i]

