from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        deque을 이용하는 방법 -> deque은 항상 내림차순으로 유지하여 가장 큰 값이 빠지더라도 그 다음 값이 나오게끔 해야한다.
        -> deque에서는 인덱스를 저장하여 접근이 용이하도록 한다.
        """
        ans = []
        q = deque()
        
        left, right = 0, 0
        while right < len(nums):
            # 그다음으로 큰 숫자 인덱스를 배치한다. 내림차순 형태로
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)
            
            # max_value가 left보다 작으면 pop한다.
            if left > q[0]:
                q.popleft()
            
            if (right + 1) >= k:
                ans.append(nums[q[0]])
                left += 1
            right += 1
        return ans

from collections import defaultdict
from heapq import heappush, heappop
"""
num_dicts로 현재 k거리만큼의 포함되어 있는 숫자들을 개수로 보관한다.
heap에서는 모든 숫자들을 넣고, 만약 max_val 의 개수가 0이라면, heap에서 heappop을 진행하고, 개수가 1이상이 나올때까지 반복한다.
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        heap = []
        num_dicts = defaultdict(int)

        max_val = nums[0]
        for i in range(k):
            num_dicts[nums[i]] += 1
            heappush(heap, -nums[i])
            max_val = max(max_val, nums[i])
        ans.append(max_val)
        
        left, right = 0, k
        while right < len(nums):
            num_dicts[nums[left]] -= 1
            num_dicts[nums[right]] += 1
            heappush(heap, -nums[right])
            
            if nums[right] > max_val:
                max_val = nums[right]
            
            if not num_dicts[max_val]:
                target = -heappop(heap)
                while not num_dicts[target] :
                    target = -heappop(heap)
                max_val = target
                
            ans.append(max_val)
            
            left += 1
            right += 1
        return ans