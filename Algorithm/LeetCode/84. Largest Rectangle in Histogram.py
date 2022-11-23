class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # 스택으로 풀기 -> 인덱스와 높이를 기록, 높이가 자신보다 작은 것이 나온다면 pop을 하면서 기록한다.
        ans = 0
        stk = []
        for idx, h in enumerate(heights):
            if not stk:
                stk.append([idx, h])
                continue
            
            # 자신보다 작은 높이가 나온다면 해당 높이보다 크거나 같은 높이가 나올 때까지 반복한다.
            # 끝마쳤을 때의 높이를 저장한다. 해당 높이 시작의 인덱스는 끝마쳤을 때의 인덱스이기 때문이다.
            start = idx
            while stk and stk[-1][1] > h:
                i, v = stk.pop()
                ans = max(ans,(idx - i) * v)
                start = i
            stk.append([start, h])
        
        while stk:
            i, v = stk.pop()
            ans = max(ans, (len(heights)-i) * v)
            
        return ans
        