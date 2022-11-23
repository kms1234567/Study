from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numSet = set()
        for num in nums:
            if num in numSet:
                return num
            numSet.add(num)