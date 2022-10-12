class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 최대값이 나오기위한 특징을 알아야 한다.
        # 만약 모든 배열이 양수이면 모두 곱한 값이 최대이고,
        # 음수가 섞여 있다면, 음수끼리 곱했을 때 양이 되는 것까지 고려해야 한다.
        # 그래서 각 지점까지의 최대값과 최소값을 구해놓고, 음이되면 최소값과 곱해서 최대값을 정하고, 최대값과 곱해서 최소값에 저장한다.
        
        dp = []
        ans = max(nums)
        for num in nums:
            if num == 0:
                dp.append([1, 1])
                continue
            else:
                if not dp:
                    dp.append([num, num])
                    continue
                min_val = min(num, dp[-1][1]*num, dp[-1][0]*num)
                max_val = max(num, dp[-1][1]*num, dp[-1][0]*num)
                dp.append([max_val, min_val])
                ans = max(ans, max_val)
        return ans

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp 배열을 사용하지 않고 풀 수 있다.
        curMin, curMax = 1, 1
        ans = max(nums)
        for num in nums:
            if num == 0:
                curMin, curMax = 1, 1
                continue
            else:
                tmp = curMax * num
                curMax = max(num, curMin * num, curMax * num)
                curMin = min(num, curMin * num, tmp)
                ans = max(ans, curMax)
        return ans