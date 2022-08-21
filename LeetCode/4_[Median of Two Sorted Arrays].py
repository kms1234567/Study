# https://leetcode.com/problems/median-of-two-sorted-arrays/

# 솔루션
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        
        
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """



# 내 풀이
from heapq import heapify, heappop
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        heapify(nums1)
        
        arr_len = len(nums1)
        isOdd = arr_len % 2 
        if (isOdd):
            for i in range(arr_len//2):
                heappop(nums1)
            return float(heappop(nums1))
        else:
            for i in range((arr_len//2)-1):
                heappop(nums1)
            return (heappop(nums1) + heappop(nums1)) / 2.0
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """