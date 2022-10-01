class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0
        # 이미 방문한 곳은 제일 최소라는 것 -> bfs
        # l은 r + 1, r은 해당 지점에서 가장 멀리 점프할 수 있는 구간이다.
        # 그 구간안에 있는 곳은 모두 최소 점프 거리가 같다.
        # 결국 해당 구간 제일 오른쪽에 있는 r이 최대 인덱스를 넘었을 경우의 답이 최소 점프수가 된다.
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
                
            l = r + 1
            r = farthest
            res += 1
        return res

class Solution:
    def jump(self, nums: List[int]) -> int:
        INF = 10**9
        len_nums = len(nums)
        dp = [0] + [INF] * (len_nums-1)
        
        # 처음부터 모든 경우의 수를 구하여 최소만 기록
        for i, num in enumerate(nums):
            for n in range(1,num+1):
                if i+n >= len_nums:
                    break
                dp[i+n] = min(dp[i+n], dp[i]+1)
        
        return dp[-1]