class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for _ in range(len(temperatures))]
        stk = []

        for curr, temp in enumerate(temperatures):
            while stk and stk[-1][1] < temp:
                day = stk.pop()[0]
                ans[day] = curr - day
            stk.append([curr, temp])

        return ans