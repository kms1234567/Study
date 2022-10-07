class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 선택한 숫자를 기점으로 왼쪽 서브트리와 오른쪽 서버트리의 경우의 수를 곱한 값을 구하면 된다.
        # index 0은 곱할 때 0이되지 않도록 1을 넣어주고, 1은 노드가 하나이므로 1을 넣어준다.
        # 그러면 2부터 구할 수 있게 된다.
        dp = [1,1] + [0] * (n-1)
        
        for i in range(2, n+1):
            for j in range(1, i+1):
                # j를 기준으로 나눔
                left = j - 1
                right = i - j
                
                dp[i] += (dp[left] * dp[right])
        return dp[n]