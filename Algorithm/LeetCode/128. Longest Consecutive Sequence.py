from collections import defaultdict
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dicts = defaultdict(bool)
        rmv_dicts = defaultdict(bool)
        
        for num in nums:
            dicts[num] = True

        ans = 0
        # 하나를 기점으로 잡고 퍼져나가기
        for num in nums:
            if rmv_dicts[num]:
                continue
            else:
                front = num - 1
                end = num + 1
                
                while dicts[front]:
                    rmv_dicts[front] = True
                    front -= 1
                while dicts[end]:
                    rmv_dicts[end] = True
                    end += 1
                    
                ans = max(ans, end - front - 1)

        return ans