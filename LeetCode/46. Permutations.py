class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def back(visited, nums, tmp, ans):
            if len(nums) == len(tmp):
                ans.append(tmp)
                return
            
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    back(visited, nums, tmp+[nums[i]], ans)
                    visited[i] = False
                    
                    
        ans = []
        visited = [False] * len(nums)
        back(visited, nums, [], ans)
        return ans