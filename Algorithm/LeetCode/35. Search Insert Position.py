class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        len_nums = len(nums)
        l = 0;r = len_nums-1
        ans = len_nums
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid > target]:
                r = mid - 1
                ans = mid
        
        return ans
            