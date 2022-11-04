class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans, prev = 0, 0

        for i in range(1, len(colors)):
            if colors[i] != colors[prev]:
                prev = i
            else:
                ans += min(neededTime[prev], neededTime[i])
                if neededTime[prev] < neededTime[i] : prev = i 
        return ans

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        stk = [neededTime[0]]

        prev = 0
        for i in range(1, len(colors)):

            if colors[i] == colors[prev]:
                stk.append(neededTime[i])
            else:
                stk.sort(reverse = True)
                while len(stk) > 1:
                    ans += stk.pop()
                stk.pop()
                stk.append(neededTime[i])
            prev = i

        stk.sort(reverse = True)
        while len(stk) > 1: 
            ans += stk.pop()

        return ans