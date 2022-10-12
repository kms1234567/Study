class Solution:
    def rob(self, nums: List[int]) -> int:
        # 전의 집을 먹었을 때의 값 최대
        # 전전의 집중 최대값 + 현재 집을 먹었을 때의 값 두개를 유지
        
        ans = nums[0]
        dp = [[0, nums[0]]] + [[0,0] for _ in range(len(nums)-1)]
        
        for idx, num in enumerate(nums[1:], start = 1):
            if idx == 1:
                dp[idx][0] = dp[idx-1][1]
                dp[idx][1] = num
            else:
                dp[idx][0] = max(dp[idx-1])
                dp[idx][1] = max(dp[idx-2]) + num
            ans = max(ans, max(dp[idx]))
        return ans