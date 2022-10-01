class Solution:
    def trap(self, height: List[int]) -> int:
        # 투 포인터를 이용한 방식
        ans = 0
        l, r = 0, len(height) - 1
        
        maxL, maxR = height[l], height[r]
        while l < r :
            # 최대값을 갱신하고
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])
            # 최대값이 작은 쪽을 더해주면서 min(maxL,maxR)에 해당 높이를 뺀 값을 더한다.
            # 후에 인덱스를 더해준다.
            if maxL <= maxR:
                ans += (maxL - height[l])
                l += 1
            elif maxR < maxL:
                ans += (maxR - height[r])
                r -= 1
        return ans

class Solution:
    def trap(self, height: List[int]) -> int:
        # 스택을 이용한 풀이
        ans = 0
        stk = []
        
        for i, h in enumerate(height):
            # 올라가는 지점에서 해당 while문을 통과
            while stk and height[stk[-1]] < h:
                # 아래에 있는 인덱스를 꺼낸다.
                btm = stk.pop()
                if not stk:
                    break
                # 아래에 있는 인덱스의 왼쪽과 현재 인덱스 사이의 거리(width)를 구한다.
                distance = i - stk[-1] - 1
                # 해당 가로길이와 왼쪽 높이와 오른쪽 높이중 작은 것에 꺼냈던 인덱스의 높이만큼 빼서 곱해준다.
                area = distance * (min(height[stk[-1]] , h)- height[btm]) 
                
                ans += area
            
            stk.append(i)
        return ans