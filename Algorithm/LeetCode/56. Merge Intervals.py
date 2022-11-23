class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # x의 첫 번째 값을 기준으로 정렬
        intervals.sort(key = lambda x : x[0])
        
        ans = []
        # 현재 x가 전의 값 y보다 작다면 다음으로 보류한다.
        prev_x, prev_y = intervals[0][0], intervals[0][1]
        for x, y in intervals[1:]:
            if prev_y < x:
                ans.append([prev_x, prev_y])
                prev_x, prev_y = x, y
            else:
                prev_y = max(prev_y, y)
        ans.append([prev_x, prev_y])
        return ans