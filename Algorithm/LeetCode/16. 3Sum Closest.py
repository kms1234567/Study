# 3sum 문제와 유사

# 하나는 순회하고 투 포인터로 접근해가면서 target 과 가장 가까운 값을 찾는다.

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = nums[0]+nums[1]+nums[2]
        
        nums.sort()
        
        for i, k in enumerate(nums):
            if ans == target:
                break
            l, r = i+1, len(nums)-1
            
            while l < r:
                res = k + nums[l] + nums[r]
                
                if abs(target - res) < abs(target - ans):
                    ans = res
                
                # 타겟과 가장 가까워야 하므로 기준은 0 이아닌 target이다.
                if res > target:
                    r -= 1
                else:
                    l += 1       
                
        return ans