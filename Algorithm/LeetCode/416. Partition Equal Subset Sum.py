class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2:
            return False
        # 순회하면서 중복값이 제거될 set에 모든 합을 add한다.
        # set에 해당 값이 없다면 False, 있다면 True이다. 속도를 위해 중간에 발견되면 바로 리턴하도록 했다.
        target = sum_nums // 2
        dp = {0}
        
        for num in nums:
            new_dp = set()
            for s in dp:
                if target == num+s:
                    return True
                new_dp.add(num+s)
                new_dp.add(s)
            dp = new_dp
            
        return True if target in dp else False
        
        
        # 현재 숫자를 포함 시키냐 안 시키는지의 모든 경우의 수 -> brute force
#         if sum(nums) % 2:
#             return False
        
#         target = sum(nums) // 2
        
#         def dfs(n, depth):
#             t = False
            
#             if n == target:
#                 return True
#             if depth == len(nums):
#                 return t
            
#             t = dfs(n, depth+1) | dfs(n+nums[depth], depth+1)

#             return t
        
#         return dfs(0, 0)