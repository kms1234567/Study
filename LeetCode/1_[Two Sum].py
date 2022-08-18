# https://leetcode.com/problems/two-sum/

import sys
class Solution(object):
    def twoSum(self, nums, target):
        
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if (nums[i]+nums[j] == target):
                    result = [i,j]
                    return result
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """