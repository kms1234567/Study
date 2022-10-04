class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 1] + [0] * (n-1)
        
        for i in range(2, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        
        return dp[-1]