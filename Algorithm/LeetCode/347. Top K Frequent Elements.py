from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        
        ans = []
        # value값 정렬로 key값 뽑아내기
        for _, item in zip(range(k), sorted(counter.items(), key = lambda x : x[1], reverse = True)):
            ans.append(item[0])
        
        return ans