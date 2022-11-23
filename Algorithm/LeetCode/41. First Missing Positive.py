class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        
        prev = 0
        for num in nums:
            # 0보다 작거나 같은 숫자들은  필요없다.
            if num <= 0 :
                continue
            # 해당 숫자를 뺏을 때 1보다 크다는 의미는 중간이 비어있다는 의미이다.
            # 0이 나올수도 있는 이유는 같은 숫자가 중복돼서 나오기 떄문
            if num - prev > 1:
                return prev + 1
            prev = num
            
        return prev + 1
                

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))                
        nums.sort()

        end = nums[-1]
        if end <= 0 :
            return 1
        
        len_nums = len(nums)
        
        prev = 0
        idx = 0
        while nums[idx] <= 0:
            idx += 1
    
        prev = 0
        for i in range(idx, len_nums):
    
            if prev != nums[i]-1:
                return prev+1
            prev = nums[i]
        return end + 1
                