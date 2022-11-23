class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # brute-force 로 풀려면 각 coin이 0개~최대로 나눌 수 있는 개수까지를 하나씩 다 해봐야한다.
        
        # dynamic programming
        dp = [amount+1] * (amount + 1)
        dp[0] = 0
        
        for i in range(amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-c])
                    
        if dp[amount] == amount + 1:
            return -1

        return dp[amount]