"""
1. heap
2. quick select

heap을 이용한 풀이는 heap은 최초에 k개만큼 heap에 저장하고 가장 작은 값과 다음에 나오는 값들을 비교하여 작은 값이면 넘어가고, 큰 값이면 pop 이후 push를 반복하여 마지막에 heappop을 진행하는 풀이 입니다.

quick select는 피벗을 정하여 왼쪽과 오른쪽을 나누는 것을 반복하는데, 해당 피벗인덱스가 k 번째로 큰 인덱스가 될 때까지 반복합니다.
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def find_at(low, high, idx):
            pivot = partition(low, high)
            
            if pivot > idx:
                return find_at(low, pivot-1, idx)
            if pivot < idx:
                return find_at(pivot+1, high, idx)
            
            return nums[idx]
        
        def partition(low, high):
            p = low
            
            for i in range(low, high):
                if nums[i] < nums[high]:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[high] = nums[high], nums[p]
            return p
            
        return find_at(0, len(nums)-1, len(nums)-k)