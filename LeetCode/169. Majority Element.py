from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        
        for num in nums:
            counter[num] += 1
        
        # counter의 value중 최대인 key값을 반환
        return max(counter, key = lambda x : counter[x])