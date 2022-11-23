from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:
        INF = 10 ** 8
        dp = [INF for _ in range(n+1)]
        dp[0] = 0

        def bfs():
            q = deque([0])
            while q:
                pos = q.popleft()
                if pos == n:
                    break
                for j in range(int((n-pos) ** (1/2)), 0, -1):
                    if dp[j**2+pos] > dp[pos]+1:
                        q.append(j**2+pos)
                        dp[j**2+pos] = dp[pos] + 1
        bfs()
        return dp[n] 