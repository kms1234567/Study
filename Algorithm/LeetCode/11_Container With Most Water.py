class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        
        # 왼쪽과 오른쪽에서 줄여나가며, 비교해 나가는 방식을 사용한다.
        left = 0;right = len(height) - 1
        
        while left < right:
            # 왼쪽과 오른쪽 높이중 작은 값과, width(가로거리)를 곱한 값과 현재 ans와 큰지 비교한다.
            ans = max(ans, (right - left) * min(height[left], height[right]))
            
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return ans