class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        # 이 풀이는 항상 작은 값이 첫 번째 위치가 아니라는 가정 하에 푼다.
        # 현재 값이 내 전의 값보다 작으면 현재 값이 가장 작은 값이다.
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[0]