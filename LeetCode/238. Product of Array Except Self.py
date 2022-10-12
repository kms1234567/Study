"""
zero 가 두 개이상이면 모두 0이며,
zero 가 하나라면 해당 값만 제외한 모두 곱한 값
zero 가 없다면, 모두 곱한 값에서 해당 인덱스를 나눈 몫이 답입니다.
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_product = 1
        zero_cnt = 0
        
        for num in nums:
            if not num:
                zero_cnt += 1
                continue
            all_product *= num
        ans = []
        if zero_cnt >= 2:
            return [0 for _ in range(len(nums))]
        else:
            for num in nums:
                if not num:
                    ans.append(all_product)
                elif zero_cnt:
                    ans.append(0)
                else:
                    ans.append(all_product // num)
        return ans